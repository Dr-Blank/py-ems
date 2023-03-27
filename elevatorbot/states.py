from enum import StrEnum


class CarState(StrEnum):
    """State of an car"""

    IDLE = "idle"
    MOVING = "moving"
    EMERGENCY = "emergency"


class DoorState(StrEnum):
    """State of the doors"""

    CLOSED = "closed"
    OPEN = "open"
    OPENING = "opening"
    CLOSING = "closing"


class Direction(StrEnum):
    """Direction of the car"""

    UP = "up"
    DOWN = "down"
