#! /usr/bin/env python3 

from jupyter_dash import JupyterDash
import dash_core_components as dcc
import dash_html_components as html 
import dash_bootstrap_components as dbc 
from dash.dependencies import Output, Input

app = JupyterDash(__name__)

app.layout = html.Div([
    dcc.Dropdown(id='color_dropdown', 
                    options=[{'label': color, 'value': color}
                                for color in ['blue', 'green', 'yellow']]),
    html.Div(id='color_output')
])

# simple function for selected color 
def display_selected_color_from_dropdown(color: str) -> str:
    if color is None:
        color = 'not value for color'
    return f'You selected -> {color}'

if __name__ == '__main__':
    app.run_server(mode='inline')