import streamlit as st
import sqlite3

st.set_page_config(page_title="AI Skincare Recommender", layout="centered")

st.title("AI skincare recommender")
st.write(
    "hii! i'm so excited to help you choose the best product for your skin concerns! it's super easy, just select your skin type and concerns to get your personalized skincare product recommendations."
)

skin_type = st.selectbox(
    "please select your skin type:",
    ["oily", "dry", "combination", "sensitive", "normal"]
)

concerns = st.multiselect(
    "what are your current skin concerns?",
    ["acne", "redness", "dryness", "aging", "dark spots", "sensitivity", "comedones"]
)

if st.button("get your personalized recommendations"):
    st.subheader("based on your input...")
    st.write(f"skin type: **{skin_type}**")
    st.write(f"concerns: **{', '.join(concerns)}**")

    st.markdown("### suggested skincare tip or product:")

    # Connect to your SQLite database
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()

    matched = False
    for concern in concerns:
        cursor.execute('''
            SELECT product_name, product_image_url, product_tip
            FROM recommendations
            WHERE skin_type = ? AND concern = ?
            LIMIT 1
        ''', (skin_type.lower(), concern.lower()))
        rec = cursor.fetchone()

        if rec:
            product_name, image_url, tip = rec
            st.write(tip)
            st.image(image_url, width=250)
            st.markdown(f"**Product:** {product_name}")
            matched = True
            break

    if not matched:
        st.write("Explore products with gentle ingredients suited to your skin type and concerns.")

    conn.close()
