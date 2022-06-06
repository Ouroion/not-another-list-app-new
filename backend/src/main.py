# STD Librarys
import time

# 3rd Part Librarys
import uvicorn

from fastapi import APIRouter, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

# Self Created Libraries
import models
from database import engine
from routers import user as userRouter
from routers import list as listRouter
from routers import task as taskRouter
from DefaultException import DefaultException

database_starting = True
database_starting_attempts = 10
database_timeout = 5

print('Attempting to Connect to Database...')
while database_starting:
    try:
        models.Base.metadata.create_all(bind=engine)
        database_starting = False
    except Exception as e:
        database_starting_attempts = database_starting_attempts - 1
        if database_starting_attempts == 0:
            raise e
        print('Unable to Connect to Database. Trying again in: {} seconds'.format(database_timeout))
        time.sleep(database_timeout)

app = FastAPI(title="Not Another List App - Swagger")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


##########################
#   Exception Handler    #
##########################
@app.exception_handler(DefaultException)
async def unicorn_exception_handler(request: Request, exc: DefaultException):
    return JSONResponse(
        status_code=400,
        content={"errorMsg": exc.msg},
    )

##########################
#        ROUTES          #
##########################
router = APIRouter(
    prefix="/api",
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def connected():
    return {'message': 'Connected!'}


##########################
#        ROUTERS         #
##########################
router.include_router(userRouter.router)
router.include_router(listRouter.router)
router.include_router(taskRouter.router)
app.include_router(router)

if __name__ == "__main__":
    # TODO: Add Environment Var to set Port
    uvicorn.run("main:app", host="0.0.0.0", port=8081, reload=True)
