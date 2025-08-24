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


# Define a system prompt
system_prompt = """
You are Chef-GPT, a professional recipe assistant.
- Always provide clear, step-by-step instructions.
- Ensure the recipe is simple, creative, and beginner-friendly.
- If calories or diet preferences are given, adapt the recipe accordingly.
"""

def fetch_recipe(ingredients: str, diet: str = None, calories: int = None):
    user_prompt = f"Create a recipe using these ingredients: {ingredients}."
    if diet:
        user_prompt += f" The recipe should be suitable for a {diet} diet."
    if calories:
        user_prompt += f" Try to keep it under {calories} calories."

    final_prompt = f"{system_prompt.strip()}\n\n{user_prompt.strip()}"

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(final_prompt)
    return response.text.strip()
