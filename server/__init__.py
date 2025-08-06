from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from server.database import engine

# from server.routers.user import router as user_router
from server.routers import user, \
    auth, user_demographic, organization, \
    trainer_profile, exercise, workout_session, \
    const_page_data, workout_routine_exercise_relationship
# from server.routers import auth

def create_app():

    app = FastAPI()

    origins = [

        "http://localhost",
        "http://localhost:3000",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )



    app.include_router(user.router)
    app.include_router(auth.router)
    app.include_router(user_demographic.router)
    app.include_router(organization.router)
    app.include_router(trainer_profile.router)
    app.include_router(exercise.router)
    app.include_router(workout_session.router)
    app.include_router(const_page_data.router)
    app.include_router(workout_routine_exercise_relationship.router)

    @app.get("/")
    def root():
        return {
            "message": "Hello World"
        }

    return app
