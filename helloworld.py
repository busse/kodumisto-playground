# Modified Hello World file
import random

languages = {
    'English': 'Hello World',
    'French': 'Bonjour le monde',
    'Hindi': 'नमस्ते दुनिया',
    'Korean': '안녕하세요 세계',
    'Vietnamese': 'Chào thế giới'
}

message = random.choice(list(languages.values()))

print(message)

# End