import keyboard
import random
import time

with open('textfile.txt', 'r') as file:
    wordlist = [line.strip().lower() for line in file if line.strip()]


typed = ''
idtyping = False

def type(word):
    print(word)
    for char in word:
        keyboard.press_and_release(char)
        time.sleep(random.uniform(0.03, 0.12))
    keyboard.press_and_release('enter')

def keypress(event):
    global typed, istyping

    if istyping:
        return

    if event.name == 'backspace':
        typed = typed[:-1]
        return

    if len(event.name) == 1:
        typed+= event.name

    if event.name == 'enter':
        fragment = typed.strip().lower()
        typed = ''

        if not fragment:
            print('nothing typed')
            return
        
        matches = []
        for word in wordlist:
            if fragment in word:
                matches.append(word)

        if not matches:
            print('no match')
            return
        
        word = random.choice(matches)

        istyping = True
        type(word)
        istyping = False


keyboard.hook(keypress)
