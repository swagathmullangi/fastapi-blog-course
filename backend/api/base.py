from fastapi import APIRouter, Depends, HTTPException
from api.v1 import route_user, route_blog, route_login

api_router = APIRouter()

api_router.include_router(route_user.router, prefix="/user", tags=["user"])
api_router.include_router(route_blog.router, prefix="/blog", tags=["blog"])
api_router.include_router(route_login.router, prefix="", tags=["login"])