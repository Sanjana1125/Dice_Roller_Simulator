import random
import time
import os

def clear():
    os.system('cls' if os.name =='nt' else 'clear') 

def dice_ascii(roll):
    dice_img = {

        1: [
             "-----",
            "|     |",
            "|  o  |",
            "|     |",
            "|     |",
             "-----"
        ],
        2: [
             "-----",
            "|o    |",
            "|     |",
            "|    o|",
            "|-----|"
        ],
        3: [
             "-----",
            "|o    |",
            "|  o  |",
            "|    o|",
            "|-----|"
        ],

        4: [
             "-----",
            "|o   o|",
            "|     |",
            "|o   o|",
            "|-----|"
        ],

        5: [
             "-----",
            "|o   o|",
            "|  o  |",
            "|o   o|",
            "|-----|"
        ],

        6: [
             "-----",
            "|o   o|",
            "|o   o|",
            "|o   o|",
            "|-----|"
        ]
    }
    return dice_img.get(roll, ["Error, Invalid"])

def animation_and_roll():
    clear()
    print("Welcome to the Dice Roller Simulator!")
    print("Press Enter to roll the dice: ")
    input()

    #Animation

    num_rolls = 12
    delay = 0.08

    for i in range (num_rolls):
        temp = random.randint(1,6)
        clear()
        print("Rolling dice...")
        for dice in dice_ascii(temp):
            print(dice)
        time.sleep(delay)

    clear()
    print("The dice landed on...")
    time.sleep(1)

    result = random.randint(1,6)
    for dice in dice_ascii(result):
        print(dice)
    print("The number is: {result}")

def main():
    while True:
        animation_and_roll()
        play_again = input("\nRoll again? (yes/no): ").lower().strip()
        if play_again != 'yes':
            print("That was a nice game! Thank you!")
            break

if __name__ == "__main__":
    main()

