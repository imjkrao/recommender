# -*- coding: utf-8 -*-
"""
Created on Fri May  1 01:50:10 2020

@author: jeevan
"""
import pandas as pd
import numpy as np

extracted_skills_df=extracted_skills_df_withoutjd
domain_df=pd.read_csv("E:/Thesis/recommender/finalCategory_jobprofile.csv")
def create_job_profile(extracted_skills_df,domain_df):
        job_id=extracted_skills_df.index.tolist()
        languages_df=pd.DataFrame(index=job_id)
        platforms_df=pd.DataFrame(index=job_id)
        frameworks_df=pd.DataFrame(index=job_id)
        databases_df=pd.DataFrame(index=job_id)
        
        for job,lang,frame,plat,datab in list(zip(job_id,extracted_skills_df.loc[:,'Language'].tolist(),extracted_skills_df.loc[:,'Framework'].tolist(),extracted_skills_df.loc[:,'Platform'].tolist(),extracted_skills_df.loc[:,'Database'].tolist())):
            #Languages
            l=lang.split(",")
            if(lang!=np.nan or lang!=''):
                for ele in l:
                    if(ele==''):
                        continue
                    if(ele not in languages_df.columns):
                        #languages.append(ele)
                        languages_df[ele]=np.nan
                    languages_df.loc[job,ele]=1
            
            #Frameworks
            l=frame.split(",")
            if(frame!=np.nan or frame!=''):
                for ele in l:
                    if(ele==''):
                        continue
                    if(ele not in frameworks_df.columns):
                        #languages.append(ele)
                        frameworks_df[ele]=np.nan
                    frameworks_df.loc[job,ele]=1

            #Platforms
            l=plat.split(",")
            if(plat!=np.nan or plat!=''):
                for ele in l:
                    if(ele==''):
                        continue
                    if(ele not in platforms_df.columns):
                        #languages.append(ele)
                        platforms_df[ele]=np.nan
                    platforms_df.loc[job,ele]=1
            
            #Databases
            l=datab.split(",")
            if(datab!=np.nan or datab!=''):
                for ele in l:
                    if(ele==''):
                        continue
                    if(ele not in databases_df.columns):
                        #languages.append(ele)
                        databases_df[ele]=np.nan
                    databases_df.loc[job,ele]=1
        languages_df=languages_df.reindex(sorted(languages_df.columns), axis=1)
        frameworks_df=frameworks_df.reindex(sorted(frameworks_df.columns), axis=1)
        platforms_df=platforms_df.reindex(sorted(platforms_df.columns), axis=1)
        databases_df=databases_df.reindex(sorted(databases_df.columns), axis=1)
        domain_df=domain_df.set_index(domain_df.iloc[:,0])
        domain_df.drop(domain_df.columns[[0]],axis = 1, inplace = True)
        domain_df=domain_df.reindex(sorted(domain_df.columns),axis=1)
        
        languages_df.index.name=frameworks_df.index.name=platforms_df.index.name=databases_df.index.name=domain_df.index.name='Job_Id'
        languages_df.to_csv("E:/Thesis/recommender/job_profile/languages_job_profile.csv")
        frameworks_df.to_csv("E:/Thesis/recommender/job_profile/frameworks_job_profile.csv")
        platforms_df.to_csv("E:/Thesis/recommender/job_profile/platforms_job_profile.csv")
        databases_df.to_csv("E:/Thesis/recommender/job_profile/databases_job_profile.csv")
        domain_df.to_csv("E:/Thesis/recommender/job_profile/domain_job_profile.csv")
        print(languages_df.columns)