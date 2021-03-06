from fastapi import APIRouter
from app.api.endpoints import auth
from app.api.endpoints import user

router = APIRouter()

router.include_router(auth.router, prefix="/auth")
router.include_router(user.router, prefix="/user")
