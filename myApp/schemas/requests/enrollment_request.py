from pydantic import BaseModel


class EnrollmentRequest(BaseModel):
    student_email : str
    course_title : str