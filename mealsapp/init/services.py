from mealsapp.meals import models


# Create data to insert in db
async def init_db_data(database):
    data_to_insert = [
        {
            "name": "Singapore Noodles",
            "price": 20,
            "ingredients": "4-6 ounces rice noodles, 2 Tbsp toasted sesame oil, 1/2 medium yellow onion, 12 whole snow peas, 3/4 medium red bell pepper, 1 Tbsp tamari, 2 tsp curry powder, 8 ounces extra-firm tofu",
            "spicy": False,
            "vegan": True,
            "gluten_free": True,
            "description": "Simplified plant-based Singapore noodles with tofu.",
            "kcal": 401,
            "image": b'0'
        },
        {
            "name": "Chickpea Spinach Curry",
            "price": 12.30,
            "ingredients": "2 Tbsp olive oil, 1 yellow onion, 2 garlic cloves, 1 inch fresh ginger, 1 1/2 Tbsp curry powder, 8 ounces spinach, 1 15 ounces can tomato sauce, 2 15 ounces cans chickpeas",
            "spicy": False,
            "vegan": True,
            "gluten_free": True,
            "description": "Vegan curried chickpeas with spinach.",
            "kcal": 322,
            "image": b'0'
        },
        {
            "name": "One Pot Penne Pasta",
            "price": 15.30,
            "ingredients": "6 ounces penne pasta, 1½ cups cherry tomatoes, 1½ cups sliced leeks, 1 medium zucchini, 1 red bell pepper, 3 small garlic cloves, 2 Tbsp extra-virgin olive oil, 2 Tbsp lemon juice, 1 tsp dried oregano, 1 tsp sea salt, 2 cups water, grated parmesan cheese",
            "spicy": False,
            "vegan": False,
            "gluten_free": False,
            "description": "Vegetables cooked in one pot with penne pasta.",
            "kcal": 420,
            "image": b'0'
        }
    ]
    for payload in data_to_insert:
        await create_new_meal_by_dict(payload, database)


# Check if Meal is already in db or not
def is_meal_in_db(meal_to_insert: models.Meals, database):
    new_meal = database.query(models.Meals).filter(models.Meals.name == meal_to_insert.name).first()
    if new_meal:
        return True
    else:
        return False


# Insert into db by dict. Note this is different from meals/services, because payload is not a request.
async def create_new_meal_by_dict(payload, database):
    new_meal = models.Meals(
        name=payload.get("name"),
        price=payload.get("price"),
        ingredients=payload.get("ingredients"),
        spicy=payload.get("spicy"),
        vegan=payload.get("vegan"),
        gluten_free=payload.get("gluten_free"),
        description=payload.get("description"),
        kcal=payload.get("kcal"),
        image=payload.get("image")
    )
    if not is_meal_in_db(new_meal, database):
        database.add(new_meal)
        database.commit()
        database.refresh(new_meal)


