import lib.data
import lib.model
import lib.val
import lib.case

filename_p1 = 'data/guernsey/guernsey_P1.csv'
filename_p5 = 'data/guernsey/guernsey_P5.csv'
filename_p8 = 'data/guernsey/guernsey_P8.csv' 
filename_p9 = 'data/guernsey/guernsey_P9.csv'
filename_p12A = 'data/guernsey/guernsey_P12A.csv'
filename_p12B = 'data/guernsey/guernsey_P12B.csv'
filename_p12C = 'data/guernsey/guernsey_P12C.csv'
filename_p12D = 'data/guernsey/guernsey_P12D.csv'
filename_p12E = 'data/guernsey/guernsey_P12E.csv'
filename_p12F = 'data/guernsey/guernsey_P12F.csv'
filename_p12G = 'data/guernsey/guernsey_P12G.csv'
filename_p43 = 'data/guernsey/guernsey_P43.csv'
filename_cons = "data/guernsey/guernsey_cons.csv"
filename_obj = 'data/guernsey/guernsey_mtx_obj.csv'
filename_mtx = 'data/guernsey/guernsey_mtx.csv'
filename_microdata = 'data/guernsey_microdata.csv'
filename_pums = 'data/guernsey/guernsey_pums10.csv'
filename_gdf_block = 'data/guernsey/tl_2010_39059_tabblock10.shp'
filename_mtx_dp = 'data/guernsey/guernsey_tract10_dp.csv'
filename_gdf_tract = 'data/guernsey/tl_2010_39059_tract10.shp'

filename_ext_val = 'figs/guernsey_ext_val.svg'
filename_case1_census = 'figs/guernsey_case1_census.eps'
filename_case1_sasm = 'figs/guernsey_case1_sasm.eps'
filename_case2_dpsasm = 'figs/guernsey_case2_dpsasm.eps'
filename_case2_sasm = 'figs/guernsey_case2_sasm.eps'
filename_case2_pe = 'figs/guernsey_case2_pe.eps'

n1, n2, n3, n4, n5 = 8, 2, 2, 63, 2
N = n1 * n2 * n3 * n4 * n5         # number of attribute combinations: HHGQ (8) ∗ VOTINGAGE (2) ∗ HISPANIC (2) ∗ RACE (63) ∗ SEX (2)

lib.data.prepare_sf1(filename_p1, filename_p5, filename_p8, filename_p9, filename_p12A, filename_p12B, filename_p12C, filename_p12D, filename_p12E, filename_p12F, filename_p12G, filename_p43, filename_cons)

lib.model.optimize(filename_cons, filename_obj, filename_mtx)
lib.data.convert_mtx_to_microdata(filename_mtx, filename_microdata)

lib.val.int_val(filename_mtx, n1, n2, n3, n4, n5)
lib.val.ext_val(filename_pums, filename_mtx, filename_ext_val, n1, n2, n3, n4, n5)

lib.case.case1(filename_mtx, filename_gdf_block, filename_case1_census, filename_case1_sasm, n1, n2, n3, n4, n5)
lib.case.case2(filename_mtx, filename_mtx_dp, filename_gdf_tract, filename_case2_sasm, filename_case2_dpsasm, filename_case2_pe)