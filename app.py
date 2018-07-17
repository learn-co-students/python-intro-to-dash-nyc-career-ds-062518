import dash
import dash_core_components as dcc # importing the core components from dash
import dash_html_components as html # importing the html components from dash
from uber_data import data

app = dash.Dash()

app.layout = html.Div(children = [html.H1('Hey, this is my first dash app!'),
html.P('Still under construction... :)'), dcc.Graph(
id = "uber_pricing_graph",
figure = {'data': [{'x' :data[0]['x'], 'y': data[0]['y'], 'type':data[0]['type'], 'name': data[0]['name']},
{'x': data[1]['x'], 'y': data[1]['y'], 'type': data[1]['type'], 'name': data[1]['name']}],
'layout': {'title': "Uber Pricing in Brooklyn and Manhattan"}}
)])

if __name__ == '__main__':
    app.run_server(debug = True)
