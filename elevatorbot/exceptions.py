"""Exceptions for the ElevatorBot package."""

from .states import CarState


class ElevatorBotException(Exception):
    """Base class for ElevatorBot exceptions."""


class MotorError(ElevatorBotException):
    """Exception for motor errors."""


class MotorNotActivatedError(MotorError):
    """Exception for motor not activated errors."""


class CarError(ElevatorBotException):
    """Exception for car errors."""


class CarNotIdleError(CarError):
    """Exception for car not idle errors."""

    def __init__(self, state: CarState) -> None:
        self.car_state = state
        super().__init__(f"Car not idle: {state}")


class CarInvalidFloorError(CarError):
    """Exception for car invalid floor errors."""

    def __init__(self, floor: int) -> None:
        self.floor = floor
        super().__init__(f"Invalid floor: {floor}")


class CarDoorNotClosedError(CarError):
    """Exception for car door not closed errors."""
