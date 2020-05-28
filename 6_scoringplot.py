# -*- coding: utf-8 -*-
"""
Created on Thu May  7 22:35:55 2020

@author: jeevan
"""


#Load file related to User domain 

#Load row of user_ID related to all the Job domain  
def score_plot(matches,v):
    import chart_studio.plotly as py
    import plotly.graph_objs as go
    import plotly .offline as offline
    import plotly.express as px
    match=[lis for lis in matches if lis[1]!=0.0]
    total_recommendation=len(match)
    print(total_recommendation)
    #select top 60%
    score=[lis[1] for lis in matches if lis[1]]
    thres=round(max(score)*v,2)
    score_thres=[lis[1] for lis in matches if lis[1]>thres]
    TP=len(score_thres)
    TN=615-total_recommendation
    FP=total_recommendation-TP
    print(TP,TN,FP)
    title=[lis[0] for lis in matches if lis[1]>thres]
    # plt.plot(title,score, color='g')
    # plt.xlabel('Title')
    # plt.ylabel('Score')
    # plt.title('Accuracy')
    # plt.show()
    data = [go.Line(x=title, y=score)]
    layout = go.Layout(title = 'Accuracy', width = 700, height = 700, xaxis_type = 'category')
    fig = go.Figure(data=data, layout=layout)
    #offline.plot(fig,filename='Accuracy.html')
    precision= (TP/(TP+FP))
    recall=(TP/TP)
    F1= 2*((precision*recall)/(precision+recall))
    return print(precision, recall, F1)                                                    
