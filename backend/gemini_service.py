import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Get API key from .env
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

genai.configure(api_key=api_key)

system_prompt = """
You are Chef-GPT, a professional recipe assistant.
- Always provide clear, step-by-step instructions.
- Ensure the recipe is simple, creative, and beginner-friendly.
- If calories or diet preferences are given, adapt the recipe accordingly.
"""

def fetch_recipe(ingredients: str, diet: str = None, calories: int = None):
    
    user_prompt = f"""
    Think step by step about how to combine these ingredients into a recipe.
    Ingredients: {ingredients}.
    {f'The recipe should be suitable for a {diet} diet.' if diet else ''}
    {f'Try to keep it under {calories} calories.' if calories else ''}

    First, explain your reasoning briefly.
    Then, provide the final recipe in a structured format.
    """

    final_prompt = f"{system_prompt.strip()}\n\n{user_prompt.strip()}"

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(final_prompt)
    return response.text.strip()
