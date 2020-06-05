# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 18:11:31 2020

@author: jeevan
"""

import pandas as pd
import spacy
import en_core_web_lg
import numpy as np
link="E:\Thesis\DataSet\Seenjobs\seenJobs_new10_.csv"

df2=pd.read_csv(link, encoding='unicode_escape')
training_range=int(len(df2.loc[:,'Job_Id']))

def categorize_jobs(df2,training_range):
        def check_threshold(threshold,ele):
            if(ele[0]!=threshold[0][0] and abs(ele[1]-threshold[0][1])<0.03):
                return True
            else:
                return False
        #Compare similarities of word embeddings using Word2vec and cosine similarity
        nlp=en_core_web_lg.load()
        job_id=df2.loc[:,'Job_Id'].tolist()[:training_range]
        job_titles=df2.loc[:,'jobtitle'].tolist()[:training_range]
        job_descriptions=df2.loc[:,'jobdescription'].tolist()[:training_range]
        final_cat=pd.DataFrame(index=job_id)
        #similarity between Predefined Categories and job_id,job_titles,job_descriptions
        categories=['Network Engineer','Full stack','QA/Test Developer','Enterprise application','DevOps','Mobile Developer','Back End','Database Administrator(DBA)','Front End','Game developer','System Administrator','Data Scientist','Business analyst','Sales professional','Product Manager','Information Security','Software Developer/Java Developer','Web Developer','Cloud Computing']
        for category in categories:
            final_cat[category]=np.nan
        for job_t_d in list(zip(job_id,job_titles,job_descriptions)):
            id_job=job_t_d[0]
            job_i=job_t_d[1]
            job_d=job_t_d[2]
            job_title=nlp(job_i.lower())
            job_description=nlp(job_d.lower())
            match_cat_title=dict()
            match_cat_description=dict()
            for category in categories:
                word=nlp(category.lower())
                match_cat_title[category]=job_title.similarity(word)
                match_cat_description[category]=job_description.similarity(word)
            match_cat_title=sorted(match_cat_title.items(),key=lambda x:x[1],reverse=True)
            match_cat_description=sorted(match_cat_description.items(),key=lambda x:x[1],reverse=True)


            #a represents max
            #if(match_cat_title[0][1]>0.5 or match_cat_description[0][1]>0.5):
            a=match_cat_title[0]
            #print(a)
            match_cat_description=list(filter(lambda x: check_threshold(match_cat_title,x),match_cat_description))
            if(len(match_cat_description)!=0):
                print(match_cat_description)
                print(id_job)
                #b=match_cat_description[0]
                final_cat.loc[id_job,a[0]]=1
                match_cat_description.extend([(match_cat_title[0][0],1)])
                sum_proportion=sum([x[1] for x in match_cat_description])
                for ele in match_cat_description:
                    final_cat.loc[id_job,ele[0]]=ele[1]/sum_proportion
            else:
                print(id_job)
                final_cat.loc[id_job,a[0]]=1
        return final_cat

