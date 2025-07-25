import sqlite3

# create the database
conn = sqlite3.connect("products.db")
cursor = conn.cursor()

# Create the recommendations table
cursor.execute('''
CREATE TABLE IF NOT EXISTS recommendations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    skin_type TEXT,
    concern TEXT,
    product_name TEXT,
    product_image_url TEXT,
    product_tip TEXT
)
''')


# sample data
sample_data = [
    ("oily", "acne", "La Roche-Posay Effaclar Duo", "https://example.com/effaclar.jpg", "Use a salicylic acid treatment to reduce breakouts."),
    ("dry", "aging", "Estée Lauder Advanced Night Repair", "https://example.com/anr.jpg", "Apply at night to hydrate and reduce wrinkles."),
    ("sensitive", "redness", "Avene Antirougeurs Calm", "https://example.com/avene.jpg", "Use fragrance-free products with calming ingredients."),
    ("combination", "dark spots", "The Ordinary Alpha Arbutin", "https://example.com/alpha-arbutin.jpg", "Brightens and evens skin tone."),
    ("normal", "dryness", "CeraVe Moisturizing Cream", "https://example.com/cerave.jpg", "Deep hydration without clogging pores.")
]

# insert sample data
cursor.executemany('''
INSERT INTO recommendations (skin_type, concern, product_name, product_image_url, product_tip)
VALUES (?, ?, ?, ?, ?)
''', sample_data)

# Commit and close
conn.commit()
conn.close()

print(" database and table created with sample data")
