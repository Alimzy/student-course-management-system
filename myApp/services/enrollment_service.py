from myApp.database.database import enrollment_collection, user_collection, course_collection
from myApp.schemas.requests.enrollment_request import EnrollmentRequest
from myApp.schemas.responses.enrollment_response import EnrollmentResponse
from myApp.exceptions.my_exceptions import (
    UserNotFoundException,
    CourseNotFoundException,
    AlreadyEnrolledException
)

class EnrollmentService:

    async def enroll_student(self, enrollment_request: EnrollmentRequest):
        student = await user_collection.find_one({"email": enrollment_request.student_email})
        if not student:
            raise UserNotFoundException("Student not found")

        course = await course_collection.find_one({"title": enrollment_request.course_title})
        if not course:
            raise CourseNotFoundException("Course not found")

        existing = await enrollment_collection.find_one({
            "student_email": enrollment_request.student_email,
            "course_title": enrollment_request.course_title
        })
        if existing:
            raise AlreadyEnrolledException("Student already enrolled in this course")

        enrollment_dict = enrollment_request.dict()
        await enrollment_collection.insert_one(enrollment_dict)

        return EnrollmentResponse(
            student_email=enrollment_request.student_email,
            course_title=enrollment_request.course_title
        )


    async def delete_enrollment(self, student_email: str, course_title: str):
        enrollment = await enrollment_collection.find_one({
            "student_email": student_email,
            "course_title": course_title
        })
        if not enrollment:
            raise UserNotFoundException("Enrollment not found")
        await enrollment_collection.delete_one({
            "student_email": student_email,
            "course_title": course_title
        })
        return {"message": "Enrollment deleted successfully"}