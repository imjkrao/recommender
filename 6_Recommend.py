# -*- coding: utf-8 -*-
"""
Created on Mon May  4 11:58:23 2020

@author: jeevan
"""

#input_path='E:/Thesis/recommender/user_job_profile/'

#print(rows)
def recommend_job(input_path,user_id,flag=0):
        import pandas as pd
        import numpy as np
        from scipy import spatial
        import jk_similarity
        
        #input_path='E:/Thesis/recommender/user_job_profile/'
        df2=pd.read_csv("E:\Thesis\DataSet\Seenjobs\seenJobs_new10_.csv", encoding='unicode_escape')
        #Match a given user_id with all jobs in the database
        def cosine_similarity(arr1,arr2):
                ans=1-spatial.distance.cosine(arr1,arr2)
                
                if(np.isnan(ans)):
                    return 0
                else:
                    return ans
        def Jacardi(arr1,arr2):
            ans=jk_similarity.jk_similarity(arr1,arr2)
            if(np.isnan(ans)):
                    return 0
            else:
                    return ans
            

        
        #Check if user id exists
        df=pd.read_csv(input_path+"domain_user_profile.csv",index_col='Respondent')
        #print(df.columns)
        matches=dict()
        if(flag==0):
            if(user_id in df.index):
                userdomain=df.loc[user_id,:]
                #print(userdomain)
                #If it does, retrieve the user profile from input_path
                df=pd.read_csv(input_path+"languages_profile_user.csv",index_col='Respondent')
                userlanguages=df.loc[user_id,:]

                df=pd.read_csv(input_path+"frameworks_profile_user.csv",index_col='Respondent')
                userframeworks=df.loc[user_id,:]

                df=pd.read_csv(input_path+"platforms_profile_user.csv",index_col='Respondent')
                userplatforms=df.loc[user_id,:]

                df=pd.read_csv(input_path+"databases_profile_user.csv",index_col='Respondent')
                userdatabases=df.loc[user_id,:]

                userdomain=np.asarray(userdomain.fillna(0))
                userlanguages=np.asarray(userlanguages.fillna(0))
                userframeworks=np.asarray(userframeworks.fillna(0))
                userplatforms=np.asarray(userplatforms.fillna(0))
                userdatabases=np.asarray(userdatabases.fillna(0))
                #print(userdomain)
            else:
                print("error! user id not in Dataset")
            #If it doesn't,take user profile as input
        else:
            print("New user!Enter details..")
            name=input("Enter full name")
            skills=input("Enter skills(comma separated). These are programming languages, frameworks,platforms or databases you have experience with").split(",")
            domains=''
            flag=1
            while(1):
                print("Enter domain(s) of interest separated by commas(Names are case sensitive). Should be one of the following:")
                for i in df.columns:
                    print(i,end=",")
                domains=input().split(",")
                for domain in domains:
                    if(domain not in df.columns):
                        flag=0
                        break
                if(flag==1):
                    break
                else:
                    print("Please enter valid domain")
            #domains=list(map(lambda x:x.lower(),domains))
            skills=list(map(lambda x:x.lower(),skills))                

            userdomain=pd.DataFrame(columns=df.columns)
            dictionary=dict()
            for domain in domains:
                dictionary[domain]=1.0
            userdomain=userdomain.append(dictionary,ignore_index=True)


            df=pd.read_csv(input_path+"languages_profile_user.csv",index_col='Respondent')
            userlanguages=pd.DataFrame(columns=df.columns)
            dictionary=dict()
            for skill in skills:
                if(skill in df.columns):
                    dictionary[skill]=1.0
            userlanguages=userlanguages.append(dictionary,ignore_index=True)

            df=pd.read_csv(input_path+"frameworks_profile_user.csv",index_col='Respondent')
            userframeworks=pd.DataFrame(columns=df.columns)
            dictionary=dict()
            for skill in skills:
                if(skill in df.columns):
                    dictionary[skill]=1.0
            userframeworks=userframeworks.append(dictionary,ignore_index=True)

            df=pd.read_csv(input_path+"platforms_profile_user.csv",index_col='Respondent')
            userplatforms=pd.DataFrame(columns=df.columns)                
            dictionary=dict()
            for skill in skills:
                if(skill in df.columns):
                    dictionary[skill]=1.0
            userplatforms=userplatforms.append(dictionary,ignore_index=True)

            df=pd.read_csv(input_path+"databases_profile_user.csv",index_col='Respondent')
            userdatabases=pd.DataFrame(columns=df.columns)               
            dictionary=dict()
            for skill in skills:
                if(skill in df.columns):
                    dictionary[skill]=1.0
            userdatabases=userdatabases.append(dictionary,ignore_index=True)
            #print(userdomain)
            userdomain=np.asarray(userdomain.iloc[0,:].fillna(0))
            userlanguages=np.asarray(userlanguages.iloc[0,:].fillna(0))
            userframeworks=np.asarray(userframeworks.iloc[0,:].fillna(0))
            userplatforms=np.asarray(userplatforms.iloc[0,:].fillna(0))
            userdatabases=np.asarray(userdatabases.iloc[0,:].fillna(0))
        
        print(user_id)
        jobdomain=pd.read_csv(input_path+"domain_job_profile.csv",index_col='Job_Id')
        joblanguages=pd.read_csv(input_path+'languages_profile_job.csv',index_col='Job_Id')
        jobframeworks=pd.read_csv(input_path+'frameworks_profile_job.csv',index_col='Job_Id')
        jobplatforms=pd.read_csv(input_path+'platforms_profile_job.csv',index_col='Job_Id')
        jobdatabases=pd.read_csv(input_path+'databases_profile_job.csv',index_col='Job_Id')
        #print(len(jobdomain.index),len(joblanguages.index))
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
            #Initializing job profiles for later access
            # self.job_domain=domain
            # self.job_language=language
            # self.job_framework=framework
            # self.job_platform=platform
            # self.job_database=database
            
            # self.user_domain=userdomain
            # self.user_language=userlanguages
            # self.user_framework=userframeworks
            # self.user_platform=userplatforms
            # self.user_database=userdatabases
            job_domain=domain
            job_language=language
            job_framework=framework
            job_platform=platform
            job_database=database
            
            user_domain=userdomain
            user_language=userlanguages
            user_framework=userframeworks
            user_platform=userplatforms
            user_database=userdatabases
        matches=sorted(matches.items(),key=lambda x:x[1],reverse=True)
        
        recommendations=matches[:10]
        
        #print("recommendations are")
        #print(recommendations)
        rows=pd.DataFrame(columns=df2.columns)
        title= []
        score= []
        for i in recommendations:
            a=int(i[0])
            row=df2[df2['Job_Id']==a]
            #print(row)
            #rows[count]=np.asarray(row.values.T.tolist()[0])
            rows=rows.append(row)
        return rows,matches

rows,matches=recommend_job('E:/Thesis/recommender/user_job_profile/',7)
print(rows)