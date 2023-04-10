Here is an example script that randomly generates one of four different haiku poems about different seasons:

```python
import random

poems = [
    ["In the spring breeze\nA tiny flower blooms bright\nNew life awakens"],
    ["Summer sun shines down\nGolden fields shimmer and wave\nNature's bounty ripe"],
    ["Autumn leaves scatter\nCrisp air carries their farewell\nBeauty in decay"],
    ["Winter's icy grip\nSilent snowfall cloaks the earth\nStillness surrounds us"]
]

print(random.choice(poems))
```

This script starts by defining a list of four haiku poems, each about a different season. Each poem is itself a list of three strings, each representing one line of the haiku. Then, the script uses the `random.choice()` function to randomly choose one of the four poems from the list, and prints the chosen poem to the console.

Sample output:

```
In the spring breeze
A tiny flower blooms bright
New life awakens
```