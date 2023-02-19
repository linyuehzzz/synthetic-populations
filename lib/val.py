import pandas as pd
import numpy as np
import torch
from numpy.linalg import norm
import matplotlib.pyplot as plt

def int_val(filename_mtx, n1, n2, n3, n4, n5):
    N = n1 * n2 * n3 * n4 * n5         # number of attribute combinations: HHGQ (8) ∗ VOTINGAGE (2) ∗ HISPANIC (2) ∗ RACE (63) ∗ SEX (2)
    mtx0 = pd.read_csv(filename_mtx)
    mtx = mtx0[mtx0.columns[1:]]

    filename_cons = 'data/guernsey/microdata/guernsey_cons.csv'
    cons = pd.read_csv(filename_cons)
    cons = cons.drop(columns=["P0010001"])
    col_names = cons.columns[1:]

    A = torch.tensor(range(N))
    A = A.reshape([n1, n2, n3, n4, n5])

    cons_fit, col_idx = pd.DataFrame(), 0
    cons_fit["GEOID10"] = mtx0["GEOID10"]

    ## P5: HISPANIC OR LATINO ORIGIN BY RACE
    for x in range(n3):  # hispanic
        mtx_idx_two_or_more = []
        for y in range(n4):  # race   
            if y >= 0 and y <= 5:
                new_col = pd.DataFrame(index=cons_fit.index)
                mtx_idx = torch.flatten(A[:, :, x, y, :]).tolist()
                new_col[col_names[col_idx]] = pd.DataFrame(mtx.iloc[:, mtx_idx].sum(axis=1), index=cons_fit.index)
                cons_fit = pd.concat([cons_fit, new_col], axis=1)
                col_idx += 1
            else:
                mtx_idx = torch.flatten(A[:, :, x, y, :]).tolist()
                mtx_idx_two_or_more.extend(mtx_idx)
        new_col = pd.DataFrame(index=cons_fit.index)
        new_col[col_names[col_idx]] = pd.DataFrame(mtx.iloc[:, mtx_idx_two_or_more].sum(axis=1), index=cons_fit.index)
        cons_fit = pd.concat([cons_fit, new_col], axis=1)
        col_idx += 1

    ## P8: RACE
    for x in range(n4):  # race
        new_col = pd.DataFrame(index=cons_fit.index)
        mtx_idx = torch.flatten(A[:, :, :, x, :]).tolist()
        new_col[col_names[col_idx]] = pd.DataFrame(mtx.iloc[:, mtx_idx].sum(axis=1), index=cons_fit.index)
        cons_fit = pd.concat([cons_fit, new_col], axis=1)
        col_idx += 1

    ## P9: HISPANIC OR LATINO, AND NOT HISPANIC OR LATINO BY RACE
    for x in range(n4):  # race
        new_col = pd.DataFrame(index=cons_fit.index)
        mtx_idx = torch.flatten(A[:, :, 0, x, :]).tolist()
        new_col[col_names[col_idx]] = pd.DataFrame(mtx.iloc[:, mtx_idx].sum(axis=1), index=cons_fit.index)
        cons_fit = pd.concat([cons_fit, new_col], axis=1)
        col_idx += 1

    ## P12: SEX BY AGE BY RACE
    for x in range(n4):  # race
        if x >= 0 and x <= 5:
            for y in range(n5):  # sex
                for z in range(n2):  # voting age
                    new_col = pd.DataFrame(index=cons_fit.index)
                    mtx_idx = torch.flatten(A[:, z, :, x, y]).tolist()
                    new_col[col_names[col_idx]] = pd.DataFrame(mtx.iloc[:, mtx_idx].sum(axis=1), index=cons_fit.index)
                    cons_fit = pd.concat([cons_fit, new_col], axis=1)
                    col_idx += 1
    for y in range(n5):  # sex
        for z in range(n2):  # voting age
            mtx_idx_two_or_more = []
            for x in range(n4):  # race
                if x > 5:
                    mtx_idx = torch.flatten(A[:, z, :, x, y]).tolist()
                    mtx_idx_two_or_more.extend(mtx_idx)
            new_col = pd.DataFrame(index=cons_fit.index)
            new_col[col_names[col_idx]] = pd.DataFrame(mtx.iloc[:, mtx_idx_two_or_more].sum(axis=1), index=cons_fit.index)
            cons_fit = pd.concat([cons_fit, new_col], axis=1)
            col_idx += 1

    ## P43: GROUP QUARTERS POPULATION BY SEX BY AGE BY GROUP QUARTERS TYPE   
    for x in range(n5):  # sex
        for y in range(n2):  # voting age
            for z in range(n1):  # hhgq
                new_col = pd.DataFrame(index=cons_fit.index)
                mtx_idx = torch.flatten(A[z, y, :, :, x]).tolist()
                new_col[col_names[col_idx]] = pd.DataFrame(mtx.iloc[:, mtx_idx].sum(axis=1), index=cons_fit.index)
                cons_fit = pd.concat([cons_fit, new_col], axis=1)
                col_idx += 1
    
    # prepare data
    cons_df = cons.set_index(["GEOID10"])
    cons_df = cons_df.T.stack().reset_index()
    cons_df = cons_df.rename(columns={0: "SF1", "level_0": "PREDICATE"})

    cons_fit_df = cons_fit.set_index(["GEOID10"])
    cons_fit_df = cons_fit_df.T.stack().reset_index()
    cons_fit_df = cons_fit_df.rename(columns={0: "FIT", "level_0": "PREDICATE"})

    all_df = pd.merge(cons_df, cons_fit_df, how='inner')
    all_df["TAB"] = all_df["PREDICATE"].str[:4]
    p5_df = all_df[all_df["TAB"] == "P005"]
    p8_df = all_df[all_df["TAB"] == "P008"]
    p9_df = all_df[all_df["TAB"] == "P009"]
    p43_df = all_df[all_df["TAB"] == "P043"]
    all_df["TAB"] = all_df["PREDICATE"].str[:5]
    p12A_df = all_df[all_df["TAB"] == "P012A"]
    p12B_df = all_df[all_df["TAB"] == "P012B"]
    p12C_df = all_df[all_df["TAB"] == "P012C"]
    p12D_df = all_df[all_df["TAB"] == "P012D"]
    p12E_df = all_df[all_df["TAB"] == "P012E"]
    p12F_df = all_df[all_df["TAB"] == "P012F"]
    p12G_df = all_df[all_df["TAB"] == "P012G"]

    # compute difference
    print("P5:", np.linalg.norm(p5_df["SF1"]-p5_df["FIT"]) ** 2)
    print("P8:", np.linalg.norm(p8_df["SF1"]-p8_df["FIT"]) ** 2)
    print("P9:", np.linalg.norm(p9_df["SF1"]-p9_df["FIT"]) ** 2)
    print("p12A:", np.linalg.norm(p12A_df["SF1"]-p12A_df["FIT"]) ** 2)
    print("p12B:", np.linalg.norm(p12B_df["SF1"]-p12B_df["FIT"]) ** 2)
    print("p12C:", np.linalg.norm(p12C_df["SF1"]-p12C_df["FIT"]) ** 2)
    print("p12D:", np.linalg.norm(p12D_df["SF1"]-p12D_df["FIT"]) ** 2)
    print("p12E:", np.linalg.norm(p12E_df["SF1"]-p12E_df["FIT"]) ** 2)
    print("p12F:", np.linalg.norm(p12F_df["SF1"]-p12F_df["FIT"]) ** 2)
    print("p12G:", np.linalg.norm(p12G_df["SF1"]-p12G_df["FIT"]) ** 2)
    print("P43:", np.linalg.norm(p43_df["SF1"]-p43_df["FIT"]) ** 2)


def ext_val(filename_pums, filename_mtx, filename_ext_val, n1, n2, n3, n4, n5):
    # prepare pums
    pums = pd.read_csv(filename_pums)
    mtx_names = np.empty((n2, n3, n4, n5), dtype="U10")
    for k2 in range(n2):
        for k3 in range(n3):
            for k4 in range(n4):
                for k5 in range(n5):
                    mtx_names[k2, k3, k4, k5] = str(k2).zfill(2) + str(k3).zfill(2) + str(k4).zfill(2) + str(k5).zfill(2)
    mtx_names = mtx_names.flatten()
                    
    pums_mtx = []
    for col in mtx_names:
        va, e, r, s = int(col[0:2]) + 1, int(col[2:4]) + 1, int(col[4:6]) + 1, int(col[6:8]) + 1
        val = len(pums[(pums['AGEP'] == va) & (pums['HISP'] == e) & (pums['RAC1P'] == r) & (pums['SEX'] == s)])
        pums_mtx.append(val)
    pums_mtx = np.array(pums_mtx)

    # prepare synthetic data
    mtx = pd.read_csv(filename_mtx)
    mtx = mtx[mtx.columns[1:]]
    mtx = mtx.sum().to_frame().T
    col_names = mtx.columns

    mtx_names = np.empty((n2, n3, n4, n5), dtype="U10")
    for k2 in range(n2):
        for k3 in range(n3):
            for k4 in range(n4):
                for k5 in range(n5):
                    mtx_names[k2, k3, k4, k5] = str(k2).zfill(2) + str(k3).zfill(2) + str(k4).zfill(2) + str(k5).zfill(2)
    mtx_names = mtx_names.flatten()

    mtx_fit = []
    for col in mtx_names:
        r = int(col[4:6]) + 1
        if r < 7:
            mtx_fit.append(np.sum(mtx.loc[:, mtx.columns.str.endswith(col)].to_numpy(), axis=1)[0])
        else:
            val = 0
            for i in range(7, 64):
                postfix = col[0:2] + col[2:4] + "%s" % '{number:0{width}d}'.format(width=2, number=i) + col[6:8]
                val += np.sum(mtx.loc[:, mtx.columns.str.endswith(postfix)].to_numpy(), axis=1)[0]
            mtx_fit.append(val)
    mtx_fit = np.array(mtx_fit)

    plt.rcParams["figure.figsize"] = (3,3)
    df = pd.DataFrame({"pums": pums_mtx})
    df["fit"] = mtx_fit

    c = round(np.dot(mtx_fit, pums_mtx)/(norm(mtx_fit)*norm(pums_mtx)), 4)
    ax = df.plot.scatter(x="pums", y="fit",c='cyan')
    ax.set_xlabel("ACS PUMS")
    ax.set_ylabel("SASM")
    ax.set(title="$c$=" + str(c))
    ax.get_figure().savefig(filename_ext_val)
