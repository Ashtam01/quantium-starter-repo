import pandas as pd

# List of input files
files = [
    'data/daily_sales_data_0.csv',
    'data/daily_sales_data_1.csv',
    'data/daily_sales_data_2.csv'
]

all_data = []

for file in files:
    # Read the CSV file
    df = pd.read_csv(file)
    
    # 1. Filter: Use 'pink morsel' (lowercase) to match your data
    df = df[df['product'] == 'pink morsel']
    
    # 2. Clean price: Remove '$' and convert to float
    df['price'] = df['price'].str.replace('$', '', regex=False).astype(float)
    
    # 3. Calculate Sales
    df['sales'] = df['price'] * df['quantity']
    
    # 4. Select only the required columns
    df = df[['sales', 'date', 'region']]
    
    all_data.append(df)

# Combine and save
output_df = pd.concat(all_data)
output_df.to_csv('formatted_data.csv', index=False)

print("Success! 'formatted_data.csv' created with", len(output_df), "rows.")