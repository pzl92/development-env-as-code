from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/sample", tags=["Sample"])


@router.get("")
async def hello(request: Request):
    return JSONResponse(content={"message": "Hello, World!!!"})


@router.get("/error")
async def error(request: Request):
    raise HTTPException(status_code=400, detail="This is a sample error.")
