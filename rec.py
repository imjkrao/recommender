# -*- coding: utf-8 -*-
"""
Created on Tue May  5 13:37:44 2020

@author: jeevan
"""

def recommend_job(input_path,user_id,flag=0):
    import pandas as pd
    import numpy as np
    from scipy import spatial
    global rows,userdomain,userlanguages,userframeworks,userplatforms,userdatabases
    #input_path='E:/Thesis/recommender/user_job_profile/'
    df2=pd.read_csv("E:\Thesis\DataSet\Seenjobs\seenJobs_new10_.csv", encoding='unicode_escape')
    #Match a given user_id with all jobs in the database
    def cosine_similarity(arr1,arr2):
            ans=1- spatial.distance.cosine(arr1,arr2)
            if(np.isnan(ans)):
                return 0
            else:
                return ans
    def Jacardi(arr1,arr2):
        ans=1-spatial.distance.jaccard(arr1,arr2)
        if(np.isnan(ans)):
            return 0
        else:
            return ans

    
    #Check if user id exists
    df=pd.read_csv(input_path+"domain_user_profile.csv",index_col='Respondent')
    #print(df.columns)
    matches=dict()
    #user_id=5
    rows=pd.DataFrame(columns=df2.columns)
    userdomain=userlanguages=userframeworks=userplatforms=userdatabases=[]
    # if(user_id in df.index):
    c=int(user_id)
    userdomain=df.loc[c,:]
    #print(userdomain)
    #If it does, retrieve the user profile from input_path
    df=pd.read_csv(input_path+"languages_profile_user.csv",index_col='Respondent')
    userlanguages=df.loc[c,:]

    df=pd.read_csv(input_path+"frameworks_profile_user.csv",index_col='Respondent')
    userframeworks=df.loc[c,:]

    df=pd.read_csv(input_path+"platforms_profile_user.csv",index_col='Respondent')
    userplatforms=df.loc[c,:]

    df=pd.read_csv(input_path+"databases_profile_user.csv",index_col='Respondent')
    userdatabases=df.loc[c,:]

    userdomain=np.asarray(userdomain.fillna(0))
    userlanguages=np.asarray(userlanguages.fillna(0))
    userframeworks=np.asarray(userframeworks.fillna(0))
    userplatforms=np.asarray(userplatforms.fillna(0))
    userdatabases=np.asarray(userdatabases.fillna(0))
    #print(userdomain)        
    print(c)
    print(userdomain)
    jobdomain=pd.read_csv(input_path+"domain_job_profile.csv",index_col='Job_Id')
    joblanguages=pd.read_csv(input_path+'languages_profile_job.csv',index_col='Job_Id')
    jobframeworks=pd.read_csv(input_path+'frameworks_profile_job.csv',index_col='Job_Id')
    jobplatforms=pd.read_csv(input_path+'platforms_profile_job.csv',index_col='Job_Id')
    jobdatabases=pd.read_csv(input_path+'databases_profile_job.csv',index_col='Job_Id')
    print(len(jobdomain.index),len(joblanguages.index))
    for i in jobdomain.index:
        #print(i)
        domain=jobdomain.loc[i,:].fillna(0)
        language=joblanguages.loc[i,:].fillna(0)
        framework=jobframeworks.loc[i,:].fillna(0)
        platform=jobplatforms.loc[i,:].fillna(0)
        database=jobdatabases.loc[i,:].fillna(0)
        job_id=str(i)
        domain=np.asarray(domain)
        language=np.asarray(language)
        framework=np.asarray(framework)
        platform=np.asarray(platform)
        database=np.asarray(database)
        #print(len(domain),len(userdomain))
        score=(0.4*cosine_similarity(domain,userdomain))+(0.6*(cosine_similarity(language,userlanguages)+cosine_similarity(framework,userframeworks)+cosine_similarity(platform,userplatforms)+cosine_similarity(database,userdatabases)))
        #score=(0.4*Jacardi(domain,userdomain))+(0.6*(Jacardi(language,userlanguages)+Jacardi(framework,userframeworks)+Jacardi(platform,userplatforms)+Jacardi(database,userdatabases)))
        matches[job_id]=score
        #score=(0.7*cosine_similarity(domain,userdomain))+(0.3*(cosine_similarity(language,userlanguages)+cosine_similarity(framework,userframeworks)+cosine_similarity(platform,userplatforms)+cosine_similarity(database,userdatabases)))
    matches=sorted(matches.items(),key=lambda x:x[1],reverse=True)

    recommendations=matches[:10]
    #print("recommendations are")
    #print(recommendations)
    row=pd.DataFrame(columns=df2.columns)
    title= []
    score= []
    for i in recommendations:
        a=int(i[0])
        row=df2[df2['Job_Id']==a]
        print(row)
        #rows[count]=np.asarray(row.values.T.tolist()[0])
        rows=rows.append(row)
    return rows