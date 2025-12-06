import dash
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output
from dash import dcc,html

# Load the dataset
crime_df=pd.read_csv('data/chicago_crime.csv')

# Creata the application
app=dash.Dash(__name__)
server = app.server
# The application layout
app.layout=html.Div([
    html.H1('Chicago Crime Dashboard', style={'textAlign':'center','font-size':30}),
    html.Br(),
    html.Div([
        html.H2('Select Crime Type:'),
        dcc.Dropdown(
            id='crime-dropdown',
            options=[{'label':c,'value':c} for c in crime_df['PRIMARY_TYPE'].unique()],
            value=crime_df['PRIMARY_TYPE'].unique()[0]
        ),
        html.H2('Select Aggregation: '),
        dcc.RadioItems(
            id='agg-radio',
            options=[
                {'label':'ward','value':'WARD'},
                {'label':'community_number','value':'COMMUNITY_AREA_NUMBER'}
            ],
            value='WARD',
            inline=True
        ),
        html.Div([
            html.Div([
                dcc.Graph(id='bar-plot')
            ]),
            html.Div([
                dcc.Graph(id='line-plot')
            ])
        ],style={'display':'flex'})
        
    ])
])

# Callback
@app.callback([
    Output('bar-plot','figure'),
    Output('line-plot','figure')
],
             [
                 Input('crime-dropdown','value'),
                 Input('agg-radio','value')
             ])

def update_graph(selected_crime,selected_agg):
    filtered_df=crime_df[crime_df['PRIMARY_TYPE']==selected_crime]
    bar_fig=px.bar(
        filtered_df.groupby(selected_agg).size().reset_index(name='Count'),
        x=selected_agg,
        y='Count',
        title=f"Number of {selected_crime} crimes by {selected_agg}"
    )
    line_fig=px.line(
        filtered_df.groupby('YEAR').size().reset_index(name='Count'),
        x='YEAR',
        y='Count',
        title=f"Yearly Evolution of {selected_crime} crime"
    )
    return bar_fig,line_fig

# Run Server
if __name__=='__main__':
    app.run_server(debug=True)
