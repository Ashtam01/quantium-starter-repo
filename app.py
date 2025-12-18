from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

# Initialize the app
app = Dash(__name__)

# 1. Load the data
df = pd.read_csv('formatted_data.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(by='date')

# 2. Define the App Layout
app.layout = html.Div(className='wrapper', children=[
    html.H1(children='Soul Foods Sales Visualiser'),

    # Radio Button for Region Selection
    html.Div(className='selector_container', children=[
        dcc.RadioItems(
            options=[
                {'label': 'All Regions', 'value': 'all'},
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'}
            ],
            value='all',  # Default selection
            id='region_selector',
            labelClassName='radio-item' # Helps with CSS styling
        )
    ]),

    # The Graph
    dcc.Graph(id='sales-line-chart')
])

# 3. Create the Callback to Update Graph based on Selection
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region_selector', 'value')
)
def update_graph(region):
    # Filter data based on selection
    if region == 'all':
        filtered_df = df
        title_text = "Pink Morsel Sales: All Regions"
    else:
        filtered_df = df[df['region'] == region]
        title_text = f"Pink Morsel Sales: {region.capitalize()} Region"

    # Create figure
    fig = px.line(
        filtered_df, 
        x='date', 
        y='sales', 
        title=title_text
    )

    # Apply some styling to the chart itself
    fig.update_layout(
        plot_bgcolor='#FFFFFF',
        paper_bgcolor='#FFFFFF',
        font_color='#333333',
        title_x=0.5 # Center the title
    )
    
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)