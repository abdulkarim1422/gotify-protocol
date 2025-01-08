import requests
from requests.auth import HTTPBasicAuth
from app.initializers import env

def current_user(username, password):
    url = f"{env.GOTIFY_URL}/current/user"
    response = requests.get(url, auth=HTTPBasicAuth(username, password))
    return response.json() # {'id': 1, 'name': 'xxxxxxx', 'admin': True}

def get_all_users():
    url = f"{env.GOTIFY_URL}/user?token={env.GOTIFY_ADMIN_TOKEN}"
    response = requests.get(url)
    return response.json() # [{'id': 1, 'name': 'xxxxxxx', 'admin': True}, {'id': 2, 'name': 'xxxxxxx', 'admin': False}]

def create_user(username, password):
    url = f"{env.GOTIFY_URL}/user?token={env.GOTIFY_ADMIN_TOKEN}"
    user_data = {
    "admin": False,
    "name": username,
    "pass": password
    }

    response = requests.post(url, json=user_data)
    return response.json() # {'id': 2, 'name': 'xxxxxxx', 'admin': False}

def get_user_by_id(user_id):
    url = f"{env.GOTIFY_URL}/user/{user_id}?token={env.GOTIFY_ADMIN_TOKEN}"
    response = requests.get(url)
    return response.json() # {'id': 2, 'name': 'xxxxxxx', 'admin': False}
    
def get_user_by_username(username):
    users = get_all_users()
    for user in users:
        if user['name'] == username:
            return user # {'id': 2, 'name': 'xxxxxxx', 'admin': False}
    return None 

def update_user(user_id, username, password):
    url = f"{env.GOTIFY_URL}/user/{user_id}?token={env.GOTIFY_ADMIN_TOKEN}"
    user_data = {
    "admin": False,
    "name": username,
    "pass": password
    }

    response = requests.put(url, json=user_data)
    return response.json() # {'id': 2, 'name': 'xxxxxxx', 'admin': False}

def delete_user(user_id):
    url = f"{env.GOTIFY_URL}/user/{user_id}?token={env.GOTIFY_ADMIN_TOKEN}"
    response = requests.delete(url)
    return response.json() # {'id': 2, 'name': 'xxxxxxx', 'admin': False}
