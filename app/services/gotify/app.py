import requests
from app.initializers import env

def get_all_apps():
    url = f"{env.GOTIFY_URL}/application?token={env.GOTIFY_ADMIN_TOKEN}"
    response = requests.get(url)
    return response.json()
# [{'id': 1, 'name': 'xxxxxxx', 'description': 'xxxxxxx', 'defaultPriority': 5, "token": "xxXX.XXxx", "image": "image/image.jpeg", "internal": false,"lastUsed": "2019-01-01T00:00:00Z"}]

def create_app(name, description, defaultPriority=5):
    url = f"{env.GOTIFY_URL}/application?token={env.GOTIFY_ADMIN_TOKEN}"
    app_data = {
    "name": name,
   "description": description,
    "defaultPriority": defaultPriority
    }

    response = requests.post(url, json=app_data)
    return response.json() 
# {'id': 2, 'name': 'xxxxxxx', 'description': 'xxxxxxx', 'defaultPriority': 5, "token": "xxXX.XXxx", "image": "image/image.jpeg", "internal": false,"lastUsed": "2019-01-01T00:00:00Z"}
    
def update_app(app_id, name, description, defaultPriority=5):
    url = f"{env.GOTIFY_URL}/application/{app_id}?token={env.GOTIFY_ADMIN_TOKEN}"
    app_data = {
    "name": name,
   "description": description,
    "defaultPriority": defaultPriority
    }

    response = requests.put(url, json=app_data)
    return response.json()
# {'id': 2, 'name': 'xxxxxxx', 'description': 'xxxxxxx', 'defaultPriority': 5, "token": "xxXX.XXxx", "image": "image/image.jpeg", "internal": false,"lastUsed": "2019-01-01T00:00:00Z"}

def delete_app(app_id):
    url = f"{env.GOTIFY_URL}/application/{app_id}?token={env.GOTIFY_ADMIN_TOKEN}"
    response = requests.delete(url)
    return response.json()

def upload_image(app_id, image_path):
    url = f"{env.GOTIFY_URL}/application/{app_id}/image?token={env.GOTIFY_ADMIN_TOKEN}"
    files = {'file': open(image_path, 'rb')}
    response = requests.post(url, files=files)
    return response.json()

def delete_image(app_id):
    url = f"{env.GOTIFY_URL}/application/{app_id}/image?token={env.GOTIFY_ADMIN_TOKEN}"
    response = requests.delete(url)
    return response.json()
