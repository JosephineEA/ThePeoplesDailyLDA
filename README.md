# ThePeoplesDailyLDA
This repository shows a natural language processing project on the People's Daily. It consists of the Python part and the Matlab part:

**The Python part** includes a crawler that collects all news reports on the People's Daily on 2020 and some data preprocess codes on such built data set. 

**The Matlab part** will also do some data preprocess on the data set produced by the Python part, then it will build an LDA(Latent Dirichlet Allocation) model to find out their main topics. 

Finally, the research report (AnalysisOnThePeoplesDaily.pdf) is written in Chinese.

The whole project is finished independently by myself. :)

## The Python part
A Pycharm project. All the files and their usages are as follows:

|Name|Description|
|----|----|
|data|Raw data collected by Python crawler|
|stopwords|Chinese stopwords used by Python package "jieba"|
|deep_preprocess.py|Data cleaning after the primary data process|
|main.py|The crawler|
|preprocess.py|Primary data process|
|word_cut.py|Chinese word cutting|
|proc_data.csv|Processed data set|

## The Matlab part
A Matlab project. All the files and their usages are as follows:
|Name|Description|
|----|----|
