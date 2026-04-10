from fastapi import FastAPI
from myApp.routes.user_route import router as user_router
from myApp.routes.course_route import router as course_router
from myApp.routes.enrollment_route import router as enrollment_router
app = FastAPI()

app.include_router(course_router)
app.include_router(user_router)
app.include_router(enrollment_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=8000)