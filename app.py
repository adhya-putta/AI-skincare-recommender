import streamlit as st

st.set_page_config(page_title="AI Skincare Recommender", layout="centered")

st.title("AI skincare recommender")
st.write(
    "hii! i'm so excited to help you choose the best product for your skin concerns! it's super easy, just select your skin type and concerns to get your personalized skincare product recommendations."
)

skin_type = st.selectbox(
    "please select your skin type:",
    ["Oily", "Dry", "Combination", "Sensitive", "Normal"]
)


concerns = st.multiselect(
    "what are your current skin concerns?",
    ["Acne", "Redness", "Dryness", "Aging", "Dark spots", "Sensitivity", "Comedones"]
)

if st.button("get your personalized recommendations"):
    st.subheader(" based on your input...")
    st.write(f"Skin type: **{skin_type}**")
    st.write(f"Concerns: **{', '.join(concerns)}**")