"""Motor module."""

from typing import Protocol

from .exceptions import MotorNotActivatedError


class Motor(Protocol):
    """A motor."""

    def activate(self) -> None:
        """
        Activate the motor.
        """


class WorkingMotor(Motor):
    """A working motor."""

    def activate(self) -> None:
        ...


class BrokenMotor(Motor):
    """A broken motor."""

    def activate(self) -> None:
        raise MotorNotActivatedError("Motor is broken")
