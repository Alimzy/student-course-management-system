class UserAlreadyExistsException(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message

class UserNotFoundException(Exception):
    def __init__(self, user_id: str):
        self.user_id = user_id


class CourseAlreadyExistsException(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class CourseNotFoundException(Exception):
    def __init__(self, user_id: str):
        self.user_id = user_id

class AlreadyEnrolledException(Exception):
    def __init__(self, user_id: str):
        self.user_id = user_id


