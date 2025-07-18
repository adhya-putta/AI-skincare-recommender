import streamlit as st

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
    ["acne", "redness", "dryness", "aging", "dark spots", "sensitivity", "nomedones"]
)

if st.button("get your personalized recommendations"):
    st.subheader("based on your input...")
    st.write(f"skin type: **{skin_type}**")
    st.write(f"concerns: **{', '.join(concerns)}**")

    st.markdown("### suggested skincare tip or product:")

    if "acne" in [c.lower() for c in concerns] and skin_type.lower() == "oily":
        st.write("try a foaming cleanser with salicylic acid and a lightweight moisturizer.")
    elif "aging" in [c.lower() for c in concerns] and skin_type.lower() == "dry":
        st.write("use a hydrating cleanser and apply retinol at night followed by moisturizer.")
    elif "redness" in [c.lower() for c in concerns] and skin_type.lower() == "combination":
        st.write("look for fragrance-free products with niacinamide or green tea.")
    elif concerns:
        st.write("explore products with gentle ingredients suited to your skin type and concern.")
    else:
        st.write("select at least one skin concern to get recommendations!")

