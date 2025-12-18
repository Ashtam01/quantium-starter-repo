from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# Initialize the app
app = Dash(__name__)

# 1. Load the data
df = pd.read_csv('formatted_data.csv')

# 2. Ensure date is correctly formatted and sorted
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(by='date')

# 3. Create the Line Chart
fig = px.line(
    df, 
    x='date', 
    y='sales', 
    title='Pink Morsel Sales Over Time'
)

# 4. Define the App Layout
app.layout = html.Div(children=[
    html.H1(
        children='Soul Foods Sales Visualiser',
        style={'textAlign': 'center', 'fontFamily': 'Arial'}
    ),

    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

# Run the app
if __name__ == '__main__':
   app.run(debug=True)