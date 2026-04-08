from myApp.database.database import course_collection
from myApp.schemas.requests.course_request import CourseRequest
from myApp.schemas.responses.course_response import CourseResponse
from myApp.exceptions.my_exceptions import (
    CourseAlreadyExistsException,
    CourseNotFoundException
)

class CourseService:

    async def create_course(self, course_request: CourseRequest):
        user_dict = course_request.dict()

        existing_course = await course_collection.find_one({"title": user_dict["title"]})
        if existing_course:
            raise CourseAlreadyExistsException("course already exists")

        result = await course_collection.insert_one(user_dict)

        new_course = await course_collection.find_one({"_id": result.inserted_id})


        return CourseResponse(
            course_code=new_course.get("course_code"),
            title=new_course.get("title"),
            description=new_course.get("description"),
        facilitator_email = new_course.get("facilitator_email")

        )

    async def get_all_course(self):
        courses = []
        async for course in course_collection.find():
            courses.append(CourseResponse(
                course_code=course.get("course_code"),
                title=course.get("title"),
                description=course.get("description"),
                facilitator_email=course.get("facilitator_email")
            ))
        return courses

    async def get_course_by_title(self, title: str):
        course = await course_collection.find_one({"title": title})
        if not course:
            raise CourseNotFoundException("Course not find")
        return CourseResponse(
            course_code=course.get("course_code"),
            title=course.get("title"),
            description=course.get("description"),
            facilitator_email=course.get("facilitator_email")
        )

    async def update_course(self, title: str, course_request: CourseRequest):
        course = await course_collection.find_one({"title": title})
        if not course:
            raise CourseNotFoundException("Course not find")
        course_dict = course_request.dict()
        await course_collection.update_one(
            {"title": title},
            {"$set": course_dict}
        )
        updated_course = await course_collection.find_one({"title": course_dict["title"]})
        return CourseResponse(
            course_code=updated_course.get("course_code"),
            title=course.get("title"),
            description=course.get("description"),
            facilitator_email=course.get("facilitator_email")
        )

    async def delete_course(self, title: str):
        course = await course_collection.find_one({"title": title})
        if not course:
            raise CourseNotFoundException("Course not find")
        await course_collection.delete_one({"title": title})
        return {"message": "Course deleted successfully"}



