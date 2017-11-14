from microbit import *
import radio

"""
PROTOKOL

Litery:
A - przycisk a
B - przycisk b
U - up
D - down

nick litera x y jasnosc

slm A 0 1 9
"""

radio.on()
radio.send('bartus')
# https://docs.python.org/3/tutorial/datastructures.html#sets
A = set()
B = set()
U = set()
D = set()

while True:
    try:
        rec = radio.receive()
    except:
        continue
    if rec is not None:
        # display.scroll(rec)
        # print(rec)
        t = rec.split()
        if len(t) == 5 and t[0] == 'bartus':
            if t[1] == 'A':
                A.add((int(t[2]), int(t[3]), int(t[4])))
            if t[1] == 'B':
                B.add((int(t[2]), int(t[3]), int(t[4])))
            if t[1] == 'U':
                U.add((int(t[2]), int(t[3]), int(t[4])))
            if t[1] == 'D':
                D.add((int(t[2]), int(t[3]), int(t[4])))

        if button_a.is_pressed():
            print('a is pressed')
            display.clear()
            for el in A:
                display.set_pixel(el[0], el[1], el[2])

        if button_b.is_pressed():
            print('b is pressed')
            display.clear()
            for el in B:
                display.set_pixel(el[0], el[1], el[2])

        if accelerometer.current_gesture() == 'up':
            print('gesture up')
            display.clear()
            for el in U:
                display.set_pixel(el[0], el[1], el[2])

        if accelerometer.current_gesture() == 'down':
            print('gesture down')
            display.clear()
            for el in D:
                display.set_pixel(el[0], el[1], el[2])
