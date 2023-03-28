from typing import Protocol


class Floor(Protocol):
    """a floor in a building which has buttons to call up and down"""

    floor_number: int
    
    def add_manager(self, manager: Manager) -> None:
        """Add a manager to the floor."""

    def request_up(self) -> None:
        """Request an up elevator."""

    def request_down(self) -> None:
        """Request a down elevator."""