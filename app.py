import dash # importing the dash framework
import dash_core_components as dcc # importing the core components from dash
import dash_html_components as html # importing the html components from dash
from uber_data import data

# creating a new instance of Dash
app = dash.Dash()

app.layout = html.Div('Hello World')

app.layout = html.Div(children=[
    html.H1('Hey, this is my first dash app!'),
    html.P('Still under construction... :)'),
    dcc.Graph(
        id='uber_pricing_graph',
        figure = {
            'data': [
            {'x': [0.86, 1.5, 2.2, 2.6, 2.7, 3, 3.67], 'y': [6.40, 8.34, 9.46, 11.13, 12.55, 18.68], 'type':'line','name':'Brooklyn'},
            {'x': [0.93, 1.33, 2.6, 2.4, 2.94, 3.34, 4.11], 'y': [9.34, 10.09, 13.24, 16.53, 15.64, 25.65], 'type':'line','name':'Manhattan'},
            ],
            'layout': {
                'title':'Uber Pricing in Brooklyn and Manhattan'
            }
        }
    )
])

# telling our app to start the server if we are running this file
if __name__ == '__main__':
    app.run_server(debug=True)
