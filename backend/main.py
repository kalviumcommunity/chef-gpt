from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import RecipeRequest
from gemini_service import fetch_recipe

app = FastAPI(title="Chef-GPT API")

# CORS (still there in case you ever connect a frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/recipes")
async def get_recipe(request: RecipeRequest):
    if not request.ingredients:
        raise HTTPException(status_code=400, detail="Ingredients required")

    try:
        recipe = fetch_recipe(
            ingredients=request.ingredients,
            diet=request.diet,
            calories=request.calories
        )
        return {"recipe": recipe}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# -------- CLI MODE --------
if __name__ == "__main__":
    print("Chef-GPT Terminal Mode")
    ingredients = input("Enter ingredients (comma separated): ")
    diet = input("Enter diet preference (press Enter to skip): ") or None
    calories_input = input("Enter calorie limit (press Enter to skip): ")
    calories = int(calories_input) if calories_input else None

    recipe = fetch_recipe(ingredients, diet, calories)
    print("\n--- Generated Recipe ---\n")
    print(recipe)
