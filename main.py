from fastapi import FastAPI
from mealsapp.user import router as user_router
from mealsapp.meals import router as meals_router
from mealsapp.auth import router as auth_router

app = FastAPI(title='Meals App',
              version='1.0',
              )

app.include_router(auth_router.router)
app.include_router(user_router.router)
app.include_router(meals_router.router)

