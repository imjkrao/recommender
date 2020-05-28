# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 16:27:13 2020

@author: jeevan
"""

import pandas as pd
# import matplotlib.pyplot as plt
import numpy as np
#import sys
import time
import easygui

# print(sys.path)

#Load data
U_filename=easygui.fileopenbox(title="Select User data")
df= pd.read_csv(U_filename)

#Data Describe
print(df.describe())
print(df.head())
print(df.columns)

#Percentage of rows that null
n_row=df.shape[0]
print(df.isnull().sum()/n_row) 

#Drop Attributes
attr_to_drop=[]
attr_to_drop.append("MainBranch")
attr_to_drop.append("OpenSourcer")
attr_to_drop.append("EduOther")
attr_to_drop.append("MgrIdiot")
attr_to_drop.append("MgrMoney")
attr_to_drop.append("MgrWant")
attr_to_drop.append("BetterLife")
attr_to_drop.append("ITperson")
attr_to_drop.append("OffOn")
attr_to_drop.append("SocialMedia")
attr_to_drop.append("Extraversion")
attr_to_drop.append("ScreenName")
attr_to_drop.append("SOVisit1st")
attr_to_drop.append("SOVisitFreq")
attr_to_drop.append("SOVisitTo")
attr_to_drop.append("SOFindAnswer")
attr_to_drop.append("SOTimeSaved")
attr_to_drop.append("SOHowMuchTime")
attr_to_drop.append("SOAccount")
attr_to_drop.append("SOPartFreq")
attr_to_drop.append("SOJobs")
attr_to_drop.append("EntTeams")
attr_to_drop.append("SOComm")
attr_to_drop.append("WelcomeChange")
attr_to_drop.append("SONewContent")
attr_to_drop.append("Dependents")
attr_to_drop.append("BlockchainOrg")
attr_to_drop.append("BlockchainIs")
attr_to_drop.append("CodeRevHrs")
attr_to_drop.append("FizzBuzz")
attr_to_drop.append("SurveyLength")
attr_to_drop.append("SurveyEase")
attr_to_drop.append("CurrencySymbol")
attr_to_drop.append("CurrencyDesc")
attr_to_drop.append("CompTotal")
attr_to_drop.append("CompFreq")
attr_to_drop.append("ConvertedComp")
attr_to_drop.append("WorkWeekHrs")
attr_to_drop.append("WorkPlan")
attr_to_drop.append("WorkChallenge")
attr_to_drop.append("WorkRemote")
attr_to_drop.append("WorkLoc")
attr_to_drop.append("ImpSyn")

df=df.drop(df.columns[[41,42]],axis=1)
print(df.columns)
df=df.drop(attr_to_drop,axis=1)
# df=df[df.columns.difference(attr_to_drop)]
print(df.head())



print(sum(df.isnull().sum())/float(np.prod(df.shape)))
col_null=df.isnull().sum()/n_row
print(col_null.sort_values(ascending=False))

#move the removed data to removed.csv
# df.to_csv("removed.csv")
df1 = df.replace(np.nan, '', regex=True) # fill nan if blank

#Creating list of webframe / webframe nextyear
# User desired webframe next year
WebFrameDesireNextYear=list()
for value in df1["WebFrameDesireNextYear"]:
        new=value.split(';')
        for i in new:
            WebFrameDesireNextYear.append(i)
webframeNY=set(WebFrameDesireNextYear)

# User worked webframe 
WebFrameWorkedWith=list()
for value in df1["WebFrameWorkedWith"]:
        new=value.split(';')
        for i in new:
            WebFrameWorkedWith.append(i)
webframeW=set(WebFrameWorkedWith)
webframeNY.remove("")
webframeW.remove("")


#Creating list of Platform / Platform Desire NextYear
# User desired Platform NextYear
PlatformDesireNextYear=list()
for value in df1["PlatformDesireNextYear"]:
        new=value.split(';')
        for i in new:
            PlatformDesireNextYear.append(i)
platformNY=set(PlatformDesireNextYear)

# User worked Platform 
PlatformWorkedWith=list()
for value in df1["PlatformWorkedWith"]:
        new=value.split(';')
        for i in new:
            PlatformWorkedWith.append(i)
platformWW=set(PlatformWorkedWith)
platformNY.remove("")
platformWW.remove("")

#Creating list of Language / Language Desire NextYear
# User desired Language NextYear

LanguageDesireNextYear=list()
for value in df1["LanguageDesireNextYear"]:
        new=value.split(';')
        for i in new:
            LanguageDesireNextYear.append(i)
languageNY=set(LanguageDesireNextYear)

# User worked Language

LanguageWorkedWith=list()
for value in df1["LanguageWorkedWith"]:
        new=value.split(';')
        for i in new:
            LanguageWorkedWith.append(i)
languageWW=set(LanguageWorkedWith)
languageNY.remove("")
languageWW.remove("")

#Creating list of Database / Database Desire NextYear
# User desired Database NextYear
DatabaseDesireNextYear=list()
for value in df1["DatabaseDesireNextYear"]:
        new=value.split(';')
        for i in new:
            DatabaseDesireNextYear.append(i)
databaseNY=set(DatabaseDesireNextYear)

# User worked Database

DatabaseWorkedWith=list()
for value in df1["DatabaseWorkedWith"]:
        new=value.split(';')
        for i in new:
            DatabaseWorkedWith.append(i)
databaseWW=set(DatabaseWorkedWith)
databaseNY.remove("")
databaseWW.remove("")


# Creating list of Dev type
DevType=list()
for value in df1["DevType"]:
        new=value.split(';')
        for i in new:
            DevType.append(i)
devtypelist=set(DevType)
devtypelist.remove("")

#Creating list of MiscTech / MiscTech Desire NextYear
# User desired MiscTech NextYear
MiscTechDesireNextYear=list()
for value in df1["MiscTechDesireNextYear"]:
        new=value.split(';')
        for i in new:
            MiscTechDesireNextYear.append(i)
misctechNY=set(MiscTechDesireNextYear)

# User worked MiscTech

MiscTechWorkedWith=list()
for value in df1["MiscTechWorkedWith"]:
        new=value.split(';')
        for i in new:
            MiscTechWorkedWith.append(i)
misctechWW=set(MiscTechWorkedWith)

misctechWW.remove("")
misctechNY.remove("") # remove empty entry

#WebFrameWorkedWith webframeW
WebFrameWorkedWith = pd.DataFrame(df1['Respondent'])
for i in webframeW:
    
    WebFrameWorkedWith[i]=""

time_start=time.time()
coldic=dict(zip(WebFrameWorkedWith.columns,range(0,len(webframeW)+1)))
print(coldic)
print(df1.head())
for i in range(88883):
    data=(df1.loc[i,'WebFrameWorkedWith']).split(';')
    if(data[0]!=""):
       # print(data)
        for value in data:
            WebFrameWorkedWith.iloc[i,coldic[value]]=1
time_end=time.time()
print(time_end-time_start)

#WebFrameDesireNextYear webframeNY
WebFrameDesireNextYear = pd.DataFrame(df1['Respondent'])
for i in webframeNY:
    
    WebFrameDesireNextYear[i]=""
time_start=time.time()
coldic=dict(zip(WebFrameDesireNextYear.columns,range(0,len(webframeNY)+1)))
print(coldic)
print(df1.head())
for i in range(88883):
    data=(df1.loc[i,'WebFrameDesireNextYear']).split(';')
    if(data[0]!=""):
       # print(data)
        for value in data:
            WebFrameDesireNextYear.iloc[i,coldic[value]]=1
time_end=time.time()
print(time_end-time_start)

#PlatformWorkedWith platformWW
PlatformWorkedWith = pd.DataFrame(df1['Respondent'])
for i in platformWW:
    
    PlatformWorkedWith[i]=""
time_start=time.time()
coldic=dict(zip(PlatformWorkedWith.columns,range(0,len(platformWW)+1)))
print(coldic)
print(df1.head())
for i in range(88883):
    data=(df1.loc[i,'PlatformWorkedWith']).split(';')
    if(data[0]!=""):
       # print(data)
        for value in data:
            PlatformWorkedWith.iloc[i,coldic[value]]=1
time_end=time.time()
print(time_end-time_start)

#PlatformDesireNextYear platformNY
PlatformDesireNextYear = pd.DataFrame(df1['Respondent'])
for i in platformNY:
    
    PlatformDesireNextYear[i]=""
time_start=time.time()
coldic=dict(zip(PlatformDesireNextYear.columns,range(0,len(platformNY)+1)))
print(coldic)
print(df1.head())
for i in range(88883):
    data=(df1.loc[i,'PlatformDesireNextYear']).split(';')
    if(data[0]!=""):
       # print(data)
        for value in data:
            PlatformDesireNextYear.iloc[i,coldic[value]]=1
time_end=time.time()
print(time_end-time_start)

#LanguageWorkedWith languageWW
LanguageWorkedWith = pd.DataFrame(df1['Respondent'])
for i in languageWW:
    
    LanguageWorkedWith[i]=""
time_start=time.time()
coldic=dict(zip(LanguageWorkedWith.columns,range(0,len(languageWW)+1)))
print(coldic)
print(df1.head())
for i in range(88883):
    data=(df1.loc[i,'LanguageWorkedWith']).split(';')
    if(data[0]!=""):
       # print(data)
        for value in data:
            LanguageWorkedWith.iloc[i,coldic[value]]=1
time_end=time.time()
print(time_end-time_start)

#LanguageDesireNextYear languageNY
LanguageDesireNextYear = pd.DataFrame(df1['Respondent'])
for i in languageNY:
    
    LanguageDesireNextYear[i]=""
time_start=time.time()
coldic=dict(zip(LanguageDesireNextYear.columns,range(0,len(languageNY)+1)))
print(coldic)
print(df1.head())
for i in range(88883):
    data=(df1.loc[i,'LanguageDesireNextYear']).split(';')
    if(data[0]!=""):
       # print(data)
        for value in data:
            LanguageDesireNextYear.iloc[i,coldic[value]]=1
time_end=time.time()
print(time_end-time_start)

#DatabaseWorkedWith databaseWW
DatabaseWorkedWith = pd.DataFrame(df1['Respondent'])
for i in databaseWW:
    
    DatabaseWorkedWith[i]=""
time_start=time.time()
coldic=dict(zip(DatabaseWorkedWith.columns,range(0,len(databaseWW)+1)))
print(coldic)
print(df1.head())
for i in range(88883):
    data=(df1.loc[i,'DatabaseWorkedWith']).split(';')
    if(data[0]!=""):
       # print(data)
        for value in data:
            DatabaseWorkedWith.iloc[i,coldic[value]]=1
time_end=time.time()
print(time_end-time_start)

#DatabaseDesireNextYear databaseNY
DatabaseDesireNextYear = pd.DataFrame(df1['Respondent'])
for i in databaseNY:
    
    DatabaseDesireNextYear[i]=""
time_start=time.time()
coldic=dict(zip(DatabaseDesireNextYear.columns,range(0,len(databaseNY)+1)))
print(coldic)
print(df1.head())
for i in range(88883):
    data=(df1.loc[i,'DatabaseDesireNextYear']).split(';')
    if(data[0]!=""):
       # print(data)
        for value in data:
            DatabaseDesireNextYear.iloc[i,coldic[value]]=1
time_end=time.time()
print(time_end-time_start)

#MiscTechWorkedWith misctechWW
MiscTechWorkedWith = pd.DataFrame(df1['Respondent'])
for i in misctechWW:
    
    MiscTechWorkedWith[i]=""
time_start=time.time()
coldic=dict(zip(MiscTechWorkedWith.columns,range(0,len(misctechWW)+1)))
print(coldic)
print(df1.head())
for i in range(88883):
    data=(df1.loc[i,'MiscTechWorkedWith']).split(';')
    if(data[0]!=""):
       # print(data)
        for value in data:
            MiscTechWorkedWith.iloc[i,coldic[value]]=1
time_end=time.time()
print(time_end-time_start)

#MiscTechDesireNextYear misctechNY
MiscTechDesireNextYear = pd.DataFrame(df1['Respondent'])
for i in misctechNY:
    
    MiscTechDesireNextYear[i]=""
time_start=time.time()
coldic=dict(zip(MiscTechDesireNextYear.columns,range(0,len(misctechNY)+1)))
print(coldic)
print(df1.head())
for i in range(88883):
    data=(df1.loc[i,'MiscTechDesireNextYear']).split(';')
    if(data[0]!=""):
       # print(data)
        for value in data:
            MiscTechDesireNextYear.iloc[i,coldic[value]]=1
time_end=time.time()
print(time_end-time_start)

#DevType devtypelist
DevType = pd.DataFrame(df1['Respondent'])
for i in devtypelist:
    
    DevType[i]=""
time_start=time.time()
coldic=dict(zip(DevType.columns,range(0,len(devtypelist)+1)))
print(coldic)
print(df1.head())
for i in range(88883):
    data=(df1.loc[i,'DevType']).split(';')
    if(data[0]!=""):
       # print(data)
        for value in data:
            DevType.iloc[i,coldic[value]]=1
time_end=time.time()
print(time_end-time_start) 

# WebFrameWorkedWith.to_csv("WebFrameWorkedWith.csv")
# PlatformWorkedWith.to_csv("PlatformWorkedWith.csv")
# LanguageWorkedWith.to_csv("LanguageWorkedWith.csv")
# DatabaseWorkedWith.to_csv("DatabaseWorkedWith.csv")
# MiscTechWorkedWith.to_csv("MiscTechWorkedWith.csv")
# DevType.to_csv("DevType.csv")
# WebFrameDesireNextYear.to_csv("WebFrameDesireNextYear.csv")
# PlatformDesireNextYear.to_csv("PlatformDesireNextYear.csv")
# DatabaseDesireNextYear.to_csv("DatabaseDesireNextYear.csv")
# LanguageDesireNextYear.to_csv("LanguageDesireNextYear.csv")
# MiscTechDesireNextYear.to_csv("MiscTechDesireNextYear.csv")

#converted categorical variables into numerical
from sklearn.preprocessing import LabelEncoder
print(set(df1['JobSat']))
number=LabelEncoder()
df1['CareerSat']=number.fit_transform(df1['CareerSat'])
df1['Employment']=number.fit_transform(df1['Employment'])
df1['EdLevel']=number.fit_transform(df1['EdLevel'])
df1['Gender']=number.fit_transform(df1['Gender'])
df1['JobSat']=number.fit_transform(df1['JobSat'])
df1['OpenSource']=number.fit_transform(df1['OpenSource'])
df1['OpSys']=number.fit_transform(df1['OpSys'])
df1['Student']=number.fit_transform(df1['Student'])
df1['UndergradMajor']=number.fit_transform(df1['UndergradMajor'])
df1['YearsCode']=number.fit_transform(df1['YearsCode'])
df1['YearsCodePro']=number.fit_transform(df1['YearsCodePro'])

# df1.to_csv("df1_categoricalconverted.csv")
