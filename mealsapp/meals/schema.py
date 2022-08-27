from pydantic import BaseModel, constr


class Meal(BaseModel):
    name: constr(min_length=2, max_length=50)
    price: float
    ingredients: str
    spicy: bool
    vegan: bool
    gluten_free: bool
    description: str
    kcal: float
    image: bytes


class DisplayMeal(BaseModel):
    id: int
    name: str
    price: float
    ingredients: str
    spicy: bool
    vegan: bool
    gluten_free: bool
    description: str
    kcal: float
    image: bytes

    class Config:
        orm_mode = True
