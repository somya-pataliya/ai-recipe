from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data model
class RecipeRequest(BaseModel):
    ingredients: str
    time: int

@app.get("/")
def home():
    return {"message": "AI Recipe Generator Backend Running 🚀"}

@app.post("/generate-recipe")
def generate_recipe(data: RecipeRequest):
    recipe_text = f"""
Ingredients: {data.ingredients}
Cooking Time: {data.time} minutes

Steps:
1. Prepare ingredients
2. Cook properly
3. Serve hot
"""
    return {"recipe": recipe_text}
