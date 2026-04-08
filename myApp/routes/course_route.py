from fastapi import APIRouter
from myApp.schemas.requests.course_request import CourseRequest
from myApp.schemas.responses.course_response import CourseResponse
from myApp.services.course_service import CourseService

from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/courses", tags=["Courses"])
course_service = CourseService()




@router.post("/", response_model=CourseResponse)
async def create_course(course: CourseRequest):
    try:
        return await course_service.create_course(course)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[CourseResponse])
async def get_all_courses():
    return await course_service.get_all_course()

@router.get("/{title}")
async def get_course_by_title(title: str):
    try:
        return await course_service.get_course_by_title(title)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.put("/{title}")
async def update_course(title: str, course_request: CourseRequest):
    try:
        return await course_service.update_course(title, course_request)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{title}")
async def delete_course(title: str):
    try:
        return await course_service.delete_course(title)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))




