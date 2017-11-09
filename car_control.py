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

enabled = False
old_gesture = None

turning_left = False
turning_right = False

while True:
    if enabled:
        display.show(Image.YES)
    else:
        display.show(Image.NO)

    if button_b.is_pressed() and button_a.is_pressed():
        enabled = not enabled
        if not enabled:
            radio.send(STOP)
        sleep(200)

    if enabled:
        if button_a.is_pressed():
            radio.send(FORWARD)
        if button_b.is_pressed():
            radio.send(BACK)

        gesture = accelerometer.current_gesture()
        if gesture != old_gesture:
            if gesture == "left":
                radio.send(LEFT)
            elif gesture == "right":
                radio.send(RIGHT)
            else:
                radio.send(STOP_TURN)

        values = accelerometer.get_values()
        x = values[0]
        print(values)
  
        if x < -600 and not turning_left:
            turning_left = True
            radio.send(LEFT)
        elif x > 600 and not turning_right:
            turning_right = True
            radio.send(RIGHT)
        else:
            if turning_left or turning_right:
                radio.send(STOP_TURN)
                turning_left = False
                turning_right = False

        y = values[1]
        if y < -600:
            radio.send(SPEEDUP)
        elif y > 600:
            radio.send(SPEEDDOWN)

    sleep(50)
