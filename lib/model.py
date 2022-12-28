import pandas as pd
import numpy as np
from gurobipy import Model, GRB, QuadExpr, quicksum
import torch
import csv

def optimize(filename_cons, filename_obj, filename_microdata):
    # define all the input data for the model
    cons = pd.read_csv(filename_cons)

    # set up parameters
    n1, n2, n3, n4, n5 = 8, 2, 2, 63, 2
    N = n1 * n2 * n3 * n4 * n5         # number of attribute combinations: HHGQ (8) ∗ VOTINGAGE (2) ∗ HISPANIC (2) ∗ RACE (63) ∗ SEX (2)

    time = 0
    with open(filename_obj, 'w', newline='') as f1:
        wr1 = csv.writer(f1)
        wr1.writerow(["GEOID10", "obj"])

        with open(filename_microdata, 'w', newline='') as f2:
            wr2 = csv.writer(f2)
            # set up column names
            col_names = ["GEOID10"]
            mtx_names = np.empty((n1, n2, n3, n4, n5), dtype="U10")
            for k1 in range(n1):
                for k2 in range(n2):
                    for k3 in range(n3):
                        for k4 in range(n4):
                            for k5 in range(n5):
                                mtx_names[k1, k2, k3, k4, k5] = str(k1).zfill(2) + str(k2).zfill(2) + str(k3).zfill(2) + str(k4).zfill(2) + str(k5).zfill(2)
            col_names.extend(mtx_names.flatten())
            wr2.writerow(col_names)

            for idx, row in cons.iterrows():
                GEOID10 = row["GEOID10"]

                A = torch.tensor(range(N))
                A = A.reshape([n1, n2, n3, n4, n5])

                # initialize model
                m = Model('td')
                m.Params.LogToConsole = 0

                # add objective function
                obj = QuadExpr()

                # add variables and constraints
                h = {}      ## detailed mtxogram (decision vairable)
                for i in range(N):
                    h[i] = m.addVar(obj=0, vtype=GRB.INTEGER, lb=0, ub=row["P0010001"], name="h_%d"%(i))
                m.update()

                ## P5: HISPANIC OR LATINO ORIGIN BY RACE
                q1 = cons.loc[:, cons.columns.str.startswith("P005")].to_numpy()
                res1, col_idx = {}, 0
                for x in range(n3):  # hispanic
                    mtx_idx_two_or_more = []
                    for y in range(n4):  # race   
                        if y >= 0 and y <= 5:
                            mtx_idx = torch.flatten(A[:, :, x, y, :]).tolist()
                            res1[col_idx] = m.addVar(obj=0, vtype=GRB.INTEGER, name="res1_%d"%(col_idx))
                            obj += res1[col_idx] * res1[col_idx]
                            m.addConstr(res1[col_idx] == q1[idx, col_idx] - quicksum(h[i] for i in mtx_idx))
                            m.update()
                            col_idx += 1
                        else:
                            mtx_idx = torch.flatten(A[:, :, x, y, :]).tolist()
                            mtx_idx_two_or_more.extend(mtx_idx)
                    res1[col_idx] = m.addVar(obj=0, vtype=GRB.INTEGER, name="res1_%d"%(col_idx))
                    obj += res1[col_idx] * res1[col_idx]
                    m.addConstr(res1[col_idx] == q1[idx, col_idx] - quicksum(h[i] for i in mtx_idx_two_or_more))
                    m.update()
                    col_idx += 1

                ## P8: RACE
                q2 = cons.loc[:, cons.columns.str.startswith("P008")].to_numpy()
                res2, col_idx = {}, 0   
                for x in range(n4):  # race
                    mtx_idx = torch.flatten(A[:, :, :, x, :]).tolist()
                    res2[col_idx] = m.addVar(obj=0, vtype=GRB.INTEGER, name="res2_%d"%(col_idx))
                    obj += res2[col_idx] * res2[col_idx]
                    m.addConstr(res2[col_idx] == q2[idx, col_idx] - quicksum(h[i] for i in mtx_idx))
                    m.update()
                    col_idx += 1

                ## P9: HISPANIC OR LATINO, AND NOT HISPANIC OR LATINO BY RACE
                q3 = cons.loc[:, cons.columns.str.startswith("P00900")].to_numpy()
                res3, col_idx = {}, 0    
                for x in range(n4):  # race
                    mtx_idx = torch.flatten(A[:, :, 0, x, :]).tolist()
                    res3[col_idx] = m.addVar(obj=0, vtype=GRB.INTEGER, name="res3_%d"%(col_idx))
                    obj += res3[col_idx] * res3[col_idx]
                    m.addConstr(res3[col_idx] == q3[idx, col_idx] - quicksum(h[i] for i in mtx_idx))
                    m.update()
                    col_idx += 1

                ## P12: SEX BY AGE BY RACE
                q4 = cons.loc[:, cons.columns.str.startswith("P012")].to_numpy()
                res4, col_idx = {}, 0   
                for x in range(n4):  # race
                    if x >= 0 and x <= 5:
                        for y in range(n5):  # sex
                            for z in range(n2):  # voting age
                                mtx_idx = torch.flatten(A[:, z, :, x, y]).tolist()
                                res4[col_idx] = m.addVar(obj=0, vtype=GRB.INTEGER, name="res4_%d"%(col_idx))
                                obj += res4[col_idx] * res4[col_idx]
                                m.addConstr(res4[col_idx] == q4[idx, col_idx] - quicksum(h[i] for i in mtx_idx))
                                m.update()
                                col_idx += 1
                for y in range(n5):  # sex
                    for z in range(n2):  # voting age
                        mtx_idx_two_or_more = []
                        for x in range(n4):  # race
                            if x > 5:
                                mtx_idx = torch.flatten(A[:, z, :, x, y]).tolist()
                                mtx_idx_two_or_more.extend(mtx_idx)
                        res4[col_idx] = m.addVar(obj=0, vtype=GRB.INTEGER, name="res4_%d"%(col_idx))
                        obj += res4[col_idx] * res4[col_idx]
                        m.addConstr(res4[col_idx] == q4[idx, col_idx] - quicksum(h[i] for i in mtx_idx_two_or_more))
                        m.update()
                        col_idx += 1

                ## P43: GROUP QUARTERS POPULATION BY SEX BY AGE BY GROUP QUARTERS TYPE
                q5 = cons.loc[:, cons.columns.str.startswith("P043")].to_numpy()
                res5, col_idx = {}, 0     
                for x in range(n5):  # sex
                    for y in range(n2):  # voting age
                        for z in range(n1):  # hhgq
                            mtx_idx = torch.flatten(A[z, y, :, :, x]).tolist()
                            res5[col_idx] = m.addVar(obj=0, vtype=GRB.INTEGER, name="res5_%d"%(col_idx))
                            obj += res5[col_idx] * res5[col_idx]
                            m.addConstr(res5[col_idx] == q5[idx, col_idx] - quicksum(h[i] for i in mtx_idx))
                            m.update()
                            col_idx += 1            

                m.setObjective(obj, GRB.MINIMIZE)
                m.optimize()

                # write mtxogram values
                mtx_values = [GEOID10]
                var_values = [int(var.X) for var in m.getVars() if 'h' == str(var.VarName[0])]
                mtx_values.extend(var_values)
                wr2.writerow(mtx_values)

                # write objective values
                obj = m.getObjective().getValue()
                wr1.writerow([GEOID10, obj])
                time += m.Runtime
                print(idx, time)
                