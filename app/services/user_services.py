from app.repositories import user_repo
from app.services import gotify
from app import models

def create_and_store_user(username, password):
    # create user in gotify
    gotify.user.create_user(username, password)
    
    # create stable client for this uset in gotify
    client = gotify.client.create_client(username, password, "stable")
    client_token = client["token"]

    # store user in db
    user = models.User(username=username, password=password, client_token=client_token)
    user_repo.create_user(user)

    return user

def get_user_token(username):
    user = user_repo.get_user_by_username(username)
    return user.client_token
