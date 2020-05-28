# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 19:24:31 2020

@author: jeevan
"""
import numpy as np
import nltk
from nltk.corpus import stopwords
import pandas as pd
#from spacy import stopwords
import re
#clean column skills in job dataset by removing symbols and stopwords
def clean_skills(df2,training_range):
        extracted_skills=dict()
        job_skills=np.asarray(df2.loc[:,"skills"])
        for i in range(training_range):
            #print(i)
            job_id=df2.iloc[i,0]
            tokenizer=nltk.tokenize.RegexpTokenizer(r'\w+')
            #print(job_skills[i])
            #skip to next iteration if skill is null 
            if(pd.isnull(job_skills[i])):
                continue
            stopwords_list=stopwords.words("english")
            tokens=re.split("|".join([","," and","/"," AND"," or"," OR",";"]),job_skills[i])
            tokens=list(set(tokens))
            extracted_skills[job_id]=[]
            extracted_skills[job_id].extend(tokens)
        return extracted_skills


#dirty work 
LanguageWorkedWith=list()
for value in df1["LanguageWorkedWith"]:
        new=value.split(';')
        for i in new:
            LanguageWorkedWith.append(i)
languageWW=set(LanguageWorkedWith)

#LanguageWorkedWith languageWW
Language_job = pd.DataFrame(df2['Job_Id'])
for i in languageWW:
    
    Language_job[i]=""
time_start=time.time()
coldic=dict(zip(Language_job.columns,range(0,len(languageWW)+1)))
print(coldic)
print(df1.head())
for i in range(615):
    data=(df2.loc[i,'skills']).split(',')
    if(data[0]!=""):
       # print(data)
        for value in data:
            Language_job.iloc[i,coldic[value]]=1
time_end=time.time()
print(time_end-time_start)
