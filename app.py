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
    ["acne", "redness", "dryness", "aging", "dark spots", "sensitivity", "comedones"]
)

if st.button("get your personalized recommendations"):
    st.subheader("based on your input...")
    st.write(f"skin type: **{skin_type}**")
    st.write(f"concerns: **{', '.join(concerns)}**")

    st.markdown("### suggested skincare tip or product:")

    recs = {
        ("oily", "acne"): {
            "text": "Try a foaming cleanser with salicylic acid and a lightweight moisturizer.",
            "image": "https://theordinary.com/dw/image/v2/BFKJ_PRD/on/demandware.static/-/Sites-deciem-master/default/dwc17b2bd6/Images/products/The%20Ordinary/rdn-salicylic-acid-2pct-solution-otc.png?sw=860&sh=860&sm=fit",
            "product": "The Ordinary Salicylic Acid 2% Solution",
            "link": "https://theordinary.com/en-us/salicylic-acid-2-solution-acne-control-100098.html"
        },
        ("dry", "aging"): {
            "text": "Use a hydrating cleanser and apply retinol at night followed by moisturizer.",
            "image": "https://images.ulta.com/is/image/Ulta/2563010?$md$",
            "product": "La Roche-Posay Hydrating Cleanser",
            "link": "https://www.laroche-posay.us/hydrating-cleanser-3337872419414.html"
        },
        ("combination", "redness"): {
            "text": "Look for fragrance-free products with niacinamide or green tea.",
            "image": "https://images.ulta.com/is/image/Ulta/2589383?$md$",
            "product": "Paula's Choice Calm Redness Relief",
            "link": "https://www.paulaschoice.com/calming-serum/1409.html"
        },
        ("sensitive", "dark spots"): {
            "text": "Use gentle cleansers and serums with tranexamic acid or vitamin C.",
            "image": "https://images.ulta.com/is/image/Ulta/2609189?$md$",
            "product": "Avene Gentle Cleanser",
            "link": "https://www.aveneusa.com/gentle-cleanser"
        }
    }

    matched = False
    for concern in concerns:
        key = (skin_type.lower(), concern.lower())
        if key in recs:
            rec = recs[key]
            st.write(rec["text"])
            st.image(rec["image"], width=250)
            st.markdown(f"**Product:** [{rec['product']}]({rec['link']})")
            matched = True
            break

    if not matched:
        st.write("Explore products with gentle ingredients suited to your skin type and concerns.")
