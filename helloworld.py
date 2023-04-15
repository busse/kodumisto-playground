import random

def add_emoji():
    emoji = ['😀', '😂', '😍', '🤩', '👍', '👌', '🙌', '🤗']
    return random.choice(emoji)

print("Hello World" + add_emoji())