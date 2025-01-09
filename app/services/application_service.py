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

def check_app(username, app_name):
    user = user_service.get_user_by_username(username)
    user_apps = app_repo.get_apps_by_user_id(user.id)
    app = next((app for app in user_apps if app.name == app_name), None)
    if not app:
        # try searching for the app in the gotify server
        user_apps = gotify.application.get_all_apps(user.client_token)
        app = next((app for app in user_apps if app["name"] == app_name), None)
        if not app:
            # create the app
            app = create_app(username, app_name)
    return app