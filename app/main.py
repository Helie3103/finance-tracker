from fastapi import FastAPI

from app.routers.health import router as health_router
from app.routers.auth import router as auth_router
from app.routers.users import router as user_router
from app.routers.categories import router as category_router
from app.routers.transactions import router as transaction_router

app = FastAPI(
    title="Personal Finance Manager",
    version="1.0.0"
)

app.include_router(
    auth_router,
    prefix = "/auth",
    tags = ["Authentication"]
)

@app.get("/")
def root():
    return {
        "message": "Personal Finance Manager API"
    }
    
app.include_router(
    user_router,
    prefix = "/users",
    tags = ["Users"]
)

app.include_router(
    category_router,
    prefix = "/categories",
    tags = ["Categories"]
)

app.include_router(
    transaction_router,
    prefix="/transactions",
    tags=["Transactions"]
)
