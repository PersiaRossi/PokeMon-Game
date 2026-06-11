import random

random.random()
#Pokemons
Pokemons = [
    "Pikachu",
    "Charizard",
    "Bulbasaur",
    "Greninja",
    "Lucario"
]
random_pokemon = random.choice(Pokemons)

print(Pokemons)
#guessing Pokemon
choice = input("Guess The Pokemon: ")
#Pokemon is correct or incorrect chack
if choice == random_pokemon:
    print("You are Correct. The Pokemon is",random_pokemon)
else:
    while True:
     choice = input("Try again: ")
     if choice == random_pokemon:
      print("This time you are Correct. Pokemon is",random_pokemon)
      break