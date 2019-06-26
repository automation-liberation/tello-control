import requests

from tellocontrol import celery
from tellocontrol.control.constants import TelloCommandEnum
from tellocontrol.control.drone import Tello


@celery.task
def start_drone():
    response = requests.get('http://drone-platform/drone/on')
    return {"response": response}


@celery.task
def camera_on():
    tello = Tello()
    response = tello.send_command(TelloCommandEnum.STREAM_ON.value)
    tello.disconnect()
    return {"response": response}


@celery.task
def camera_off():
    tello = Tello()
    response = tello.send_command(TelloCommandEnum.STREAM_OFF.value)
    tello.disconnect()
    return {"response": response}


@celery.task
def take_off():
    tello = Tello()
    response = tello.send_command(TelloCommandEnum.TAKE_OFF.value)
    tello.disconnect()
    return {"response": response}


@celery.task
def land():
    tello = Tello()
    response = tello.send_command(TelloCommandEnum.LAND.value)
    tello.disconnect()
    return {"response": response}


@celery.task
def forward(distance):
    tello = Tello()
    response = tello.send_command(TelloCommandEnum.FORWARD.value.format(distance=distance))
    tello.disconnect()
    return {"response": response}


@celery.task
def back(distance):
    tello = Tello()
    response = tello.send_command(TelloCommandEnum.BACK.value.format(distance=distance))
    tello.disconnect()
    return {"response": response}


@celery.task
def left(distance):
    tello = Tello()
    response = tello.send_command(TelloCommandEnum.LEFT.value.format(distance=distance))
    tello.disconnect()
    return {"response": response}


@celery.task
def right(distance):
    tello = Tello()
    response = tello.send_command(TelloCommandEnum.RIGHT.value.format(distance=distance))
    tello.disconnect()
    return {"response": response}


@celery.task
def up(distance):
    tello = Tello()
    response = tello.send_command(TelloCommandEnum.UP.value.format(distance=distance))
    tello.disconnect()
    return {"response": response}


@celery.task
def down(distance):
    tello = Tello()
    response = tello.send_command(TelloCommandEnum.DOWN.value.format(distance=distance))
    tello.disconnect()
    return {"response": response}


@celery.task
def clockwise(degrees):
    tello = Tello()
    response = tello.send_command(TelloCommandEnum.CLOCKWISE.value.format(degrees=degrees))
    tello.disconnect()
    return {"response": response}


@celery.task
def counterclockwise(degrees):
    tello = Tello()
    response = tello.send_command(TelloCommandEnum.COUNTERCLOCKWISE.value.format(degrees=degrees))
    tello.disconnect()
    return {"response": response}
