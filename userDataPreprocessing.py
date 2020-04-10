# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 16:27:13 2020

@author: jeevan
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
import time
import easygui

# print(sys.path)
U_filename=easygui.fileopenbox(title="Select User data")
df= pd.read_csv(U_filename)
print(df.describe())
print(df.head())
print(df.columns)

n_row=df.shape[0]
print(df.isnull().sum()/n_row)
attr_to_drop=[]

attr_to_drop.append("MgrIdiot")
attr_to_drop.append("MgrMoney")
attr_to_drop.append("MgrWant")
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

df=df.drop(df.columns[[126,3,8,15,50,51,53,62,63,64,123,125,43,44,45,46,47,48,49]],axis=1)
print(df.columns)
df=df[df.columns.difference(attr_to_drop)]
print(df.head())
attr_to_drop=["HackathonReasons","ErgonomicDevices"]
df=df[df.columns.difference(attr_to_drop)]


print(sum(df.isnull().sum())/float(np.prod(df.shape)))
col_null=df.isnull().sum()/n_row
print(col_null.sort_values(ascending=False))
#print(sum(df.isnull().sum()))