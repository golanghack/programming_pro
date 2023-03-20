#! /usr/bin/env python3 

import dash 
import dash_html_components as html 
import dash_bootstrap_components as dbc 

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
    dbc.Tabs([
        dbc.Tab([
            html.Ul([
                html.Br(), 
                html.Li('Number of Economies -> 170'), 
                html.Li('Temporal Coverage -> 1974 - 2019'),
                html.Li('Update Frequency -> Quarterly'), 
                html.Li('Last Updated -> March 18, 2020'),
                html.Li([
                    'Source -> ', 
                    html.A('https://datacatalog.worldbank.org/dataset/poverty-and-equity-database',
                                    href='https://datacatalog.worldbank.org/dataset/poverty-and-equity-database')
                ]) 
            ])
        ], label='Two'), 
        dbc.Tab([
            html.Ul([
                html.Br(), 
                html.Li('Data'),
                html.Li(['Githyb -> ', html.A('https://github.com', 
                                href='https://github.com')
            ])
            ])
        ], label='One')
    ])
])


if __name__ == '__main__':
    app.run_server(debug=True)