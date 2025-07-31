***AI SKINCARE RECOMMENDER***

1. *Project Purpose*:
This app helps users find personalized skincare product recommendations based on their skin type and skin concerns, leveraging:

A SQLite database to store users' past recommendations and avoid repeating suggestions

An AI assistant (GPT-4 via OpenRouter API) to generate customized product suggestions

2. *Project Components*:
   
app.py: The main Streamlit app — user interface + logic

SQLite database (products.db): Stores history of users’ past recommended products

.env file: Securely stores your API key (e.g., OPENROUTER_API_KEY) outside your code

load_dotenv(): Loads environment variables from .env so API key can be accessed securely

Requests to OpenRouter API: Sends a prompt about skin type/concerns + past recommendations, and gets a GPT-generated skincare product suggestion

3. *How It Works*:
   Step-by-Step
   
A. *Setup & Initialization*

When you run the app with streamlit run app.py, the environment variables (like the API key) are loaded with load_dotenv()

The UI shows a title, inputs for user name, skin type, and skin concerns

B. *User Interaction*

User enters their name

Selects skin type (oily, dry, combination, sensitive, normal)

Selects one or more skin concerns (acne, redness, dryness, etc.)

Presses the "Get your personalized recommendation" button

C. *Fetch Past Recommendations*

The app connects to the local SQLite database (products.db)

Looks up previous products recommended to this user (by matching the lowercase user name)

Retrieves the product names previously suggested (if any) to avoid repeating

D. *Generate GPT Recommendation*

Constructs a prompt with user info: name, skin type, concerns, and the past recommended products to avoid

Sends this prompt to the OpenRouter GPT-4 API, with the API key securely pulled from .env

The AI responds with skincare product suggestions tailored to the user’s inputs

E. *Display & Save*

The app shows the AI’s recommendation on the main page

Saves the new recommendation product name into the database under the user’s history to track and avoid repeats next time

Also lists past recommended products in a sidebar

4. *Key Functions in app.py*

get_past_recommendations(user_name)
Queries the database for past product names for this user. Returns a list of strings.

save_recommendation(user_name, recommendation_text)
Takes the new recommendation and inserts it into the database for the user.

generate_gpt_recommendation(user_name, skin_type, concerns, past_recs)
Calls the OpenRouter GPT-4 API with the constructed prompt and returns the AI’s product suggestion.

5. *Security and Best Practices*
   
API key is never hardcoded in app.py — it's kept securely in the .env file, which is added to .gitignore

Your app loads the API key dynamically from the environment, so you can share the code without exposing credentials

If the AI API response is invalid or missing choices, the app gracefully shows an error message

6. *How to Run Locally*
Create .env file (in project root) with:

ini
Copy code
OPENROUTER_API_KEY=your_actual_api_key_here
Activate your virtual environment (example):

bash
Copy code
source venv/bin/activate
Install dependencies (if not done yet):

nginx
Copy code
pip install -r requirements.txt
Run the app with Streamlit:

arduino
Copy code
streamlit run app.py
7. ***How the Database Works***
The SQLite products.db contains at least one table, user_history, with columns:

user_name (TEXT)

product_name (TEXT)

Each time a new recommendation is generated, it inserts a new row for that user and product, avoiding duplicates with INSERT OR IGNORE.

8. ***User Experience***
Simple and clean interface powered by Streamlit

User inputs are validated (must enter name, select at least one concern)

Loading spinner while AI generates recommendation

Recommendations shown clearly on the main page

Past recommendations are accessible on sidebar for reference

9.***Summary***
   
You have built a personalized skincare recommender powered by AI that:

Collects user skin info

Remembers past recommendations using a database

Uses OpenRouter GPT-4 API to generate new suggestions dynamically

Maintains security by loading API keys from environment variables

Provides a friendly and responsive Streamlit user interface

### Prerequisites

- Python 3.8+
- Required libraries listed in `requirements.txt`
