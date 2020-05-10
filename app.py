# -*- coding: utf-8 -*-
"""
Created on Tue May  5 15:56:30 2020

@author: jeevan
"""

# -*- coding: utf-8 -*-
"""
Created on Mon May  4 19:04:50 2020

@author: jeevan
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import dash_table
from dash.dependencies import ClientsideFunction,Output, Input
import plotly.graph_objs as go
from rec import recommend_job

import time


df1 = pd.read_csv('E:/Thesis/DataSet/Seenjobs/seenJobs_new10_.csv', encoding='unicode_escape')

colors = {
    'background': '#111111',
    'text': '#ffffff '
}

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.scripts.config.serve_locally = True
app.config['suppress_callback_exceptions'] = True

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Job Recommendation system',
        style={'textAlign': 'center','color': colors['text']}),

    html.Div(style={'textAlign': 'center','color': colors['text']},children=[  
        html.I("Input Your User ID Number"),
        html.Br(),
        dcc.Input(id="input", type="text", placeholder="1-80000",debounce=True),
        html.Br(),
        html.Div(style={'Clear': 'both'},children=[
        html.H4(style={'display': 'inline','textAlign': 'right'},children="Top 10 Jobs recommended to User ID "),
        html.H4(id='output',style={'display': 'inline','textAlign': 'left'})]),
        
        
    html.Script(id='particles-js',src='E:/Thesis/recommender/assets/app.js') ,  
        
    html.Div(style={'backgroundColor': colors['background'],'color': colors['text']},children=[
        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in df1.columns],
            style_header={'backgroundColor': 'white','fontWeight': 'bold'},
            style_cell={'color': 'black','overflow': 'hidden',
                        'textOverflow': 'ellipsis','maxWidth': 0},
            
            )
        ])
        
]) 
])

@app.callback([Output('table','data'),Output('output', 'children')],
              [Input('input', 'value')])

def on_data_set_table(input):
    data1=input
    print(data1)
    tab=recommend_job('E:/Thesis/recommender/user_job_profile/',data1,0)
    print(tab)
    return tab.to_dict(orient='records'),data1



if __name__ == '__main__':
    app.run_server(debug=False)