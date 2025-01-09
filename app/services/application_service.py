from app.services import gotify
from app.services import user_service
from app import models
from app.repositories import app_repo

def create_app(username, app_name):
    # get user token from db
    client_token = user_service.get_user_token(username)

    # create app in gotify
    app = gotify.application.create_app(client_token, app_name)
    app_token = app["token"]

    # store app in db
    user = user_service.get_user_by_username(username)
    app = models.App(name=app_name, user_id=user.id, app_token=app_token)
    app_repo.create_app(app)
    
    return app

