#Quiz 2 by Tristan Thompson 9-17-2020

#Part 1
sounds_list = ["meow", "woof", "quack"]
def get_animal(animal_sound):
    if animal_sound == "meow":
        return "cat"
    elif animal_sound == "woof":
        return "dog"
    elif animal_sound == "quack":
        return "duck"
    else:
        return "I dont recognize that animal sound"

print(get_animal(sounds_list[0]))
print(get_animal(sounds_list[1]))
print(get_animal(sounds_list[2]))
print(get_animal("RAWR"))

#Part 2

colors = ["red", "yellow", "green", "blue", "purple"]

colors.append("violet")

colors.pop(1)

for color in colors:
    print(color)