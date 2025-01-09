import fastapi
from app import routers


app = fastapi.FastAPI()

# Include routers
app.include_router(routers.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Gotify Protocol App"}