

from dash import Dash, html, dash_table, dcc
import pandas as pd
import plotly.express as px

df = pd.read_csv("dati.csv", sep = ";")

df["lt_codice_pulito"] = df["lt_codice"].str.split("-").str[0]

df_sorted = df.sort_values(by=['lt_codice', 'reg', 'OraSig'], ascending=[True, True, False])
raggruppato = df_sorted.groupby(['lt_codice', 'reg', 'OraSig'])['odi_value'].first().reset_index()

print(raggruppato)

# Initialize the app
app = Dash(__name__)

# App layout
app.layout = html.Div([
     dcc.Dropdown(
       id='lotti-dropdown',
       options=[{'label': lotto, 'value':lotto} for lotto in df['lt_codice_pulito']],
       value=df['lt_codice_pulito'].iloc[0] # mostra di default il primo
   ),
        html.H1(id='lotti-header'),
        html.Div([
          html.Div([
            html.H2('lotti'),
            html.Div(id='lotti_list')
          ], className='lotto'),
        html.Div([
          html.H2('lotti2'),
          html.Div(id='lotti_list2')
        ], className='lotto2'),
        html.Div([
           html.H2('lotti3'),
           html.Div(id='lotti_list3')
        ], className='lotto3')
   ], className='lotti-container')
])
    # html.Div(children='My First App with Data and a Graph'),
    # dash_table.DataTable(data=df.to_dict('records')),
    # dcc.Graph(figure=px.histogram(df, x='lt_codice_pulito', y='odi_value'))



if __name__ == '__main__':
    app.run(debug=True)