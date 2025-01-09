from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
import uuid

# database class to store user data (gotify side)
class User(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(default=uuid.uuid4(), primary_key=True)
    username: str
    password: str
    created_at: datetime = Field(default=datetime.now())
    updated_at: datetime = Field(default=datetime.now())
    client_token: str

# # database class to store user projects (team side)
# class Project(SQLModel, table=True):
#     id: Optional[uuid.UUID] = Field(default=uuid.uuid4(), primary_key=True)
#     name: str
#     user_id: uuid.UUID
#     created_at: datetime = Field(default=datetime.now())
#     updated_at: datetime = Field(default=datetime.now())

# database class to store user apps (gotify side)
class App(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(default=uuid.uuid4(), primary_key=True)
    name: str
    user_id: uuid.UUID
    # project_id: str
    created_at: datetime = Field(default=datetime.now())
    updated_at: datetime = Field(default=datetime.now())
    app_token: str
