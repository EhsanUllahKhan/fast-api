import uvicorn
from fastapi import FastAPI
# from Routers import users
# from Routers import items
from starlette.responses import RedirectResponse

from API.database import SessionLocal, engine
from API.Routers.user_routes import router_user
from API.Routers.lost_item_routes import router_lost_items
from API.Routers.found_item_routes import router_found_items

# name of app passed as args
app = FastAPI(title='Lost and found App', description='APIs for lost and found item Apis', version='0.1')
# routers for routers passed to app so that it knows all the routes.
app.include_router(router_user)
app.include_router(router_lost_items)
app.include_router(router_found_items)

# visiting the link for home directly takes to swagger docs. All the api testing was done on swagger docs.
@app.get('/')
async def home():
    return RedirectResponse(url="/docs/")

 # if project run through pycharm start button then the port will be 8080, but on uvicorn it'll be 8000
if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8080)
# alembic initialized for db migrations