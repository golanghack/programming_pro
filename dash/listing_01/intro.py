#! /usr/bin/env python3 

from jupyter_dash import JupyterDash
import dash_core_components as dcc
import dash_html_components as html 
import dash_bootstrap_components as dbc 

app = JupyterDash(__name__)

app.layout = html.Div([
    dcc.Dropdown(options=[{'label': color, 'value': color}
        for color in ['blue', 'green', 'yellow']]),
        html.Div()
])
if __name__ == '__main__':
    app.run_server(mode='inline')