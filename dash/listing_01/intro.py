#! /usr/bin/env python3 

import dash 
import dash_html_components as html 

app = dash.Dash(__name__)

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