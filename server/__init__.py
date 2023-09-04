from fastapi import FastAPI
# from fastapi.middleware.cors 

from server.database import engine

# from server.routers.user import router as user_router
from server.routers import user, auth, user_demographic
# from server.routers import auth

def create_app():

    app = FastAPI()

    app.include_router(user.router)
    app.include_router(auth.router)
    app.include_router(user_demographic.router)

    @app.get("/")
    def root():
        return {
            "message": "Hello World"
        }

    return app
