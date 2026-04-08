from typing import Optional

from pydantic import BaseModel

class GradeResponse(BaseModel):
    course_code: str
    grade: str
    facilitator_email: str

