Here's the python script that randomly outputs one of five jokes to the console. The jokes are about fish and each joke has a 50% chance of being shown in English or Icelandic:

```python
import random

# English jokes
english_jokes = [
    "Why did the fish blush? Because it saw the ocean's bottom!",
    "What do you call a fish that wears a bowtie? Sophisticated!",
    "Why don't fish play basketball? They're afraid of the net!",
    "What do you call a fish that's good at poker? A card shark!",
    "What do you get when you cross a fish and an elephant? Swimming trunks!"
]

# Icelandic jokes
icelandic_jokes = [
    "Hvaða fiskur er aldrei einmana? Hópafiskur!",
    "Hvað segir fiskurinn í þeirri gjáfuskrúði sem hann fékk? Þetta er mér að fara í bókina!",
    "Hvaða útlendingur eldar aldrei fisk? Samherji!",
    "Hvað segir dýrumálarin á fiskimóti? Áfram ferðast!",
    "Hvað gerist ef maður kastar skónum sínum í haf og sífelldar? Maður verður tilbúinn á næsta veiði!"
]

# randomly select a joke and language
if random.random() < 0.5:  # English
    joke = random.choice(english_jokes)
    print(joke)
else:  # Icelandic
    joke = random.choice(icelandic_jokes)
    print(joke)
```

Every time the script is run, it randomly selects one joke from the list of English or Icelandic jokes, then outputs the chosen joke to the console. The chances of getting an English or Icelandic joke are 50-50.