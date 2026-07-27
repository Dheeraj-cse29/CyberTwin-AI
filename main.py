from fastapi import FastAPI

# Routers
from app import models
from app.api.auth import router as auth_router
from app.api.users import router as users_router
from app.api.assets import router as assets_router
from app.api.network import router as network_router

# Logger
from app.core.logger import logger

# Exception Handlers
from app.exceptions.handlers import (
    resource_not_found_handler,
    unauthorized_handler,
    bad_request_handler,
    conflict_handler,
)

# Custom Exceptions
from app.exceptions.custom_exceptions import (
    ResourceNotFoundException,
    UnauthorizedException,
    BadRequestException,
    ConflictException,
)

app = FastAPI(
    title="CyberTwin AI",
    description="AI-Powered Digital Twin Platform for SOC Operations",
    version="1.0.0",
)

# ----------------------------
# Register Exception Handlers
# ----------------------------

app.add_exception_handler(
    ResourceNotFoundException,
    resource_not_found_handler,
)

app.add_exception_handler(
    UnauthorizedException,
    unauthorized_handler,
)

app.add_exception_handler(
    BadRequestException,
    bad_request_handler,
)

app.add_exception_handler(
    ConflictException,
    conflict_handler,
)

# ----------------------------
# Register Routers
# ----------------------------

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(assets_router)
app.include_router(network_router)

# ----------------------------
# Startup Event
# ----------------------------

@app.on_event("startup")
async def startup():
    logger.info("🚀 CyberTwin AI Backend Started")


# ----------------------------
# Shutdown Event
# ----------------------------

@app.on_event("shutdown")
async def shutdown():
    logger.info("🛑 CyberTwin AI Backend Stopped")


# ----------------------------
# Root Endpoint
# ----------------------------

@app.get("/")
def root():
    logger.info("Root endpoint accessed")

    return {
        "application": "CyberTwin AI",
        "version": "1.0.0",
        "status": "Running",
        "message": "Welcome to CyberTwin AI Backend 🚀",
    }