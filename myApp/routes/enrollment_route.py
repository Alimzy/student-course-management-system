
from myApp.schemas.requests.enrollment_request import EnrollmentRequest
from myApp.schemas.responses.enrollment_response import EnrollmentResponse
from myApp.services.enrollment_service import EnrollmentService

from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/enrollments", tags=["Enrollments"])
enrollment_service = EnrollmentService()




@router.post("/", response_model=EnrollmentResponse)
async def create_enrollment(enrollment: EnrollmentRequest):
    try:
        return await enrollment_service.enroll_student(enrollment)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))





@router.delete("/{title}")
async def delete_enrollment(title: str):
    try:
        return await enrollment_service.delete_enrollment(title)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))




