import pandas as pd
import sqlite3

df = pd.read_csv('skincare_products_extended.csv')

conn = sqlite3.connect('products.db')
cursor = conn.cursor()

for _, row in df.iterrows():
    
    cursor.execute('''
        INSERT OR IGNORE INTO recommendations (skin_type, concern, product_name, product_image_url, product_tip)
        VALUES (?, ?, ?, ?, ?)
    ''', (
        row['Skin Type'].lower(),
        row['Concern'].lower(),
        row['Product Name'],
        row.get('Product Image URL', ''),  
        row.get('Tip', '')                 
    ))

conn.commit()
conn.close()
print("✅ CSV data loaded into database.")
