from typing import Optional

from pydantic import BaseModel

class CourseResponse(BaseModel):
    course_code: str
    title: str
    description: str
    facilitator_email: str
    grade : str