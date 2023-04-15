```python
import random

def add_emoji(text):
    emojis = ["😀", "😃", "😄", "😁", "😆", "😅", "😂", "🤣"]
    return text + random.choice(emojis)

# Hello World file
print(add_emoji("Hello World"))

# End
```