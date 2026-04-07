from pydantic import BaseModel


class Enrollment(BaseModel):
    id: str
    student_id : str
    course_id : str