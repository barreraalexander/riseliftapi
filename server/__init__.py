from fastapi import FastAPI
# from fastapi.middleware.cors 

from server.database import engine

def create_app():

    app = FastAPI()

    @app.get("/")
    def root():
        return {
            "message": "Hello World"
        }

    return app
