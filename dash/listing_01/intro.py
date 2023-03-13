#! /usr/bin/env python3 

import dash 
import dash_html_components as html 
import dash_bootstrap_components as dbc 
dbc.Col(children=[child1, child2, ...], lg={'size': 6, 'offset': 4}, md=12)
dbc.Row([
    dbc.Col('Column 1', width=2), 
    dbc.Col('Column 2', width=5), 
    dbc.Col('Column 3', width=4),
])

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

app.layout = html.Div([
    html.H1('Database', 
    style={
        'color': 'blue', 
        'fontSize': '45px',
    }),
    html.H2('The World Bank'), 
    html.P('Key Facts -> '),
    html.Ul([
        html.Li('Number of Economies -> 170'), 
        html.Li('Temporal Coverage -> 174 - 2019'), 
        html.Li('Update Frequency -> Quartely'), 
        html.Li('Last Updated -> March 18, 2020'),
        html.Li([
            'Source -> ', 
            html.A('https://datacatalog.worldbank.org/dataset/property-and-equuty-database', 
            href='https://datacatalog.worldbank.org/dataset/proverty-and-equity-database')
        ])
    ])
])


if __name__ == '__main__':
    app.run_server(debug=True)