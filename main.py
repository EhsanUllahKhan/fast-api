import uvicorn
from fastapi import FastAPI
# from Routers import users
# from Routers import items
from starlette.responses import RedirectResponse

from API.database import SessionLocal, engine
from API.Routers.user_routes import router_user
from API.Routers.lost_item_routes import router_lost_items

app = FastAPI(title='Lost and found App', description='APIs for lost and found item Apis', version='0.1')
app.include_router(router_user)
app.include_router(router_lost_items)


@app.get('/')
async def home():
    return RedirectResponse(url="/docs/")

if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8080)
# alembic initialized for db migrations