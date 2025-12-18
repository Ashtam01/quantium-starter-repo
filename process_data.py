import pandas as pd

# List the file names (assuming they are in the 'data' folder)
files = [
    'data/daily_sales_data_0.csv',
    'data/daily_sales_data_1.csv',
    'data/daily_sales_data_2.csv'
]

# Create an empty list to hold the dataframes
all_data = []

for file in files:
    # Read the CSV
    df = pd.read_csv(file)
    
    # 1. Filter: Keep only 'Pink Morsel'
    df = df[df['product'] == 'Pink Morsel']
    
    # 2. Clean price: Remove '$' and convert to float number
    # (Prices are strings like "$3.00", we need the number 3.00)
    df['price'] = df['price'].str.replace('$', '').astype(float)
    
    # 3. Calculate Sales: quantity * price
    df['sales'] = df['price'] * df['quantity']
    
    # 4. Select only desired columns: sales, date, region
    df = df[['sales', 'date', 'region']]
    
    # Add to our list
    all_data.append(df)

# Combine all three dataframes into one
output_df = pd.concat(all_data)

# Save to a new CSV file without the index numbers
output_df.to_csv('formatted_data.csv', index=False)

print("Success! 'formatted_data.csv' has been created.")