# Synthetic Population Data for Small Area Estimation in the United States

This repository contains the reproducible code of a synthetic data generator. We release synthetic population data for all 308,745,538 individual in 220,334 block groups in the United States. Each individual has five socio-demographic characteristics of housing type, age, sex, race, and Hispanic or Latino origin. The synthetic data can be found on Figshare at <https://doi.org/10.6084/m9.figshare.22056893>. We here show how the data is generated, validated, and used.

## Details
This repository includes the following files:
- [`data.ipynb`]: Synthetic data generation
- [`validation.ipynb`]: Data validation

## Getting Started
1. We use [Gurobi Optimizer] as our optimization solver in this implementation. Gurobi provides free, unlimited-use acedemic licenses at <https://www.gurobi.com/features/academic-named-user-license/>. Please follow the instructions to install a Gurobi Optimizer license on your device.
2. Clone repo and install [`requirements.txt`] in a Python>=3.8.0 environment.
```
git clone https://github.com/linyuehzzz/synthetic-populations.git
cd synthetic-populations/usa
pip install -r requirements.txt
```
3. Download input data for modeling and validation at <http://bit.ly/3lEybku>. Organize the files as shown below.
```
├── usa
│   ├── data
│   │   ├── nhgis0003_ds172_2010_blck_grp.csv
│   │   ├── state_fips.txt
│   │   ├── usa_pums.csv
│   │   ├── US_blck_grp_2010_puma.csv
│   │   ├── demo_data
│   │   │   ├── OH_microdata.csv
│   │   │   ├── tl_2010_39_bg10.shp
│   │   │   ├── ...
│   │   │   ├── WA_microdata.csv
│   │   │   ├── tl_2010_53_bg10.shp
│   │   │   ├── ...
│   │   ├── microdata_by_state
│   │   │   ├── ...
│   ├── data.ipynb
│   ├── validation.ipynb
│   ├── demo.ipynb
│   ├── requirements.txt
```


[//]: # 
   [Gurobi Optimizer]: <https://www.gurobi.com/>
   [`data.ipynb`]: <https://github.com/linyuehzzz/synthetic-populations/blob/main/usa/data.ipynb>
   [`validation.ipynb`]: <https://github.com/linyuehzzz/synthetic-populations/blob/main/usa/validation.ipynb>
   [`demo.ipynb`]: <https://github.com/linyuehzzz/synthetic-populations/blob/main/usa/demo.ipynb>
   [`requirements.txt`]: <https://github.com/linyuehzzz/synthetic-populations/blob/main/requirements.txt>
   

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
