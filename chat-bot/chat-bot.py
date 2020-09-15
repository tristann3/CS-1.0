# Chat bot by Tristan Thompson 9-15-2020
from random import choice
import os

pc = ["PC master race!", "pog! You're Awesome", "Jesus christ its Jason Bourne, nice!"]
console = ["60 fps lul.", ":pepehands:", "Haha, Thats so funny the last time I heard that, I laughed so hard I fell off my dinosaur!"]
non_gamer = ["What do you even do with your free time?", "OK, boomer."]

def get_bot_response(user_input, pc, console, non_gamer):
    def prompt2(non_gamer):
            user_input2 = input("Do you even play games? ")

            if (user_input2.lower() == "no") or (user_input2.lower() == "nope") or user_input2.lower() == "n":
                return choice(non_gamer)
            elif (user_input2.lower() == "yes") or (user_input2.lower() == "yeah") or user_input2.lower() == "yno":
                return "Oh, so youre not really a gamer. ok."
            else:
                return

    if user_input.lower() == "pc":
        return choice(pc)
    elif user_input.lower() == "console":
        return choice(console)
    elif user_input.lower() == "done":
        return "Dont forget, PC master race!"
    else:
        return prompt2(non_gamer)
        

os.system("clear")
print("Welcome to my Chat bot!\n")
user_input =""

while user_input != "done":
    user_input=input("Do you prefer PC or console gaming? ")
    print(get_bot_response(user_input, pc, console, non_gamer) + "\n")


