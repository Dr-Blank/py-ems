"""Exceptions for the ElevatorBot package."""

from .._util.states import CarState


class ElevatorBotException(Exception):
    """Base class for ElevatorBot exceptions."""


class CarError(ElevatorBotException):
    """Exception for car errors."""


class CarNotIdleError(CarError):
    """Exception for car not idle errors."""

    def __init__(self, msg: str, state: CarState) -> None:
        self.msg = msg
        self.car_state = state
        super().__init__(f"{msg}\nCar not idle, current state: {state}")


class CarInvalidFloorError(CarError):
    """Exception for car invalid floor errors."""

    def __init__(self, msg: str, floor: int) -> None:
        self.floor = floor
        super().__init__(f"{msg}\nInvalid floor: {floor}")


class CarDoorNotClosedError(CarError):
    """Exception for car door not closed errors."""
