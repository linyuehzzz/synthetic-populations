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


3. Reproduce results for Franklin and Guernsey.
```
python franklin.py
python guernsey.py
```

[//]: # 
   [Gurobi Optimizer]: <https://www.gurobi.com/>
   [2010 United States Census Summary File 1 (SF1)]: <https://www.census.gov/data/datasets/2010/dec/summary-file-1.html>
   
   [`data.ipynb`]: <https://github.com/linyuehzzz/synthetic-populations/blob/main/usa/data.ipynb>
   [`validation.ipynb`]: <https://github.com/linyuehzzz/synthetic-populations/blob/main/usa/validation.ipynb>
   [`requirements.txt`]: <https://github.com/linyuehzzz/synthetic-populations/blob/main/requirements.txt>
   [Codebook]: <https://github.com/linyuehzzz/synthetic-populations/blob/main/data/codebook.txt>
   
   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
