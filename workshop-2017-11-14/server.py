import random

from microbit import *

import radio
radio.on()

random.seed(123456789)

def shuffle(seq):
    new_seq = []
    while len(seq) != 0:
        n = random.choice(seq)
        seq.remove(n)
        new_seq.append(n)
    return new_seq


IMAGES = [
  Image.HEART, Image.HAPPY, Image.SMILE, Image.SAD,
  Image.CONFUSED, Image.ANGRY, Image.ASLEEP, Image.SURPRISED,
  Image.SILLY, Image.FABULOUS, Image.MEH, Image.YES, Image.NO,
  Image.ARROW_N, Image.ARROW_NE, Image.ARROW_E, Image.ARROW_SE, Image.ARROW_S,
  Image.ARROW_SW, Image.ARROW_W, Image.ARROW_NW,
  Image.TRIANGLE, Image.TRIANGLE_LEFT, Image.CHESSBOARD, Image.DIAMOND,
  Image.DIAMOND_SMALL, Image.SQUARE, Image.SQUARE_SMALL, Image.RABBIT,
  Image.COW,
  Image.PITCHFORK,
  Image.XMAS, Image.PACMAN, Image.TARGET, Image.TSHIRT,
  Image.ROLLERSKATE, Image.DUCK, Image.HOUSE, Image.TORTOISE, Image.BUTTERFLY,
  Image.STICKFIGURE, Image.GHOST, Image.SWORD, Image.GIRAFFE, Image.SKULL,
  Image.UMBRELLA, Image.SNAKE
]

clients = {}

while True:
    cl = radio.receive()
    if cl is not None and cl not in clients:
        images = {
                  'A': IMAGES[random.randrange(len(IMAGES))],
                  'B': IMAGES[random.randrange(len(IMAGES))],
                  'U': IMAGES[random.randrange(len(IMAGES))],
                  'D': IMAGES[random.randrange(len(IMAGES))],
                }
        clients[cl] = images
        print("New client: %s. Images: %s" % (cl, images))

    for cl in clients:
        radio.send("%s START" % cl)
        for l in shuffle(['A', 'B', 'U', 'D']):
            img = clients[cl][l]
            for x in range(5):
                for y in range(5):
                    brig = img.get_pixel(x, y)
                    if brig != 0:
                        radio.send("%s %s %d %d %d" % (cl, l, x, y, brig))
                        sleep(50)
        radio.send("%s STOP" % cl)

    display.scroll(str(len(clients)))
