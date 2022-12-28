import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

def case1(filename_mtx, filename_gdf, filename_case1_census, filename_case1_sasm, n1, n2, n3, n4, n5):
    # prepare data
    mtx = pd.read_csv(filename_mtx)
    mtx2 = mtx.copy()
    column_names = mtx2.columns[1:]

    for k2 in range(n2): # voting age
        k2 = '{number:0{width}d}'.format(width=2, number=k2)
        for k3 in range(n3): # ethnicity
            k3 = '{number:0{width}d}'.format(width=2, number=k3)
            for k4 in range(n4): # race
                k4 = '{number:0{width}d}'.format(width=2, number=k4)
                # for k5 in range(n5): # sex
                #     k5 = '{number:0{width}d}'.format(width=2, number=k5)
                col_names = [col for col in column_names if k2 in col[2:4] and k3 in col[4:6] and k4 in col[6:8]]
                mtx2[k2 + k3 + k4] = mtx2[col_names].sum(axis=1)

    mtx2.drop([col for col in mtx2.columns if len(col)==10], axis=1, inplace=True)
    mtx2['GEOID10'] = mtx2['GEOID10'].astype(str)
    mtx2['TOTAL'] = mtx2[mtx2.columns[1:]].sum(axis=1)

    gdf = gpd.read_file(filename_gdf)

    # census tables: non-Hispanics Black
    merged = gdf.set_index('GEOID10').join(mtx2.set_index('GEOID10'))
    merged["PLOT"] = (merged["010100"] + merged["000100"]) / merged['TOTAL'] *100
    fig = merged.plot(column='PLOT', legend=True, cmap='Blues', scheme='userdefined', classification_kwds={'bins':[-5, 0, 5, 10, 50, 100]})
    fig.set_axis_off()
    plt.savefig(filename_case1_census, format='eps')

    # SASM: voting age, non-Hispanics Black 
    merged = gdf.set_index('GEOID10').join(mtx2.set_index('GEOID10'))
    merged["PLOT"] = merged["010100"] / merged['TOTAL'] *100
    fig = merged.plot(column='PLOT', legend=True, cmap='Blues', scheme='userdefined', classification_kwds={'bins':[-5, 0, 5, 10, 50, 100]})
    fig.set_axis_off()
    plt.savefig(filename_case1_sasm, format='eps')


def case2(filename_mtx, filename_mtx_dp, filename_gdf, filename_case2_sasm, filename_case2_dpsasm, filename_case2_pe):

    # DP-SASM
    mtx_dp = pd.read_csv(filename_mtx_dp)
    mtx_dp["TRACT"] = mtx_dp["TRACT"].astype(str)

    x = '{number:0{width}d}'.format(width=2, number=1)
    col_names = [col for col in mtx_dp.columns if x in col[6:8]]
    mtx_dp["new_dp"] = mtx_dp[col_names].sum(axis=1)
    mtx_dp["sum_dp"] = mtx_dp[mtx_dp.columns[1:]].sum(axis=1)
    mtx_dp["new_dp"] = mtx_dp["new_dp"] / mtx_dp["sum_dp"] * 100

    gdf = gpd.read_file(filename_gdf)
    gdf = gdf.set_index('GEOID10').join(mtx_dp.set_index('TRACT'))

    fig = gdf.plot(column='new_dp', legend=True, cmap='Blues')
    fig.set_axis_off()
    fig.get_figure().savefig(filename_case2_dpsasm)

    # SASM
    mtx = pd.read_csv(filename_mtx)
    mtx['TRACT'] = mtx['GEOID10'].astype(str).str[:11]
    col_names = mtx.columns.to_numpy()
    col_names = np.delete(col_names, [0, -1])
    mtx = mtx.groupby('TRACT').sum()[col_names]
    mtx = mtx.reset_index()

    x = '{number:0{width}d}'.format(width=2, number=1)
    col_names = [col for col in mtx.columns if x in col[6:8]]
    mtx["new_ori"] = mtx[col_names].sum(axis=1)
    mtx["sum_ori"] = mtx[mtx.columns[1:]].sum(axis=1)
    mtx["new_ori"] = mtx["new_ori"] / mtx["sum_ori"] * 100

    gdf = gdf.join(mtx.set_index('TRACT'))
    fig = gdf.plot(column='new_ori', legend=True, cmap='Blues')
    fig.set_axis_off()
    fig.get_figure().savefig(filename_case2_sasm)

    # percent error
    gdf["diff"] = abs(gdf["new_ori"] - gdf["new_dp"]) / (gdf["new_ori"] + gdf["new_dp"]) * 100
    fig = gdf.plot(column='diff', legend=True, cmap='Oranges')
    fig.set_axis_off()
    fig.get_figure().savefig(filename_case2_pe)