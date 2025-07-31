import os
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import sqlite3
import requests


st.set_page_config(page_title="AI Skincare Recommender", layout="centered")



st.markdown("""
    <style>
    .centered-title {
        text-align: center;
        color: #a67c52;
        font-family: Georgia, serif;
        font-size: 2.8rem;
        margin-bottom: 0.5rem;
    }
    .footer {
        text-align: center;
        font-size: 0.8rem;
        color: #888;
        margin-top: 3rem;
    }
    </style>
""", unsafe_allow_html=True)
st.markdown("<div class='centered-title'>🧴 AI Skincare Recommender + GPT</div>", unsafe_allow_html=True)


user_name = st.text_input("Please enter your name:", max_chars=30)
skin_type = st.selectbox("Please select your skin type:", ["oily", "dry", "combination", "sensitive", "normal"])
concerns = st.multiselect(
    "What are your current skin concerns?",
    ["acne", "redness", "dryness", "aging", "dark spots", "sensitivity", "comedones"],
)


def get_past_recommendations(user_name):
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("SELECT product_name FROM user_history WHERE user_name = ?", (user_name.lower(),))
    past = [row[0] for row in cursor.fetchall()]
    conn.close()
    return past

def save_recommendation(user_name, recommendation_text):
    product_name = recommendation_text.split('\n')[0].strip()[:100]  # get first line as product name, max 100 chars

    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT OR IGNORE INTO user_history (user_name, product_name) VALUES (?, ?)",
        (user_name.lower(), product_name)
    )
    conn.commit()
    conn.close()



def generate_gpt_recommendation(user_name, skin_type, concerns, past_recs):
    prompt = f"Suggest skincare products for a user named {user_name} with {skin_type} skin and these concerns: {concerns}. Avoid these past recommendations: {past_recs}."

    headers = {
        "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
    }

    body = {
        "model": "openai/gpt-4",
        "messages": [
            {"role": "system", "content": "You are a helpful skincare assistant."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 300
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=body)
    

    response_json = response.json()
    
    if "choices" not in response_json:
        st.error("Oops! The AI service didn't return a valid response. Please try again later.")
        return "" 
    
    return response_json["choices"][0]["message"]["content"].strip()



if st.button("✨ Get your personalized recommendation"):
    if not user_name.strip():
        st.warning("Please enter your name.")
    elif not concerns:
        st.warning("Please select at least one concern.")
    else:
        past_recs = get_past_recommendations(user_name)
        with st.spinner("Generating your personalized recommendation..."):
            recommendation = generate_gpt_recommendation(user_name, skin_type, concerns, past_recs)

        
        st.markdown("### 🌟 Your new skincare recommendation:")
        st.write(recommendation)

        
        save_recommendation(user_name, recommendation[:100])  

        
        st.sidebar.header("🧴 Suggestions given earlier")
        if past_recs:
            for p in past_recs:
                st.sidebar.write(f"- {p}")
        else:
            st.sidebar.write("No past recommendations found.")
