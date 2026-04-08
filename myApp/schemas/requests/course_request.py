from pydantic import BaseModel

class CourseRequest(BaseModel):
    course_code: str
    title: str
    description: str
    facilitator_email: str