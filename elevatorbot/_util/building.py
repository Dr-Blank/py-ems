"""Class to represent a building."""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from ..car import Car
    from ..manager.manager import Manager


class Floor(Protocol):
    """a floor in a building which has buttons to call up and down"""

    floor_number: int

    def add_manager(self, manager: Manager) -> None:
        """Add a manager to the floor."""

    def request_up(self) -> None:
        """Request an up elevator."""

    def request_down(self) -> None:
        """Request a down elevator."""


class Building:
    """Class to represent a building."""

    def __init__(self, num_floors: int, cars: list[Car]|None = None):
        """Initialize a building."""
        self.num_floors = num_floors
        self.cars = cars or []

    def get_cars(self) -> list[Car] | None:
        """Return the cars in the building."""
        return self.cars

    def add_car(self, car: Car) -> None:
        """Add a car to the building."""
        self.cars.append(car)

    @property
    def num_cars(self) -> int:
        """Return the number of cars in the building."""
        return len(self.cars)

    def __repr__(self) -> str:
        """Return the representation of the building."""
        return f"Building({self.num_floors})"
