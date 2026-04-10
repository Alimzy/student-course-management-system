from pydantic import BaseModel


class Course(BaseModel):
    course_code: str
    title: str
    description: str
    facilitator_email: str
    grade : str