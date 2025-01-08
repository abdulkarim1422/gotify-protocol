from app.initializers import db
from app import models
from sqlmodel import select

def get_all_projects():
    with db.get_session() as session:
        projects = session.exec(select(models.Project)).all()
        return projects
    
def get_project_by_id(project_id):
    with db.get_session() as session:
        project = session.get(models.Project, project_id)
        return project
    
def get_projects_by_user_id(user_id):
    with db.get_session() as session:
        projects = session.exec(select(models.Project).where(models.Project.user_id == user_id)).all()
        return projects
    
def create_project(project):
    with db.get_session() as session:
        session.add(project)
        session.commit()
        session.refresh(project)
        return project
    
def update_project(project):
    with db.get_session() as session:
        session.add(project)
        session.commit()
        session.refresh(project)
        return project
    
def delete_project(project):
    with db.get_session() as session:
        session.delete(project)
        session.commit()
        return project
    
def get_project_by_name(name):
    with db.get_session() as session:
        project = session.exec(select(models.Project).where(models.Project.name == name)).first()
        return project

