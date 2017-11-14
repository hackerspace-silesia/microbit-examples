import microbit
import radio

MY_NICK = 'js'


class ImageReceiver:
    def __init__(self, nick):
        radio.on()
        radio.send(nick)
        self.nick = nick
        self.image_a = microbit.Image().copy()
        self.image_b = microbit.Image().copy()
        self.image_up = microbit.Image().copy()
        self.image_down = microbit.Image().copy()

    def receive(self):
        try:
            message = radio.receive()
        except ValueError:
            return
        if message is None:
            return
        ary = message.split()
        if len(ary) != 5:
            return
        nick, image, x, y, brightness = ary
        if nick != self.nick:
            return
        if image == 'A':
            self.image_a.set_pixel(int(x), int(y), int(brightness))
        elif image == 'B':
            self.image_b.set_pixel(int(x), int(y), int(brightness))
        elif image == 'U':
            self.image_up.set_pixel(int(x), int(y), int(brightness))
        elif image == 'D':
            self.image_down.set_pixel(int(x), int(y), int(brightness))

    def display(self):
        if microbit.button_a.is_pressed():
            microbit.display.clear()
            microbit.display.show(self.image_a)
        elif microbit.button_b.is_pressed():
            microbit.display.clear()
            microbit.display.show(self.image_b)
        elif microbit.accelerometer.current_gesture() == "up":
            microbit.display.clear()
            microbit.display.show(self.image_up)
        elif microbit.accelerometer.current_gesture() == "down":
            microbit.display.clear()
            microbit.display.show(self.image_down)


receiver = ImageReceiver(MY_NICK)
while True:
    receiver.display()
    receiver.receive()
