from fastapi import Request
from fastapi.responses import JSONResponse

from app.exceptions.custom_exceptions import (
    ResourceNotFoundException,
    UnauthorizedException,
    BadRequestException,
    ConflictException,
)


async def resource_not_found_handler(
    request: Request,
    exc: ResourceNotFoundException,
):
    return JSONResponse(
        status_code=404,
        content={
            "success": False,
            "message": exc.message,
        },
    )


async def unauthorized_handler(
    request: Request,
    exc: UnauthorizedException,
):
    return JSONResponse(
        status_code=401,
        content={
            "success": False,
            "message": exc.message,
        },
    )


async def bad_request_handler(
    request: Request,
    exc: BadRequestException,
):
    return JSONResponse(
        status_code=400,
        content={
            "success": False,
            "message": exc.message,
        },
    )


async def conflict_handler(
    request: Request,
    exc: ConflictException,
):
    return JSONResponse(
        status_code=409,
        content={
            "success": False,
            "message": exc.message,
        },
    )