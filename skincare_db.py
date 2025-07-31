import sqlite3

conn = sqlite3.connect("products.db")
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS recommendations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    skin_type TEXT,
    concern TEXT,
    product_name TEXT UNIQUE,
    product_image_url TEXT,
    product_tip TEXT
)
''')


sample_data = [
    ("oily", "acne", "La Roche-Posay Effaclar Duo", "https://...jpg", "Use a salicylic acid treatment to reduce breakouts."),
    ("dry", "aging", "Estée Lauder Advanced Night Repair", "https://...tif", "Apply at night to hydrate and reduce wrinkles."),
    
]

for entry in sample_data:
    cursor.execute('''
    INSERT OR IGNORE INTO recommendations (skin_type, concern, product_name, product_image_url, product_tip)
    VALUES (?, ?, ?, ?, ?)
    ''', entry)

cursor.execute('''
CREATE TABLE IF NOT EXISTS user_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name TEXT,
    skin_type TEXT,
    concern TEXT,
    product_name TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_name, product_name)
)
''')

conn.commit()
conn.close()

print("✅ Database and tables created with sample data.")
