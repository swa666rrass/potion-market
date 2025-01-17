import random


def welcome_screen():
    print("-------------------------")
    print("Welcome At The Markets.")
    print("-------------------------")
    print("\nWhere Do You Want To Go?")
    print("1 - Potion Markets")
    print("Anything Else - End")

    choice = input("Enter Your Choice: ")
    if choice == "1":
        potion_markets()
    else:
        exit()


def potion_markets():
    print("-------------------------")
    print("Welcome At The Potion Markets.")
    print("-------------------------")

    print("\nChoose Your Market?:")
    print("1 - Dark Jerome's Elixirs")
    print("2 - Elf's Health Essences And Other Potions")
    print("3 - Potions From Monsters Guts")
    print("4 - Witchers Alchemical Draft")
    print("5 - Tonics")
    print("Anything Else - End")

    choice = input("Your Choice: ")
    if choice == 1:
        print("You Are Going For A Dark Elixir")
    elif choice == 2:
        print("You Are Going For Essences (Made From ELF?!)")
    elif choice == 3:
        print("You Are Going For A Really Nasty Potion")
    elif choice == 4:
        print("You Are Going For Some Real Witcher Potion")
    elif choice == 5:
        print("You Are Just Going For A Basic Tonic")
    elif choice == 6:
        print("Your Inventory Contains:")
        potion_stat()
    else:
        print("You need a valid number")
        exit()

def main():
    welcome_screen()

    choice = input("Enter Your Choice: ")
    if choice == "1":
        potion_markets()
    else:
        print("You Are Going Home!")
        exit()

main()



