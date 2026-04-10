

from pydantic import BaseModel


class EnrollmentResponse(BaseModel):
    student_email : str
    course_title : str