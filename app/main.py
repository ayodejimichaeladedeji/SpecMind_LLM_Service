from fastapi import FastAPI
from app.errors.error import Error 
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.api.routes import APIResponse, router
from fastapi.exceptions import RequestValidationError

app = FastAPI()

app.include_router(router)

@app.exception_handler(Error)
async def custom_error_handler(request: Request, ex: Error):
    return JSONResponse(
        status_code=ex.status_code,
        content={
            "isSuccess": False,
            "body": None,
            "message": "An error occurred",
            "errorMessage": ex.message,
        }
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    error_details = exc.errors()
    messages = [f"{e['loc'][-1]}: {e['msg']}" for e in error_details]
    return JSONResponse(
        status_code=400,
        content=APIResponse(
            isSuccess=False,
            errorMessage="; ".join(messages),
            message="Validation failed"
        ).model_dump()
    )