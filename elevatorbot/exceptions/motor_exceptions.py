"""Motor exceptions."""
from .exceptions import ElevatorBotException


class MotorError(ElevatorBotException):
    """Exception for motor errors."""


class MotorNotActivatedError(MotorError):
    """Exception for motor not activated errors."""

