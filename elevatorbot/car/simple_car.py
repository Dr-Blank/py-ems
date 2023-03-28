
from __future__ import annotations
import time

from typing import TYPE_CHECKING

from ..exceptions import (CarDoorNotClosedError, CarInvalidFloorError,
                          CarNotIdleError, MotorError)
from ..util import (CarState, ConsoleDisplay, Direction, Display, DoorState,
                     Motor, WorkingMotor)

if TYPE_CHECKING:
    pass

class SimpleCar:
    """A simple car class"""

    state: CarState

    def __init__(
        self,
        car_id: int,
        num_floors: int,
        speed: float,
        motor: Motor | None = None,
        display: Display | None = None,
    ) -> None:
        self.car_id = car_id
        self.num_floors = num_floors
        self.speed = speed
        self._direction = None
        self.state = CarState.IDLE
        self.door_state = DoorState.CLOSED
        self.display = display or ConsoleDisplay()
        self.motor = motor or WorkingMotor()
        self.available_floors = set(range(num_floors))
        self.current_floor = 0

    @property
    def current_floor(self) -> int:
        """Current floor"""
        return self._current_floor

    @property
    def direction(self) -> Direction | None:
        """Direction"""
        return self._direction

    @direction.setter
    def direction(self, value: Direction | None) -> None:
        """Direction"""
        self._direction = value
        self.display.show(self.current_floor, value)

    @current_floor.setter
    def current_floor(self, value: int) -> None:
        """Current floor"""
        self._current_floor = value
        self.display.show(value, self.direction)

    def open_door(self) -> None:
        """Open the door"""
        self.motor.activate()
        self.door_state = DoorState.OPEN

    def close_door(self) -> None:
        """Close the door"""
        self.motor.activate()
        self.door_state = DoorState.CLOSED

    def move_to(self, destination_floor: int) -> None:
        """Move to the given floor"""

        excs: list[Exception] = []
        # make sure the car is idle
        if self.state != CarState.IDLE:
            err = CarNotIdleError("", self.state)
            excs.append(err)

        # make sure the floor is valid
        if destination_floor not in self.available_floors:
            err = CarInvalidFloorError(
                f"Available floors: {self.available_floors}",
                destination_floor,
            )

            excs.append(err)

        # make sure the door is closed
        if self.door_state != DoorState.CLOSED:
            try:
                self.close_door()
            except MotorError as exc:
                # excs.append(ExceptionGroup([exc, CarDoorNotClosed("Door not closed")]))
                excs.append(CarDoorNotClosedError(f"Door not closed due to {exc}"))

        if excs:
            raise ExceptionGroup("Cannot move Car", excs)

        self.state = CarState.MOVING

        # sleep for every journey between floors while updating the current floor
        # check if going up or down
        direction = 1 if destination_floor > self._current_floor else -1
        self.direction = Direction.UP if direction > 0 else Direction.DOWN
        for floor in range(
            self._current_floor + direction, destination_floor + direction, direction
        ):
            time.sleep(self.speed)
            self.current_floor = floor

        self.state = CarState.IDLE
        self.direction = None
        return
