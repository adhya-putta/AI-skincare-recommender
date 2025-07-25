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
    ("oily", "acne", "La Roche-Posay Effaclar Duo", "https://www.laroche-posay.us/dw/image/v2/AANG_PRD/on/demandware.static/-/Sites-acd-laroche-posay-master-catalog/default/dwb13c1487/img/3337875926065/LaRochePosay-Product-Skincare-Effaclar-Duo+M-40ml-3337875930673-ATF-PIM-Packshot-Front-1500x1500.jpg?sw=1536&sh=1536&sm=cut&sfrm=jpg&q=70", "Use a salicylic acid treatment to reduce breakouts."),
    ("dry", "aging", "Estée Lauder Advanced Night Repair", "https://slimages.macysassets.com/is/image/MCY/products/1/optimized/19229251_fpx.tif?op_sharpen=1&wid=500&fit=fit,1&fmt=webp", "Apply at night to hydrate and reduce wrinkles."),
    ("sensitive", "redness", "Avene Antirougeurs Calm", "https://www.dermstore.com/images?url=https://static.thcdn.com/productimg/original/15299452-3205153224559943.jpg&format=webp&auto=avif&width=800&height=800&fit=cover&dpr=2", "Use fragrance-free products with calming ingredients."),
    ("combination", "dark spots", "The Ordinary Alpha Arbutin", "https://theordinary.com/dw/image/v2/BFKJ_PRD/on/demandware.static/-/Sites-deciem-master/default/dwa689472f/Images/products/The%20Ordinary/FY25-D41247-ORD-Web-Alp-Arb-2pct-30ml-1x1-EN-1.jpg?sw=860&sh=860&sm=fit", "Brightens and evens skin tone."),
    ("normal", "dryness", "CeraVe Moisturizing Cream", "https://target.scene7.com/is/image/Target/GUEST_ef902ef2-7e84-4c3e-8857-6b45c768af63?wid=626&hei=626&qlt=80&fmt=pjpeg", "Deep hydration without clogging pores.")
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
