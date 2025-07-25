import streamlit as st
import sqlite3

st.set_page_config(page_title="AI Skincare Recommender", layout="centered")

st.markdown("<h1 style='color:#a67c52; font-family:Georgia, serif;'>AI Skincare Recommender</h1>", unsafe_allow_html=True)
st.write(
    "Hi! I'm excited to help you find the best product for your skin concerns! "
    "Select your skin type and concerns below to get your personalized skincare product recommendations."
)

skin_type = st.selectbox(
    "Please select your skin type:",
    ["oily", "dry", "combination", "sensitive", "normal"],
    help="Your skin type helps us personalize recommendations."
)

concerns = st.multiselect(
    "What are your current skin concerns?",
    ["acne", "redness", "dryness", "aging", "dark spots", "sensitivity", "comedones"],
    help="Select one or more concerns for tailored advice."
)

if st.button("Get your personalized recommendations"):
    if not concerns:
        st.warning("Please select at least one skin concern to get recommendations.")
    else:
        st.subheader("Based on your input...")
        st.write(f"Skin type: **{skin_type}**")
        st.write(f"Concerns: **{', '.join(concerns)}**")
        st.markdown("### Suggested skincare tip or product:")

        with st.spinner("Loading recommendations..."):
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
                    # Layout with columns for image and text
                    col1, col2 = st.columns([1, 2])
                    with col1:
                        st.image(image_url, width=200)
                    with col2:
                        st.write(f"**Product:** {product_name}")
                        st.write(tip)
                    matched = True
                    break

            if not matched:
                st.info("Explore products with gentle ingredients suited to your skin type and concerns.")

            conn.close()
