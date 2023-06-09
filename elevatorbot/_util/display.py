""" Display for cars to show the current floor and direction. """
from __future__ import annotations

from typing import Any, Protocol, Optional

from .states import Direction


class Display(Protocol):
    """Display protocol"""

    def show(self, floor: int, direction: Optional[Direction]) -> Any:
        """Show the current floor and direction"""


class ConsoleDisplay:
    """Console display"""

    emoji = {
        Direction.UP: "⬆️",
        Direction.DOWN: "⬇️",
    }

    def show(self, floor: int, direction: Direction | None = None) -> None:
        """Show the current floor and direction"""
        output = f"Floor: {floor}"
        if direction:
            output += f"| {self.emoji[direction]}"
        print(output)
