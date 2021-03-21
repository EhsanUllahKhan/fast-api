from fastapi import FastAPI
# from Routers import users
# from Routers import items
from starlette.responses import RedirectResponse

app = FastAPI(title='Lost and found App', description='APIs for lost and found item Apis', version='0.1')
# app.include_router(users.router_user)
# app.include_router(items.router_items)

@app.get('/')
async def home():
    return RedirectResponse(url="/docs/")

