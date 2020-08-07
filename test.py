from pynput import keyboard
import time

start_time = time.time()

def on_press(key):
    if key == keyboard.Key.esc:
        return False
    print("{}키를 누름 [{}]".format(str(key), time.time() - start_time))


def on_release(key):
    if key == keyboard.Key.esc:
        return False
    print("{}키를 땜 [{}]".format(str(key),time.time() - start_time))


listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()
listener.join()
