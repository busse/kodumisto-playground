import random

def add_emoji(text):
    emojis = ['😀', '😁', '😂', '😊', '😋', '😎', '😍', '😇']
    return text + random.choice(emojis)

print(add_emoji("Hello World"))