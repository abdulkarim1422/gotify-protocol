import requests
from app.initializers import env

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
    url = f"{env.GOTIFY_URL}/user?token={env.GOTIFY_ADMIN_TOKEN}"
    response = requests.get(url)
    users = response.json()
    for user in users:
        if user['name'] == username:
            return user
    return None # {'id': 2, 'name': 'xxxxxxx', 'admin': False}

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
