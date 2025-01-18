import random


global gold_coins, hp, pwr, insanity

gold_coins = 1
hp = 100
pwr = 0
insanity = 0

def add_hp(amount):
    global hp
    hp += amount

    if hp > 1000:
        hp = 1000

def subtract_hp(amount):
    global hp
    hp -= amount

    if hp < 0:
        hp = 0

def subtract_insanity(amount):
    global insanity
    insanity -= amount

    if insanity < 0:
        insanity = 0


def add_power(amount):
    global pwr
    pwr += amount

    if pwr > 1000:
        pwr = 1000

def subtract_power(amount):
    global pwr
    pwr -= amount

    if pwr < 0:
        pwr = 0

def stats():
    print("Your stats...")
    print(f"### HP {hp} ### Power {pwr} ### Insanity {insanity} ### Gold Coins {gold_coins}")

def random_stats_dark():
    global hp, pwr, insanity
    hp = random.randint(200,500)
    pwr = random.randint(200,500)
    insanity = random.randint(400,800)
    print(f"### HP {hp} ### Power {pwr} ### Insanity {insanity} ### Gold Coins {gold_coins}")


def random_stats_elf():
    global hp, pwr, insanity
    hp = random.randint(50,200)
    pwr = random.randint(50,200)
    insanity = random.randint(0,20)
    print(f"### HP {hp} ### Power {pwr} ### Insanity {insanity} ### Gold Coins {gold_coins}")


def random_stats_guts():
    global hp, pwr, insanity
    hp = random.randint(0,300)
    pwr = random.randint(0,300)
    insanity = random.randint(500,900)
    print(f"### HP {hp} ### Power {pwr} ### Insanity {insanity} ### Gold Coins {gold_coins}")


def random_stats_witcher():
    global hp, pwr, insanity
    hp = random.randint(500,1000)
    pwr = random.randint(500,1000)
    insanity = random.randint(0,50)
    print(f"### HP {hp} ### Power {pwr} ### Insanity {insanity} ### Gold Coins {gold_coins}")


def random_stats_tonics():
    global hp, pwr, insanity
    hp = random.randint(5,100)
    pwr = random.randint(5,100)
    insanity = random.randint(0,5)
    print(f"### HP {hp} ### Power {pwr} ### Insanity {insanity} ### Gold Coins {gold_coins}")



def welcome_screen():
    print("-------------------------")
    print("Welcome At The Markets.")
    print("-------------------------")
    print("\nWhere Do You Want To Go?")
    print("1 - Potion Markets")
    print("Anything Else - End")

    choice = input("Enter Your Choice: ")
    if int(choice) == 1:
        potion_markets()
    else:
        print("WTF we didnt even started yet?")
        exit()

def drk_potions():
    global gold_coins, hp, pwr, insanity

    print("-----------------------------------------")
    print("You Going Into Jeromes Dark Elixirs")
    print("-----------------------------------------")
    print("As you entered, the first thing you noticed was a dwarf sitting in a really tall chair. He was all in black clothes and had a big black Wizards Hat. You couldnt stop looking at him. Now you think he is EMO, and he thinks your a FREAK... ")

    print("\nLets Show You The Offers.")
    print("1 - Shades Whispering Potion - 15 Silvers")
    print("2 - Brew From A Lost Soul - 25 Silvers")
    print("3 - Wraiths Kiss - 50 Silvers")

    choice = input("Choose Your Potion And Lets Hope It wont Make You Emo: ")
    if int(choice) == 1:
        if gold_coins < 0.15:
            print("You dont have any coins, go make some money or beg some on the street you VAGABOND")
        elif gold_coins >= 0.15:
            gold_coins -= 0.15
            print("I have a bad news for you if you are scared of whispering")
            print("You have drank the potion. ----Suddenly You are hearing some really creepy sounds... But your muscles has got bigger. ")
            random_stats_dark()

    elif int(choice) == 2:
        print("How the hell did they make this one")
        if gold_coins < 0.25:
            print("You dont have any coins, go make some money or beg on the street VAGABOND")
        elif gold_coins >= 0.25:
            gold_coins -= 0.25
            print("You have drank the interesting potion. ---- Suddenly you started to see dead people.... They were everywhere just minding their bussiness, but it could be useful sometimes. ")
            random_stats_dark()

    elif int(choice) == 3:
        print("Na am Good, I dont need a kiss")
        if gold_coins < 0.5:
            print("You dont have any coins, go make some money or beg on the street VAGABOND")
        elif gold_coins >= 0.5:
            gold_coins -= 0.5
            print("The name is little disturbing...")
            print("You have drank the potion lets see what it does. ----You started to feel little dizzy and a horriblle freeze had came through your body and you saw some creature lurking at you far in the sreets. It seemed like other people dont see it. Lets just hope that its gonna be a positive thing...")
            random_stats_dark()

        else:
            print("You are going back!")
            potion_markets()

def potion_markets():
    global gold_coins, hp, pwr, insanity

    print("-------------------------")
    print("Welcome At The Potion Markets.")
    print("-------------------------")
    stats()
    print("\nChoose Your Market?:")
    print("1 - Jerome's Dark Elixirs")
    print("2 - Elf's Health Essences And Other Potions")
    print("3 - Potions From Monsters Guts")
    print("4 - Witchers Alchemical Draft")
    print("5 - Tonics")
    print("Anything Else - End")

    choice = input("Your Choice: ")
    if int(choice) == 1:
        print("You Are Going For A Dark Elixir")
        drk_potions()
    elif int(choice) == 2:
        print("You Are Going For Essences (Made From ELF?!)")
    elif int(choice) == 3:
        print("You Are Going For A Really Nasty Potion")
    elif int(choice) == 4:
        print("You Are Going For Some Real Witcher Potion")
    elif int(choice) == 5:
        print("You Are Just Going For A Basic Tonic")
    elif int(choice) == 6:
        print("Your Stats Are:")
        stats()

def main():
    welcome_screen()

    choice = input("Enter Your Choice: ")
    if int(choice) == 1:
        potion_markets()
    else:
        print("You Are Going Home!")
        exit()

main()



