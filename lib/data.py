import pandas as pd

def prepare_sf1(filename_p1, filename_p5, filename_p8, filename_p9, filename_p12A, filename_p12B, filename_p12C, filename_p12D, filename_p12E, filename_p12F, filename_p12G, filename_p43, filename_cons):
    ## P1: TOTAL POPULATION
    data_p1 = pd.read_csv(filename_p1)
    data_p1 = data_p1.drop(columns=["FILEID", "STUSAB", "SUMLEV", "LOGRECNO", "REGION", "DIVISION", "STATE", "COUNTY",
                                    "TRACT", "BLOCK"])

    ## P5: HISPANIC OR LATINO ORIGIN BY RACE
    data_p5 = pd.read_csv(filename_p5)
    data_p5 = data_p5.drop(columns=["FILEID", "STUSAB", "SUMLEV", "LOGRECNO", "REGION", "DIVISION", "STATE", "COUNTY",
                                    "TRACT", "BLOCK", "P0050001", "P0050002", "P0050010"])

    ## P8: RACE
    data_p8 = pd.read_csv(filename_p8)
    data_p8 = data_p8.drop(columns=["FILEID", "STUSAB", "SUMLEV", "LOGRECNO", "REGION", "DIVISION", "STATE", "COUNTY",
                                    "TRACT", "BLOCK", "P0080001", "P0080002", "P0080009", "P0080010", "P0080026", 
                                    "P0080047", "P0080063", "P0080070"])

    ## P9: HISPANIC OR LATINO, AND NOT HISPANIC OR LATINO BY RACE
    data_p9 = pd.read_csv(filename_p9)
    data_p9 = data_p9.drop(columns=["FILEID", "STUSAB", "SUMLEV", "LOGRECNO", "REGION", "DIVISION", "STATE", "COUNTY",
                                    "TRACT", "BLOCK", "P0090001", "P0090002", "P0090003", "P0090004", "P0090011", 
                                    "P0090012", "P0090028", "P0090049", "P0090065", "P0090072"])

    ## P12A: SEX BY AGE (WHITE ALONE)
    data_p12A = pd.read_csv(filename_p12A)
    data_p12A["P012A00A"] = sum([data_p12A["P012A0%s" % '{number:0{width}d}'.format(width=2, number=i)] 
                                for i in range(3, 7)])
    data_p12A["P012A00B"] = sum([data_p12A["P012A0%s" % '{number:0{width}d}'.format(width=2, number=i)] 
                                for i in range(7, 26)])
    data_p12A["P012A00C"] = sum([data_p12A["P012A0%s" % '{number:0{width}d}'.format(width=2, number=i)] 
                                for i in range(27, 31)])
    data_p12A["P012A00D"] = sum([data_p12A["P012A0%s" % '{number:0{width}d}'.format(width=2, number=i)] 
                                for i in range(31, 50)])
    data_p12A = data_p12A[["P012A00A", "P012A00B", "P012A00C", "P012A00D"]]

    ## P12B: SEX BY AGE (BLACK OR AFRICAN AMERICAN ALONE)
    data_p12B = pd.read_csv(filename_p12B)
    data_p12B["P012B00A"] = sum([data_p12B["P012B0%s" % '{number:0{width}d}'.format(width=2, number=i)] 
                                for i in range(3, 7)])
    data_p12B["P012B00B"] = sum([data_p12B["P012B0%s" % '{number:0{width}d}'.format(width=2, number=i)] 
                                for i in range(7, 26)])
    data_p12B["P012B00C"] = sum([data_p12B["P012B0%s" % '{number:0{width}d}'.format(width=2, number=i)] 
                                for i in range(27, 31)])
    data_p12B["P012B00D"] = sum([data_p12B["P012B0%s" % '{number:0{width}d}'.format(width=2, number=i)] 
                                for i in range(31, 50)])
    data_p12B = data_p12B[["P012B00A", "P012B00B", "P012B00C", "P012B00D"]]

    ## P12C: SEX BY AGE (AMERICAN INDIAN AND ALASKA NATIVE ALONE)
    data_p12C = pd.read_csv(filename_p12C)
    data_p12C["P012C00A"] = sum([data_p12C["P012C0%s" % '{number:0{width}d}'.format(width=2, number=i)] 
                                for i in range(3, 7)])
    data_p12C["P012C00B"] = sum([data_p12C["P012C0%s" % '{number:0{width}d}'.format(width=2, number=i)] 
                                for i in range(7, 26)])
    data_p12C["P012C00C"] = sum([data_p12C["P012C0%s" % '{number:0{width}d}'.format(width=2, number=i)] 
                                for i in range(27, 31)])
    data_p12C["P012C00D"] = sum([data_p12C["P012C0%s" % '{number:0{width}d}'.format(width=2, number=i)] 
                                for i in range(31, 50)])
    data_p12C = data_p12C[["P012C00A", "P012C00B", "P012C00C", "P012C00D"]]

    ## P12D: SEX BY AGE (ASIAN ALONE)
    data_p12D = pd.read_csv(filename_p12D)
    data_p12D["P012D00A"] = sum([data_p12D["P012D0%s" % '{number:0{width}d}'.format(width=2, number=i)] 
                                for i in range(3, 7)])
    data_p12D["P012D00B"] = sum([data_p12D["P012D0%s" % '{number:0{width}d}'.format(width=2, number=i)] 
                                for i in range(7, 26)])
    data_p12D["P012D00C"] = sum([data_p12D["P012D0%s" % '{number:0{width}d}'.format(width=2, number=i)] 
                                for i in range(27, 31)])
    data_p12D["P012D00D"] = sum([data_p12D["P012D0%s" % '{number:0{width}d}'.format(width=2, number=i)] 
                                for i in range(31, 50)])
    data_p12D = data_p12D[["P012D00A", "P012D00B", "P012D00C", "P012D00D"]]

    ## P12E: SEX BY AGE (NATIVE HAWAIIAN AND OTHER PACIFIC ISLANDER ALONE)
    data_p12E = pd.read_csv(filename_p12E)
    data_p12E["P012E00A"] = sum([data_p12E["P012E0%s" % '{number:0{width}d}'.format(width=2, number=i)] 
                                for i in range(3, 7)])
    data_p12E["P012E00B"] = sum([data_p12E["P012E0%s" % '{number:0{width}d}'.format(width=2, number=i)] 
                                for i in range(7, 26)])
    data_p12E["P012E00C"] = sum([data_p12E["P012E0%s" % '{number:0{width}d}'.format(width=2, number=i)] 
                                for i in range(27, 31)])
    data_p12E["P012E00D"] = sum([data_p12E["P012E0%s" % '{number:0{width}d}'.format(width=2, number=i)] 
                                for i in range(31, 50)])
    data_p12E = data_p12E[["P012E00A", "P012E00B", "P012E00C", "P012E00D"]]

    ## P12F: SEX BY AGE (SOME OTHER RACE ALONE)
    data_p12F = pd.read_csv(filename_p12F)
    data_p12F["P012F00A"] = sum([data_p12F["P012F0%s" % '{number:0{width}d}'.format(width=2, number=i)] 
                                for i in range(3, 7)])
    data_p12F["P012F00B"] = sum([data_p12F["P012F0%s" % '{number:0{width}d}'.format(width=2, number=i)] 
                                for i in range(7, 26)])
    data_p12F["P012F00C"] = sum([data_p12F["P012F0%s" % '{number:0{width}d}'.format(width=2, number=i)] 
                                for i in range(27, 31)])
    data_p12F["P012F00D"] = sum([data_p12F["P012F0%s" % '{number:0{width}d}'.format(width=2, number=i)] 
                                for i in range(31, 50)])
    data_p12F = data_p12F[["GEOID10", "P012F00A", "P012F00B", "P012F00C", "P012F00D"]]

    ## P12G: SEX BY AGE (TWO OR MORE RACES)
    data_p12G = pd.read_csv(filename_p12G)
    data_p12G["P012G00A"] = sum([data_p12G["P012G0%s" % '{number:0{width}d}'.format(width=2, number=i)] 
                                for i in range(3, 7)])
    data_p12G["P012G00B"] = sum([data_p12G["P012G0%s" % '{number:0{width}d}'.format(width=2, number=i)] 
                                for i in range(7, 26)])
    data_p12G["P012G00C"] = sum([data_p12G["P012G0%s" % '{number:0{width}d}'.format(width=2, number=i)] 
                                for i in range(27, 31)])
    data_p12G["P012G00D"] = sum([data_p12G["P012G0%s" % '{number:0{width}d}'.format(width=2, number=i)] 
                                for i in range(31, 50)])
    data_p12G = data_p12G[["P012G00A", "P012G00B", "P012G00C", "P012G00D"]]

    ## P43: GROUP QUARTERS POPULATION BY SEX BY AGE BY GROUP QUARTERS TYPE
    data_p43 = pd.read_csv(filename_p43)
    data_p43["P043A001"] = data_p12A["P012A00A"] + data_p12B["P012B00A"] + data_p12C["P012C00A"]+ data_p12D["P012D00A"] + data_p12E["P012E00A"] + data_p12F["P012F00A"] + data_p12G["P012G00A"] - data_p43["P0430003"]
    data_p43["P043A002"], data_p43["P043A003"], data_p43["P043A004"], data_p43["P043A005"] = data_p43[["P0430005"]], data_p43[["P0430006"]], data_p43[["P0430007"]], data_p43[["P0430008"]]
    data_p43["P043A006"], data_p43["P043A007"], data_p43["P043A008"] = data_p43[["P0430010"]], data_p43[["P0430011"]], data_p43[["P0430012"]]
    data_p43["P043A009"] = data_p12A["P012A00B"] + data_p12B["P012B00B"] + data_p12C["P012C00B"]+ data_p12D["P012D00B"] + data_p12E["P012E00B"] + data_p12F["P012F00B"] + data_p12G["P012G00B"] - data_p43["P0430013"] - data_p43["P0430023"]
    data_p43["P043A010"] = sum([data_p43["P0430015"], data_p43["P0430025"]])
    data_p43["P043A011"] = sum([data_p43["P0430016"], data_p43["P0430026"]])
    data_p43["P043A012"] = sum([data_p43["P0430017"], data_p43["P0430027"]])
    data_p43["P043A013"] = sum([data_p43["P0430018"], data_p43["P0430028"]])
    data_p43["P043A014"] = sum([data_p43["P0430020"], data_p43["P0430030"]])
    data_p43["P043A015"] = sum([data_p43["P0430021"], data_p43["P0430031"]])
    data_p43["P043A016"] = sum([data_p43["P0430022"], data_p43["P0430032"]])
    data_p43["P043A017"] = data_p12A["P012A00C"] + data_p12B["P012B00C"] + data_p12C["P012C00C"]+ data_p12D["P012D00C"] + data_p12E["P012E00C"] + data_p12F["P012F00C"] + data_p12G["P012G00C"] - data_p43["P0430034"]
    data_p43["P043A018"], data_p43["P043A019"], data_p43["P043A020"], data_p43["P043A021"] = data_p43[["P0430036"]], data_p43[["P0430037"]], data_p43[["P0430038"]], data_p43[["P0430039"]]
    data_p43["P043A022"], data_p43["P043A023"], data_p43["P043A024"] = data_p43[["P0430041"]], data_p43[["P0430042"]], data_p43[["P0430043"]]
    data_p43["P043A025"] = data_p12A["P012A00D"] + data_p12B["P012B00D"] + data_p12C["P012C00D"]+ data_p12D["P012D00D"] + data_p12E["P012E00D"] + data_p12F["P012F00D"] + data_p12G["P012G00D"] - data_p43["P0430044"] - data_p43["P0430054"]
    data_p43["P043A026"] = sum([data_p43["P0430046"], data_p43["P0430056"]])
    data_p43["P043A027"] = sum([data_p43["P0430047"], data_p43["P0430057"]])
    data_p43["P043A028"] = sum([data_p43["P0430048"], data_p43["P0430058"]])
    data_p43["P043A029"] = sum([data_p43["P0430049"], data_p43["P0430059"]])
    data_p43["P043A030"] = sum([data_p43["P0430051"], data_p43["P0430061"]])
    data_p43["P043A031"] = sum([data_p43["P0430052"], data_p43["P0430062"]])
    data_p43["P043A032"] = sum([data_p43["P0430053"], data_p43["P0430063"]])
    data_p43 = data_p43[["P043A0%s" % '{number:0{width}d}'.format(width=2, number=i) for i in range(1, 33)]]                   

    cons = pd.concat([data_p1, data_p5, data_p8, data_p9, data_p12A, data_p12B, data_p12C, data_p12D, data_p12E, data_p12F, data_p12G, data_p43], 
                    axis=1, join='inner')

    # shift column "GEOID10" to first position
    first_column = cons.pop("GEOID10")
    # insert column using insert(position,column_name,first_column) function
    cons.insert(0, "GEOID10", first_column)

    cons.to_csv(filename_cons, index=False)


def convert_mtx_to_microdata(filename_mtx, filename_microdata):
    mtx = pd.read_csv(filename_mtx)
    mtx["GEOID10"] = mtx["GEOID10"].astype(str)
    cols = mtx.columns[1:]

    with open(filename_microdata, 'w', newline='') as fw:
        fw.write("County,Tract,BG,Block,HT,VA,E,R,S\n")

        for index, row in mtx.iterrows():
            block_id = row["GEOID10"]
            print(index)
            bg_id, tract_id, county_id = block_id[:12], block_id[:11], block_id[:5]
            for col in cols:
                cnt = int(row[col])
                if cnt != 0:
                    ht, va, e, r, s = int(col[0:2]) + 1, int(col[2:4]) + 1, int(col[4:6]) + 1, int(col[6:8]) + 1, int(col[8:10]) + 1
                    for i in range(cnt): 
                        fw.write(county_id + ',' + tract_id + ',' + bg_id + ',' + block_id + ',' + str(ht) + ',' + str(va) + ',' + str(e) + ',' + str(r) + ',' + str(s) + '\n')

def prepare_pums_franklin(filename_pums_all, filename_pums):
    # filename_pums = 'data/psam_p39.csv'
    data_pums = pd.read_csv(filename_pums_all)
    pums_fra = data_pums[(data_pums["PUMA"] <= 4111) & (data_pums["PUMA"] >= 4101)]
    pums_fra['ST'] = pums_fra['ST'].apply('{:0>2}'.format)
    pums_fra['PUMA'] = pums_fra['PUMA'].apply('{:0>5}'.format)
    pums_fra['PUMAID'] = pums_fra[['ST', 'PUMA']].apply(lambda x: ''.join(x), axis=1)
    col_list = ["ST", "PUMA", "PUMAID", "AGEP", "HISP", "RAC1P", "SEX"]
    pums_fra = pums_fra[col_list]

    # AGEP
    pums_fra.loc[pums_fra["AGEP"] < 18, "AGEP"] = 1
    pums_fra.loc[pums_fra["AGEP"] >= 18, "AGEP"] = 2
    # HISP
    pums_fra.loc[pums_fra["HISP"] == 1, "HISP"] = 1
    pums_fra.loc[pums_fra["HISP"] > 1, "HISP"] = 2
    # RAC1P
    pums_fra.loc[(pums_fra["RAC1P"] >= 3) & (pums_fra["RAC1P"] <= 5), "RAC1P"] = 3
    pums_fra.loc[pums_fra["RAC1P"] >= 6, "RAC1P"] = pums_fra["RAC1P"] - 2

    pums_fra.to_csv(filename_pums, index=False)


def prepare_pums_guernsey(filename_pums_all, filename_pums):
    # filename_pums = 'data/psam_p39.csv'
    data_pums = pd.read_csv(filename_pums_all)
    pums_gue = data_pums[data_pums["PUMA"] == 2900]
    pums_gue['ST'] = pums_gue['ST'].apply('{:0>2}'.format)
    pums_gue['PUMA'] = pums_gue['PUMA'].apply('{:0>5}'.format)
    pums_gue['PUMAID'] = pums_gue[['ST', 'PUMA']].apply(lambda x: ''.join(x), axis=1)

    col_list = ["ST", "PUMA", "PUMAID", "AGEP", "HISP", "RAC1P", "SEX"]
    pums_gue = pums_gue[col_list]

    # AGEP
    pums_gue.loc[pums_gue["AGEP"] < 18, "AGEP"] = 1
    pums_gue.loc[pums_gue["AGEP"] >= 18, "AGEP"] = 2

    # HISP
    pums_gue.loc[pums_gue["HISP"] == 1, "HISP"] = 1
    pums_gue.loc[pums_gue["HISP"] > 1, "HISP"] = 2

    # RAC1P
    pums_gue.loc[(pums_gue["RAC1P"] >= 3) & (pums_gue["RAC1P"] <= 5), "RAC1P"] = 3
    pums_gue.loc[pums_gue["RAC1P"] >= 6, "RAC1P"] = pums_gue["RAC1P"] - 2

    pums_gue.to_csv(filename_pums, index=False)