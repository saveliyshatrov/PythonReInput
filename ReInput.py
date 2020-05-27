import time
import os
from pynput.keyboard import Key, Controller


def Timer(time_in_seconds):
    os.system('cls' if os.name == 'nt' else 'clear')
    while time_in_seconds:
        print(time_in_seconds)
        time_in_seconds = time_in_seconds - 1
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')

keyboard = Controller()
print('start')

def click(char):
    if char == ';' or char == '}':
        keyboard.press(char)
        keyboard.release(char)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    else:
        keyboard.press(char)
        keyboard.release(char)


if __name__ == "__main__":
    Timer(10)
    f = open('code_txt.txt', 'r')
    code = f.read()

    while '  ' in code:
        code = code.replace('  ', '')

    for i in range(len(code)):
        time.sleep(0.005)
        click(code[i])

    print('Text re-printted!')
