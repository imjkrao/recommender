# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 13:00:28 2020

@author: jeevan
"""
import networkx as nx
import pandas as pd
import easygui

u_filename=easygui.fileopenbox(title="Select User Language data")
userDataset= pd.read_csv(u_filename, encoding='unicode_escape')



###Dart
Dart=userDataset[userDataset['dart']==1.0][1:25]
Dart['dart']=Dart['dart'].replace(to_replace=1.0,value='dart')
FG_1=nx.from_pandas_edgelist(Dart,source='Respondent',target='dart', edge_attr=True)
nx.set_node_attributes(FG_1, Dart.set_index('Respondent')['dart'].to_dict(), 'dart')

###Python
Python=userDataset[userDataset['python']==1.0][1:25]
Python['python']=Python['python'].replace(to_replace=1.0,value='python')
FG_2=nx.from_pandas_edgelist(Python,source='Respondent',target='python', edge_attr=True)
nx.set_node_attributes(FG_2, Python.set_index('Respondent')['python'].to_dict(), 'python')
FG_1.add_edges_from(FG_2.edges)
FG_1.add_nodes_from(FG_2.nodes)     

###JavaScript
JavaScript=userDataset[userDataset['javascript']==1.0][1:25]
JavaScript['javascript']=JavaScript['javascript'].replace(to_replace=1.0,value='javascript')
FG_3=nx.from_pandas_edgelist(JavaScript,source='Respondent',target='javascript', edge_attr=True)
FG_1.add_edges_from(FG_3.edges)

###html/css
Htmlcss=userDataset[userDataset['html/css']==1.0][1:25]
Htmlcss['html/css']=Htmlcss['html/css'].replace(to_replace=1.0,value='html/css')
FG_4=nx.from_pandas_edgelist(Htmlcss,source='Respondent',target='html/css', edge_attr=True)
FG_1.add_edges_from(FG_4.edges)

###Plot of all edges
nx.draw_networkx(FG_1, with_labels=True)
