from microbit import *
import radio

radio.on()

FORWARD = "FORWARD"
BACK = "BACK"
LEFT = "LEFT"
RIGHT = "RIGHT"
FASTER = "FASTER"
SLOWER = "SLOWER"
SPEEDUP = "SPEEDUP"
SPEEDDOWN = "SPEEDDOWN"
STOP = "STOP"
STOP_TURN = "STOPTURN"

RIGHT_PIN = pin0
LEFT_PIN = pin1
FORWARD_PIN = pin2
BACK_PIN = pin12

# speed between 300 and 1000
MAX_SPEED = 900
MIN_SPEED = 300
speed = 600


def forward():
    BACK_PIN.write_analog(0)
    FORWARD_PIN.write_analog(speed)


def back():
    FORWARD_PIN.write_analog(0)
    BACK_PIN.write_analog(speed)


def stop():
    FORWARD_PIN.write_analog(0)
    BACK_PIN.write_analog(0)
    RIGHT_PIN.write_digital(0)
    LEFT_PIN.write_digital(0)


def left():
    RIGHT_PIN.write_digital(0)
    LEFT_PIN.write_digital(1)


def right():
    LEFT_PIN.write_digital(0)
    RIGHT_PIN.write_digital(1)


def stop_turn():
    LEFT_PIN.write_digital(0)
    RIGHT_PIN.write_digital(0)


def speed_up():
    global speed
    if speed + 100 > MAX_SPEED:
        return
    speed += 150


def speed_down():
    global speed
    if speed - 100 < MIN_SPEED:
        return
    speed -= 150


def update_speed():
    lines = []
    level = speed / 150 - 1
    for i in range(level):
        lines.append("99999")

    for i in range(5-level):
        lines.append("00000")

    speed_level = Image(":".join(lines))
    display.show(speed_level)


while True:
    msg = radio.receive()
    if msg is None:
        update_speed()
        sleep(40)
        continue

    if msg == STOP:
        stop()
    elif msg == FORWARD:
        forward()
    elif msg == BACK:
        back()
    elif msg == LEFT:
        left()
    elif msg == RIGHT:
        right()
    elif msg == SPEEDUP:
        speed_up()
    elif msg == SPEEDDOWN:
        speed_down()
    elif msg == STOP_TURN:
        stop_turn()

display.show(Image.NO)