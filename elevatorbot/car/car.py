"""
Represents an elevator car.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol


if TYPE_CHECKING:
    from ..util.states import CarState, DoorState, Direction
    from ..manager import Manager
    from ..util.motor import Motor
    from ..util.display import Display


class Car(Protocol):
    """Protocol for a car."""

    car_id: int
    num_floors: int
    speed: float
    motor: Motor
    display: Display
    available_floors: set[int]
    current_floor: int
    direction: Direction | None
    state: CarState
    door_state: DoorState

    def open_door(self) -> None:
        """Open the door."""

    def close_door(self) -> None:
        """Close the door."""

    def move_to(self, destination_floor: int) -> None:
        """Move to the given floor."""

    def floor_request(self, floor: int) -> None:
        """Request a floor."""

    def add_manager(self, manager: Manager) -> None:
        """Add a manager to the car."""

