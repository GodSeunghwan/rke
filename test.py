from pynput import keyboard


def on_press(key):
    if key == keyboard.Key.esc:
        return False
    print(str(key)+"키를 누름")


def on_release(key):
    if key == keyboard.Key.esc:
        return False
    print(str(key)+"키를 땜")


listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()
listener.join()
