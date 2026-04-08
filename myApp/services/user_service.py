from myApp.database.database import user_collection
from myApp.schemas.requests.user_request import UserRequest
from myApp.schemas.responses.user_response import UserResponse
from myApp.models.Role import Role
from myApp.exceptions.my_exceptions import (
    UserAlreadyExistsException,
    UserNotFoundException
)

class UserService:

    async def create_user(self, user_request: UserRequest):
        user_dict = user_request.dict()

        existing_user = await user_collection.find_one({"email": user_dict["email"]})
        if existing_user:
            raise UserAlreadyExistsException("User with this email already exists")

        result = await user_collection.insert_one(user_dict)

        new_user = await user_collection.find_one({"_id": result.inserted_id})


        return UserResponse(
            name=new_user.get("name"),
            email=new_user.get("email"),
            role=Role(new_user.get("role"))
        )

    async def get_all_users(self):
        users = []
        async for user in user_collection.find():
            users.append(UserResponse(
                name=user.get("name"),
                email=user.get("email"),
                role=Role(user.get("role"))
            ))
        return users

    async def get_user_by_email(self, email: str):
        user = await user_collection.find_one({"email": email})
        if not user:
            raise UserNotFoundException(email)
        return UserResponse(
            name=user.get("name"),
            email=user.get("email"),
            role=Role(user.get("role"))
        )

    async def update_user(self, email: str, user_request: UserRequest):
        user = await user_collection.find_one({"email": email})
        if not user:
            raise UserNotFoundException(email)
        user_dict = user_request.dict()
        await user_collection.update_one(
            {"email": email},
            {"$set": user_dict}
        )
        updated_user = await user_collection.find_one({"email": user_dict["email"]})
        return UserResponse(
            name=updated_user.get("name"),
            email=updated_user.get("email"),
            role=Role(updated_user.get("role"))
        )

    async def delete_user(self, email: str):
        user = await user_collection.find_one({"email": email})
        if not user:
            raise UserNotFoundException(email)
        await user_collection.delete_one({"email": email})
        return {"message": "User deleted successfully"}



