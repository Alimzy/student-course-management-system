from pydantic import BaseModel


class GradeRequest(BaseModel):
    course_code: str
    grade: str

