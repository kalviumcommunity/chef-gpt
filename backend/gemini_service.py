import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get API key from .env
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Configure Gemini
genai.configure(api_key=api_key)

def fetch_recipe(ingredients: str, diet: str = None, calories: int = None):
    prompt = f"Create a recipe using these ingredients: {ingredients}."
    if diet:
        prompt += f" The recipe should be suitable for a {diet} diet."
    if calories:
        prompt += f" Try to keep it under {calories} calories."

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text.strip()
