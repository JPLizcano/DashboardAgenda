# Import packages
from dash import Dash, html, dash_table, dcc
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

# Incorporate data
df = pd.read_csv('ventas.csv')

# Initialize the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# App layout
app.layout = html.Div([
    dbc.Row(dbc.Col(html.H2('Ventas'),
                    style={'textAlign': 'center', 'color': 'blue', 'fontSize': 30, 'marginTop': 20, 'marginBottom': 20})),
    dbc.Row([
        dbc.Col(dash_table.DataTable(data=df.to_dict('records'), page_size=10)),
    ], style={'fontSize': 12, 'padding': 20}),

    dbc.Row([
        dbc.Col(dcc.Graph(figure=px.histogram(df, x='Id', y='Nombre',)),
                style={'padding': 20}),
        dbc.Col(dcc.Graph(figure=px.histogram(df, x='Id', y='Pais', color_discrete_sequence=['#FF6000'])),
                style={'padding': 20}),
    ]),   
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)