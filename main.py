from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from mealsapp.user import router as user_router
from mealsapp.meals import router as meals_router
from mealsapp.auth import router as auth_router
from mealsapp.init import router as init_router

app = FastAPI(title='Meals App',
              version='1.0',
              )

app.include_router(auth_router.router)
app.include_router(user_router.router)
app.include_router(meals_router.router)
app.include_router(init_router.router)


def generate_html_response():
    html_content = """
            <html>
                <head>
                    <title>Meals App</title>
                </head>
                <body>
                    <h1>Welcome to Meals App!</h1>
                    <h2>You can reach the Swagger Docs on <a href="/docs">~/docs</a></h2>
                    <p> First create a user, then login, then you can test the features locked otherwise. </p>
                </body>
            </html>
            """
    return HTMLResponse(content=html_content, status_code=200)


@app.get("/", response_class=HTMLResponse)
async def welcome():
    return generate_html_response()

