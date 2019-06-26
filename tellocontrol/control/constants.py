from enum import Enum


class TelloCommandEnum(Enum):
    STREAM_ON = 'streamon'
    STREAM_OFF = 'streamoff'

    TAKE_OFF = 'takeoff'
    LAND = 'land'

    STOP = 'stop'
    EMERGENCY = 'emergency'

    SPEED = 'speed {cms}'

    UP = 'up {distance}'
    DOWN = 'down {distance}'
    LEFT = 'left {distance}'
    RIGHT = 'right {distance}'
    FORWARD = 'forward {distance}'
    BACK = 'back {distance}'

    CLOCKWISE = 'cw {degrees}'
    COUNTERCLOCKWISE = 'ccw {degrees}'

    FLIP = 'flip {direction}'
