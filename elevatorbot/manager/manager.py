"""Bot that manages the elevators in a building."""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from ..util.building import Building, Floor
    from ..car import Car

class Manager(Protocol):
    """Bot that manages the elevators in a building."""


    def __init__(self, building: Building) -> None:
        """Initialize the manager."""

    def add_request(self, floor: int) -> None:
        """Add a request to the manager."""