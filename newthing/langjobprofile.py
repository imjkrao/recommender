# -*- coding: utf-8 -*-
"""
Created on Fri May  1 00:02:21 2020

@author: jeevan
"""
df_languages=pd.read_csv("E:\Thesis\DataSet\Seenjobs\language_job.csv")

langlist=[i.lower() for i in langlist]

Languagejob = pd.DataFrame(df_languages['Job_Id'])
for i in langlist:
    
    Languagejob[i]=""
time_start=time.time()
Languagejob_columns=Languagejob.columns
coldic=dict(zip(Languagejob.columns,range(0,len(languageWW)+1)))
print(coldic)
print(df1.head())
time_start=time.time()
for i in range(615):
    data=(df_languages.loc[i,'skills']).split(',')
    if(data[0]!=""):
       # print(data)
        for value in data:
            try:
                Languagejob.iloc[i,coldic[value]]=1
            except KeyError:
                print(i)

Languagejob.to_csv("langjob.csv")
time_end=time.time()
print(time_end-time_start)

languageWW.lower