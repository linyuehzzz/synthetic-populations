# Generating Small Area Synthetic Microdata for Public Use: Towards Accessible and Reproducible Spatial Data Science

This is an implementation of our small area synthetic microdata (SASM) generator on Python3. We formulate an optimization problem to generate SASM by minimizing the difference between published census tables and the SASM. This method only requires a set of census tables that are publicly available in most countries as input to provide effective results.

For the purpose of demonstration, we here show the use of tables from the [2010 United States Census Summary File 1 (SF1)] to generate the SASM for Franklin and Guernsey Counties, Ohio, USA. The SASM include 1,163,414 individuals in 22,826 census blocks of Franklin County, and 40,087 individuals in 3,768 census blocks of Guernsey County. Each individual in the SASM has five attributes: housing type, voting age, ethnicity, race, and sex. The SASM and metadata can be found at:
- [Franklin]
- [Guernsey]
- [Codebook]

## Details
This repository includes:
- [`data.py`]: Convert published census tables to a matrix
- [`model.py`]: Optimization with [Gurobi Optimizer]
- [`val.py`]: Internal and external validations
- [`case.py`]: Case studies

## Getting Started
1. We use [Gurobi Optimizer] as our optimization solver in this implementation. Gurobi provides free, unlimited-use acedemic licenses at <https://www.gurobi.com/features/academic-named-user-license/>. Please follow the instructions to install a Gurobi Optimizer license on your device.
2. Clone repo and install [`requirements.txt`] in a Python>=3.8.0 environment.
```
git clone https://github.com/linyuehzzz/synthetic-populations.git
cd synthetic-populations
pip install -r requirements.txt
```
3. Reproduce results for Franklin and Guernsey.
```
python franklin.py
python guernsey.py
```

## Citation
```
@article{lin2022developing,
  title={Developing synthetic individual-level population datasets: The case of contextualizing maps of privacy-preserving census data},
  author={Lin, Yue and Xiao, Ningchuan},
  journal={arXiv preprint arXiv:2206.04766},
  year={2022}
}
```

[//]: # 
   [Gurobi Optimizer]: <https://www.gurobi.com/>
   [2010 United States Census Summary File 1 (SF1)]: <https://www.census.gov/data/datasets/2010/dec/summary-file-1.html>
   
   [`data.py`]: <https://github.com/linyuehzzz/synthetic-populations/blob/main/lib/data.py>
   [`model.py`]: <https://github.com/linyuehzzz/synthetic-populations/blob/main/lib/model.py>
   [`val.py`]: <https://github.com/linyuehzzz/synthetic-populations/blob/main/lib/val.py>
   [`case.py`]: <https://github.com/linyuehzzz/synthetic-populations/blob/main/lib/case.py>
   [`requirements.txt`]: <https://github.com/linyuehzzz/synthetic-populations/blob/main/requirements.txt>
   [Franklin]: <https://github.com/linyuehzzz/synthetic-populations/blob/main/data/franklin_microdata.csv>
   [Guernsey]: <https://github.com/linyuehzzz/synthetic-populations/blob/main/data/guernsey_microdata.csv>
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
