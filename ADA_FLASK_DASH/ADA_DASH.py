import configparser
import pandas as pd
import requests
from pandas.io.json import json_normalize
from datetime import datetime
import numpy as np
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html


app = dash.Dash()

url_linear = 'http://127.0.0.1:5000/api/v1.0/linear'
url_random = 'http://127.0.0.1:5000/api/v1.0/random'

colors = {
     'background': '#111111',
     'text': '#7FDBFF'
 }

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children= 'Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
         }
    ),
    dcc.Input(id='input', value='Enter something here!', type='text', style={'textAlign': 'center'}),

    html.Div(children='Dash: A web application framework for Python.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    html.Div(id='output'),
    # dcc.Graph(
    #     id='static_graph_example',
    #     figure={
    #         'data': [
    #             {'x': [1, 2], 'y': [30, 34], 'type': 'bar', 'name': 'Lakas arak'},
    #             #{'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
    #         ],
    #         'layout': {
    #             'plot_bgcolor': colors['background'],
    #             'paper_bgcolor': colors['background'],
    #             'font': {
    #                 'color': colors['text']
    #             }
    #         }
    #     }
    # )
])

@app.callback(
    Output(component_id='output', component_property='children'),
    [Input(component_id='input', component_property='value')]
)
def update_value(input_data):
    
    parameter = {'p': input_data}
    
    linear = requests.get(url_linear, params=parameter).json().get('prediction')
    randomforest = requests.get(url_random, params=parameter).json().get('prediction')
    
    
    return dcc.Graph(
        id='example_price',
        figure={
            'data': [
                {'x': [1, 2] , 'y':[linear, randomforest] , 'type': 'bar', 'name': 'model comparison'},
            ],
            'layout': {
                'title': 'Model Comparison'
            }
        }
    )

if __name__ == "__main__":
    app.run_server(debug=True)
    

