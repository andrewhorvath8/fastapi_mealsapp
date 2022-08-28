from sqlalchemy import Column, Integer, String, Numeric, Text, Boolean, LargeBinary
from mealsapp.db import Base


class Meals(Base):
    __tablename__ = "meals"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    price = Column(Numeric)
    ingredients = Column(Text)
    spicy = Column(Boolean)
    vegan = Column(Boolean)
    gluten_free = Column(Boolean)
    description = Column(Text)
    kcal = Column(Numeric)
    image = Column(LargeBinary)

    def __init__(self, name, price, ingredients, spicy, vegan, gluten_free, description, kcal, image, *args, **kwargs):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.spicy = spicy
        self.vegan = vegan
        self.gluten_free = gluten_free
        self.description = description
        self.kcal = kcal
        self.image = image
