"""Test car module"""

import time

from elevatorbot.car import SimpleCar
from elevatorbot.exceptions import (
    CarDoorNotClosedError,
    CarInvalidFloorError,
    CarNotIdleError,
)
from elevatorbot.util import BrokenMotor, CarState, Direction, DoorState


def test_car_creation():
    """Test car creation"""
    car = SimpleCar(1, 10, 0.1)
    assert car.car_id == 1
    assert car.num_floors == 10
    assert car.speed == 0.1
    assert car.current_floor == 0
    assert car.state == CarState.IDLE
    assert car.door_state == DoorState.CLOSED
    assert car.available_floors == set(range(10))


def test_car_open_door():
    """Test car open door"""
    car = SimpleCar(1, 10, 0.1)
    car.open_door()
    assert car.door_state == DoorState.OPEN


def test_car_close_door():
    """Test car close door"""
    car = SimpleCar(1, 10, 0.1)
    car.open_door()
    car.close_door()
    assert car.door_state == DoorState.CLOSED


def test_car_move():
    """Test car move"""
    car = SimpleCar(1, 10, 0.1)
    car.move_to(5)
    assert car.current_floor == 5
    assert car.state == CarState.IDLE


def test_car_move_invalid_floor():
    """Test car move invalid floor"""
    car = SimpleCar(1, 10, 0.1)

    try:
        car.move_to(11)
    except* CarInvalidFloorError:
        assert True
    else:
        assert False


def test_car_move_invalid_car_state():
    """Test car move invalid state"""
    car = SimpleCar(1, 10, 0.1)
    car.state = CarState.MOVING
    try:
        car.move_to(5)
    except* CarNotIdleError:
        assert True
    else:
        assert False


def test_car_move_invalid_door_state_with_working_motor():
    """Test car move invalid door state"""
    car = SimpleCar(1, 10, 0.1)
    car.open_door()
    car.move_to(5)
    assert car.current_floor == 5
    assert car.state == CarState.IDLE


def test_car_door_with_broken_motor():
    """Test car move invalid door state"""
    car = SimpleCar(1, 10, 0.1, motor=BrokenMotor())
    car.door_state = DoorState.OPEN
    try:
        car.move_to(5)
    except* CarDoorNotClosedError:
        assert True
    else:
        assert False


def test_car_move_time():
    """Test car move time"""
    speed = 0.5
    floors = 4
    car = SimpleCar(1, 10, speed)
    start = time.time()
    car.move_to(floors)
    end = time.time()
    assert round(end - start, 1) == round(speed * floors, 1)


def test_car_move_display():
    """Test car move display"""

    class MockDisplay:
        """
        Mock display
        """

        def __init__(self) -> None:
            self.calls: list[tuple[int, Direction | None]] = []

        def show(self, floor: int, direction: Direction | None) -> None:
            """collect calls"""
            self.calls.append((floor, direction))

    display = MockDisplay()
    car = SimpleCar(1, 10, 0.1, display=display)
    assert display.calls == [(0, None)]

    display.calls = []

    going_up = 5
    car.move_to(going_up)
    assert display.calls == [(0, Direction.UP)] + [
        (i, Direction.UP) for i in range(1, going_up + 1)
    ] + [(going_up, None)]
    display.calls = []

    going_down = 2
    car.move_to(going_down)
    assert display.calls == [(going_up, Direction.DOWN)] + [
        (i, Direction.DOWN) for i in range(going_up - 1, going_down - 1, -1)
    ] + [(going_down, None)]
