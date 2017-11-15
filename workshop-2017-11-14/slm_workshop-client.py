from microbit import *

import radio
radio.on()

N = "slm"

radio.send(N)

images = {
    'A': ["00000", "00000", "00000", "00000", "00000"], 
    'B': ["00000", "00000", "00000", "00000", "00000"],
    'U': ["00000", "00000", "00000", "00000", "00000"],
    'D': ["00000", "00000", "00000", "00000", "00000"]
    }

while True:
    try:
        msg = radio.receive()
    except Exception as e:
        print(e)

    if msg is not None and msg.startswith(N):
        s = msg.split()
        if len(s) == 5:
            _, letter, x, y, b = s
            y = int(y)
            x = int(x)

            line = list(images[letter][y])
            line[x] = b
            images[letter][y] = ''.join(line)

    values = accelerometer.get_values()
    pos_y = values[1]
    
    if button_a.is_pressed():
        display.show(Image(':'.join(images['A'])))
    elif button_b.is_pressed():
        display.show(Image(':'.join(images['B'])))
    elif pos_y < -600:
        display.show(Image(':'.join(images['D'])))
    elif pos_y > 600:
        display.show(Image(':'.join(images['U'])))

    sleep(100)
    
    
    