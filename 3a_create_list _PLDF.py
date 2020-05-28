# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 14:11:17 2020

@author: jeevan
"""
#making dataframe of platform, languages, databases,Framework 
import numpy as np
import pandas as pd
user_df=pd.read_csv("E:\Thesis\DataSet\Stackoverflow userdata\survey_results_public.csv")
platforms_unclean=user_df.loc[:,"PlatformWorkedWith"].tolist()
platforms_unclean_next=user_df.loc[:,"PlatformDesireNextYear"].tolist()
platforms=[]
for string1,string2 in list(zip(platforms_unclean,platforms_unclean_next)):
    if(not pd.isnull(string1)):
        ele=string1.split(";")
        for plat in ele:
            if(plat not in platforms):
                platforms.append(plat)
    if(not pd.isnull(string2)):
        ele=string2.split(";")
        for plat in ele:
            if(plat not in platforms):
                platforms.append(plat)
platform_df=pd.DataFrame.from_dict({'Platform':platforms})
platform_df.to_csv("../platforms.csv")

language_unclean=user_df.loc[:,"LanguageWorkedWith"].tolist()
language_unclean_next=user_df.loc[:,"LanguageDesireNextYear"].tolist()
languages=[]
for string1,string2 in list(zip(language_unclean,language_unclean_next)):
    if(not pd.isnull(string1)):
        ele=string1.split(";")
        for plat in ele:
            if(plat not in languages):
                languages.append(plat)
    if(not pd.isnull(string2)):
        ele=string2.split(";")
        for plat in ele:
            if(plat not in languages):
                languages.append(plat)
language_df=pd.DataFrame.from_dict({'language':languages})
language_df.to_csv("../languages.csv")

database_unclean=user_df.loc[:,"WebFrameWorkedWith"].tolist()
database_unclean_next=user_df.loc[:,"WebFrameDesireNextYear"].tolist()
languages=[]
for string1,string2 in list(zip(database_unclean,database_unclean_next)):
    if(not pd.isnull(string1)):
        ele=string1.split(";")
        for plat in ele:
            if(plat not in languages):
                languages.append(plat)
    if(not pd.isnull(string2)):
        ele=string2.split(";")
        for plat in ele:
            if(plat not in languages):
                languages.append(plat)
frameWork_df=pd.DataFrame.from_dict({'frameWork':languages})
frameWork_df.to_csv("../framework.csv")


opsys_unclean=user_df.loc[:,"OpSys"].tolist()
#database_unclean_next=user_df.loc[:,"WebFrameDesireNextYear"].tolist()
languages=[]
for string1 in list(opsys_unclean):
    if(not pd.isnull(string1)):
        ele=string1.split(";")
        for plat in ele:
            if(plat not in languages):
                languages.append(plat)
frameWork_df=pd.DataFrame.from_dict({'os':languages})
frameWork_df.to_csv("../operating_systems.csv")
