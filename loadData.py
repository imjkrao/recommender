# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 17:34:52 2020

@author: jeevan
"""

import pandas as pd

import easygui

U_filename=easygui.fileopenbox(title="Select User data")
userDataset= pd.read_csv(U_filename)

J_filename=easygui.fileopenbox(title="Select Job data")
jobDataset= pd.read_csv(J_filename, encoding='unicode_escape')

