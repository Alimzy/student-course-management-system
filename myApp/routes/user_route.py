from fastapi import APIRouter
from myApp.schemas.requests.user_request import UserRequest
from myApp.schemas.responses.user_response import UserResponse
from myApp.services.user_service import UserService

from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/users", tags=["Users"])
user_service = UserService()




@router.post("/", response_model=UserResponse)
async def create_user(user: UserRequest):
    try:
        return await user_service.create_user(user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{email}")
async def get_user_by_email(email: str):
    try:
        return await user_service.get_user_by_email(email)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))




@router.get("/", response_model=list[UserResponse])
async def get_all_users():
    return await user_service.get_all_users()

@router.put("/{email}")
async def update_user(email: str, user_request: UserRequest):
    try:
        return await user_service.update_user(email, user_request)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{email}")
async def delete_user(email: str):
    try:
        return await user_service.delete_user(email)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))




