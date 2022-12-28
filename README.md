# Generating Small Area Synthetic Microdata for Public Use: Towards Accessible and Reproducible Spatial Data Science

This is an implementation of our small area synthetic microdata (SASM) generator on Python3. We formulate an optimization problem to generate SASM by minimizing the difference between published census tables and the SASM. This method only requires a set of census tables that are publicly available in most countries as input to provide effective results.

For the purpose of demonstration, we here show the use of 11 tables from the [2010 United States Census Summary File 1 (SF1)] to generate the SASM for two counties in Ohio, USA. These tables include:
| Table No. | Description |
| ------ | ------ |
| P5 | Population counts broken down by ethnicity by race |
| P8 | Population counts broken down by race |
| P89 | Population counts broken down by race for non-Hispanics |
| P43 | Population counts broken down by sex by age by group quarter types |
| P12A | Population counts broken down by sex by age for Whites |
| P12B | Population counts broken down by sex by age for Black or African Americans |
| P12C | Population counts broken down by sex by age for American Indian or Alaska Natives |
| P12D | Population counts broken down by sex by age for Asians |
| P12E | Population counts broken down by sex by age for Native Hawaiian or other Pacific Islanders |
| P12F | Population counts broken down by sex by age for individuals with some other race alone |
| P12G | Population counts broken down by sex by age for individuals with two or more races |

This repository includes:
- [data.py]: Converting published census tables to a matrix representation
- [model.py]: The optimization problem solved by [Gurobi]
- [val.py]: Internal and external validations using the original census tables and the 5-Year ACS PUMS
- [case.py]: Case studies
