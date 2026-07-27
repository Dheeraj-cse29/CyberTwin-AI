class CyberTwinException(Exception):
    """Base exception for CyberTwin AI."""

    def __init__(self, message: str):
        self.message = message


class ResourceNotFoundException(CyberTwinException):
    pass


class UnauthorizedException(CyberTwinException):
    pass


class BadRequestException(CyberTwinException):
    pass


class ConflictException(CyberTwinException):
    pass