# -*- coding: utf-8 -*-
"""
Created on Mon May  1 11:27:20 2020

@author: jeevan
"""
import pandas as pd

#Input is user data and Job data dataframes    
job_profile_path='E:/Thesis/recommender/job_profile/'
user_profile_path='E:/Thesis/recommender/respodent_profile/'
output_path='E:/Thesis/recommender/user_job_profile/'
def create_common_profile(job_profile_path,user_profile_path,output_path,flag=0):
        if(flag==0):
            #Domain
            userprofile=pd.read_csv(user_profile_path+"DevType.csv",index_col='Respondent')
            jobprofile=pd.read_csv(job_profile_path+"domain_job_profile.csv",index_col='Job_Id')
            print("Read from file")
            print(jobprofile.index)
            #jobprofile=jobprofile.reset_index()
            #userprofile=userprofile.reset_index()
            userprofile.drop('Unnamed: 0', axis=1, inplace=True)
            
            print(jobprofile.index)
            #print(jobprofile.loc[:,'Job_Id'])
            userprofile.rename(columns={'Product manager':'Product Manager','Back-end developer':'Back End','C-suite executive (CEO, CTO, etc.)':'C-suite executive','Data scientist or machine learning specialist':'Data Scientist','Database administrator':'Database Administrator(DBA)','Mobile developer':'Mobile Developer','Desktop or enterprise applications developer':'Enterprise application','DevOps specialist':'DevOps','Front-end developer':'Front End','Full-stack developer':'Full stack','Marketing or sales professional':'Sales professional','QA or test developer':'QA/Test Developer','System administrator':'System Administrator','Game or graphics developer':'Game developer'},inplace=True)
            jobprofile.rename(columns={'Business analyst':'Data or business analyst'},inplace=True)
            print(userprofile.columns)
            print(jobprofile.columns)
            #Present in userprofile but not in jobprofile
            a=list(set(userprofile.columns)-set(jobprofile.columns))
            print(a)
            for i in a:
                if(i!='Respondent'):
                    jobprofile[i]=0
            b=list(set(jobprofile.columns)-set(userprofile.columns))
            print(b)
            for i in b:
                if(i!='Job_Id'):
                    userprofile[i]=0
            #userprofile=userprofile.set_index('Respondent')
            #jobprofile=jobprofile.set_index('Job_Id')
            userprofile=userprofile[sorted(userprofile.columns.tolist())]
            jobprofile=jobprofile[sorted(jobprofile.columns.tolist())]
            #Exclude 

            print(userprofile.columns==jobprofile.columns)

            print(userprofile.columns)
            print(jobprofile.columns)
            userprofile=userprofile[userprofile.columns.tolist()]
            jobprofile=jobprofile[jobprofile.columns.tolist()]
            userprofile.to_csv(output_path+"domain_user_profile.csv")
            jobprofile.to_csv(output_path+"domain_job_profile.csv")

            #Languages
            df_user=pd.read_csv(user_profile_path+"LanguageWorkedWith.csv",index_col='Respondent')
            df_job=pd.read_csv(job_profile_path+"languages_job_profile.csv",index_col='Job_Id')
        
            print(df_job.index)
            print(df_user.index)
            print(df_user.columns)
            print(df_job.columns)
            df_user.drop('Unnamed: 0', axis=1, inplace=True)
            #df_job.drop('Unnamed: 0', axis=1, inplace=True)
            #df_job.rename(columns={'visual basic .net':'vb.net'},inplace=True)
            df_user.columns=list(map(lambda x:x.lower(),df_user.columns))
            df_job.columns=list(map(lambda x:x.lower(),df_job.columns))
            #columns_to_add=[]
            a=list(set(df_user.columns)-(set(df_job.columns)))
            print(a)
            for i in a:
                if(i!='Respondent'):
                    df_job[i]=0        
            b=list(set(df_job.columns)-set(df_user.columns))
            print(b)
            for i in b:
                if(i!='Job_Id'):
                    df_user[i]=0
            print(df_job.index)        
            df_user=df_user[sorted(df_user.columns.tolist())]
            df_job=df_job[sorted(df_job.columns.tolist())]
            #df_user,df_job=self.clean_common_profile(df_user,df_job,'Language')
            #print(df_job.loc[df_job.index[0],:])
            df_user.to_csv(output_path+"languages_profile_user.csv")
            df_job.to_csv(output_path+"languages_profile_job.csv")

            #Frameworks
            df_user=pd.read_csv(user_profile_path+"WebFrameWorkedWith.csv",index_col='Respondent')
            df_job=pd.read_csv(job_profile_path+"frameworks_job_profile.csv",index_col='Job_Id') 
            #df_job.index.name='Job_Id'
            print(df_user.columns)
            print(df_job.columns)
            df_user.drop('Unnamed: 0', axis=1, inplace=True)
            #df_job.drop('Unnamed: 0', axis=1, inplace=True)
            #df_job.rename(columns={'visual basic .net':'vb.net'},inplace=True)
            df_user.columns=list(map(lambda x:x.lower(),df_user.columns))
            df_job.columns=list(map(lambda x:x.lower(),df_job.columns))

            a=list(set(df_user.columns)-(set(df_job.columns)))
            print(a)
            for i in a:
                if(i!='Respondent'):
                    df_job[i]=0        
            b=list(set(df_job.columns)-set(df_user.columns))
            print(b)
            for i in b:
                if(i!='Job_Id'):
                    df_user[i]=0
            #userprofile=userprofile.reindex_axis(sorted(userprofile.columns), axis=1)
            #jobprofile=jobprofile.reindex_axis(sorted(jobprofile.columns), axis=1)
            df_user=df_user[sorted(df_user.columns.tolist())]
            df_job=df_job[sorted(df_job.columns.tolist())]

            print(len(set(df_user.columns).intersection(df_job.columns)),len(df_user.columns))
            #df_user,df_job=self.clean_common_profile(df_user,df_job,'Framework')   
            df_user.to_csv(output_path+"frameworks_profile_user.csv")
            df_job.to_csv(output_path+"frameworks_profile_job.csv")

            #Platforms
            df_user=pd.read_csv(user_profile_path+"PlatformWorkedWith.csv",index_col='Respondent')
            df_job=pd.read_csv(job_profile_path+"platforms_job_profile.csv",index_col='Job_Id') 
            print(df_user.columns)
            print(df_job.columns)
            df_user.drop('Unnamed: 0', axis=1, inplace=True)
            #df_job.drop('Unnamed: 0', axis=1, inplace=True)
            #df_job.rename(columns={'visual basic .net':'vb.net'},inplace=True)
            df_user.columns=list(map(lambda x:x.lower(),df_user.columns))
            df_job.columns=list(map(lambda x:x.lower(),df_job.columns))

            a=list(set(df_user.columns)-(set(df_job.columns)))
            print(a)
            for i in a:
                if(i!='Respondent'):
                    df_job[i]=0
            b=list(set(df_job.columns)-set(df_user.columns))
            print(b)
            for i in b:
                if(i!='Job_Id'):
                    df_user[i]=0
            df_user=df_user[sorted(df_user.columns.tolist())]
            df_job=df_job[sorted(df_job.columns.tolist())]

            print(len(set(df_user.columns).intersection(df_job.columns)),len(df_user.columns))
            #df_user,df_job=self.clean_common_profile(df_user,df_job,'Platform')        
            df_user.to_csv(output_path+"platforms_profile_user.csv")
            df_job.to_csv(output_path+"platforms_profile_job.csv")

            #Databases
            df_user=pd.read_csv(user_profile_path+"DatabaseWorkedWith.csv",index_col='Respondent')
            df_job=pd.read_csv(job_profile_path+"databases_job_profile.csv",index_col='Job_Id') 
            
            print(df_user.columns)
            print(df_job.columns)
            #df_user.drop('Unnamed: 0', axis=1, inplace=True)
            #df_job.drop('Unnamed: 0', axis=1, inplace=True)
            #df_job.rename(columns={'visual basic .net':'vb.net'},inplace=True)
            df_user.columns=list(map(lambda x:x.lower(),df_user.columns))
            df_job.columns=list(map(lambda x:x.lower(),df_job.columns))

            a=list(set(df_user.columns)-(set(df_job.columns)))
            print(a)
            for i in a:
                if(i!='Respondent'):
                    df_job[i]=0
            b=list(set(df_job.columns)-set(df_user.columns))
            print(b)
            for i in b:
                if(i!='Job_Id'):
                    df_user[i]=0
            df_user=df_user[sorted(df_user.columns.tolist())]
            df_job=df_job[sorted(df_job.columns.tolist())]

            print(len(set(df_user.columns).intersection(df_job.columns)),len(df_user.columns))
            #df_user,df_job=self.clean_common_profile(df_user,df_job,'Database')        
            df_user.to_csv(output_path+"databases_profile_user.csv")
            df_job.to_csv(output_path+"databases_profile_job.csv")
