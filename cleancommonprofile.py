# -*- coding: utf-8 -*-
"""
Created on Fri May  1 17:49:06 2020

@author: jeevan
"""

def clean_common_profile(df_user,df_job,flag):
        #Shift .net from languages to frameworks
        if(flag=='Language'):
            print(df_job.columns.tolist())
            #bash and bash/shell
            count=0
            for ele in df_user.loc[:,'bash/shell']:
                if(ele==1.0):
                    df_user.ix[count,'bash']=1.0
                count=count+1
            df_user=df_user.drop('bash/shell',axis=1)
            count=0
            for ele in df_job.loc[:,'bash/shell']:
                if(ele==1.0):
                    df_job.ix[count,'bash']=1.0
                count=count+1
            df_job=df_job.drop('bash/shell',axis=1)

        if(flag=='Framework'):
            print(df_user.columns.tolist())
            count=0
            for ele in df_user.loc[:,'nodejs']:
                if(ele==1.0):
                    df_user.ix[count,'node.js']=1.0
                count=count+1
            df_user=df_user.drop('nodejs',axis=1)
            count=0
            for ele in df_job.loc[:,'nodejs']:
                if(ele==1.0):
                    df_job.ix[count,'node.js']=1.0
                count=count+1
            df_job=df_job.drop('nodejs',axis=1)
            
            count=0
            for ele in df_user.loc[:,'angularjs']:
                if(ele==1.0):
                    df_user.ix[count,'angular']=1.0
                count=count+1
            df_user=df_user.drop('angularjs',axis=1)
            count=0
            for ele in df_job.loc[:,'angularjs']:
                if(ele==1.0):
                    df_job.ix[count,'angular']=1.0
                count=count+1
            df_job=df_job.drop('angularjs',axis=1)
            
        if(flag=='Platform'):
            print(df_user.columns.tolist())
        if(flag=='Database'):
            print(df_user.columns.tolist())
            count=0
            for ele in df_user.loc[:,'microsoft sql server']:
                if(ele==1.0):
                    df_user.ix[count,'sql server']=1.0
                count=count+1
            df_user=df_user.drop('microsoft sql server',axis=1)
            count=0
            for ele in df_job.loc[:,'microsoft sql server']:
                if(ele==1.0):
                    df_job.ix[count,'sql server']=1.0
                count=count+1
            df_job=df_job.drop('microsoft sql server',axis=1)
        return df_user,df_job