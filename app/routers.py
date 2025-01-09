from fastapi import APIRouter
from fastapi import Request
from app.services import user_service, notification_service

router = APIRouter()

@router.post("/user")
async def create_user(request: Request):
    username = request.query_params.get("username")
    password = request.query_params.get("password")
    if not username or not password:
        return {"error": "Missing required query parameters"}
    user = user_service.create_and_store_user(username, password)
    return user.model_dump()


@router.post("/notification")
async def create_notification(request: Request):
    username = request.query_params.get("username")
    projectname = request.query_params.get("projectname")
    title = request.query_params.get("title")
    content = request.query_params.get("content")
    if not username or not title or not content:
        return {"error": "Missing required query parameters"}
    await notification_service.send_notification(username, title, content, projectname)
    return {"message": "Notification sent successfully"}

