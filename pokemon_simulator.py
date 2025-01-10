#Diana Reyes Tamayo
#11/21/2024
#Pokemon Simulator

#Init
import random

#Global variables
pokemon_level = 0
pokemon_name = "froakie"
day = 0


# Functions⠀⠀⠀
def draw_pokemon():
    global pokemon_level
    if pokemon_level < 5:
        print("""
        Your pokemon is Froakie :)
        ⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬜⬛🟦🟦🟦🟦⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟦🟦🟦🟦⬛⬛⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬛🟦🟦🟦🟦🟦🟦⬛⬜⬜⬜⬜⬜⬜⬜⬛🟦🟦🟦⬛⬛🟦🟦⬛⬜⬜⬜
        ⬜⬜⬜⬜⬛🟦🟦🟦🟦⬛⬛⬛🟦⬛⬜⬜⬜⬜⬜⬛🟦🟦🟦⬛🟨🟨⬛🟦⬛⬜⬜⬜
        ⬜⬜⬜⬛🟦🟦🟦🟦⬛🟨🟨🟨⬛🟦⬛⬜⬜⬜⬛🟦🟦🟦⬛🟨🟨🟨🟨⬛🟦⬛⬜⬜
        ⬜⬜⬜⬛🟦🟦🟦⬛🟨🟨🟨🟨🟨⬛⬛⬜⬜⬜⬛🟦🟦⬛🟨🟨🟨🟨🟨🟨⬛⬛⬜⬜
        ⬜⬜⬛🟦🟦🟦⬛🟨⬛⬛🟨🟨🟨⬛🟦⬛⬜⬛🟦🟦🟦⬛⬛⬛⬛🟨🟨🟨⬛🟦⬛⬜
        ⬜⬜⬛🟦🟦⬛🟨⬛⬛⬛⬛🟨🟨🟨⬛⬛⬜⬛🟦🟦⬛🟨⬛⬛⬛⬛🟨🟨⬛🟦⬛⬜
        ⬜⬜⬛🟦🟦⬛🟨⬛⬛⬜⬛⬛🟨🟨⬛⬛⬜⬛🟦🟦⬛⬛⬛⬜⬛⬛🟨🟨🟨⬛⬛⬜
        ⬜⬜⬛🟦🟦⬛🟨⬛⬛⬜⬛⬛🟨🟨⬛⬛⬜⬛🟦🟦⬛⬛⬛⬜⬛⬛🟨🟨🟨⬛⬛⬜
        ⬜⬜⬛🟦🟦⬛🟨⬛⬛⬜⬛⬛🟨🟨⬛⬛⬜⬛🟦🟦⬛⬛⬛⬜⬛⬛🟨🟨🟨⬛⬛⬜
        ⬜⬜⬛🟦🟦⬛🟨⬛⬛⬜⬛⬛🟨🟨⬛🟦⬛⬛⬛🟦⬛⬛⬛⬜⬛⬛🟨🟨🟨⬛⬛⬜
        ⬜⬜⬛🟦🟦⬛🟨⬛⬛⬛⬛⬛🟨🟨⬛🟦🟦🟦🟦⬛⬛🟨⬛⬛⬛🟨🟨🟨🟨⬛⬛⬜
        ⬜⬜⬛🟦🟦⬛🟨⬛⬛⬛⬛🟨🟨🟨⬛🟦🟦🟦🟦⬛🟦⬛⬛⬛⬛🟨🟨🟨🟨⬛⬛⬜
        ⬜⬜⬜⬛🟦⬛🟨🟨⬛⬛🟨🟨🟨🟨⬛⬛🟦🟦🟦🟦⬛⬛🟨⬛🟨🟨🟨🟨⬛⬛⬜⬜
        ⬜⬜⬜⬛🟦🟦⬛🟨🟨🟨🟨🟨🟨⬛🟦🟦⬛🟦🟦🟦⬛⬛🟨🟨🟨🟨🟨🟨⬛⬛⬜⬜
        ⬜⬜⬛🟦⬛🟦🟦⬛🟨🟨🟨🟨🟨⬛🟦🟦⬛⬛⬛🟦🟦🟦⬛⬛⬛🟨🟨⬛🟦🟦⬛⬜
        ⬜⬛🟦🟦🟦🟦🟦🟦⬛🟨🟨🟨⬛🟦🟦⬛⬜⬜⬜⬛🟦⬛⬜⬜⬜⬛⬛🟦🟦🟦⬛⬜
        ⬛🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛⬛🟦🟦⬛⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬛🟦🟦🟦🟦⬛
        ⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟦🟦🟦🟦⬛
        ⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟦🟦🟦🟦⬛
        ⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜⬛🟦🟦🟦🟦🟦⬛
        ⬜⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛⬜⬜⬜⬛🟦⬛⬛⬛⬛🟦🟦🟦🟦🟦🟦⬛
        ⬜⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛⬜
        ⬜⬜⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛⬛🟦🟦🟦🟦🟦🟦🟦⬛⬜⬜
        ⬜⬜⬜⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛⬛🟦🟦🟦⬛⬛🟦🟦🟦🟦⬛⬜⬜⬜
        ⬜⬜⬜⬜⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛🟦🟦🟦🟦🟦🟦🟦🟦⬛🟦🟦⬛⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬛⬛⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛⬜⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜
        """)

    elif (pokemon_level >= 5) and (pokemon_level < 10):
        print ("""
        Your pokemon is Frogadier!
        ⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬛🟦🟨🟦⬛⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜
        ⬜⬜⬜⬛🟨🟨🟦🟦⬛⬛🟨🟦🟦⬛⬜⬜⬜⬜
        ⬜⬜⬜⬛🟨⬛🟦🟦⬛🟨🟨🟨🟦⬛⬜⬜⬜⬜
        ⬜⬜⬛⬛🟨⬛🟦🟦⬛🟨⬛🟨🟦⬛⬛⬛⬜⬜
        ⬜⬛🟦🟦🟦🟨🟦🟦⬛🟨⬛🟨🟦⬛⬜⬜⬛⬜
        ⬜⬛🟦⬜⬜🟦🟦🟦🟦🟨🟨🟨🟦⬛⬜⬜⬜⬛
        ⬜⬜⬛⬜⬜🌫️⬜⬜🟦🟦🟨🟦🟦🟦⬛⬜⬜⬛
        ⬜⬜⬛⬛🟦🟦⬜⬜🟦🟦🟦🟦🟦🟦⬛⬜🌫️⬛
        ⬜⬜⬜⬛⬛⬛🟦🟦🟦🟦🟦⬛⬛⬛🌫️⬛⬛⬜
        ⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛🌫️⬛🌫️🌫️🌫️⬛⬜
        ⬜⬜⬜⬜⬛🟦⬛🌫️🌫️🌫️🌫️⬛🟦⬛🌫️⬛⬜⬜
        ⬜⬜⬜⬛🟦⬛🟦⬛🌫️🌫️⬛⬛🟦⬛⬛⬜⬜⬜
        ⬜⬛⬛🌫️🌫️⬛⬛🟦⬜⬜🟦⬛🟦🟦⬛⬛⬜⬜
        ⬛⬜🌫️🌫️⬛🟦🟦⬛🟦🟦🟦🟦⬛🟦⬛⬜⬛⬜
        ⬜⬛⬛⬜⬛⬛⬛⬜⬛⬛⬛🟦⬛⬜⬛⬜⬛⬜
        ⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬛⬛🌫️🌫️⬛⬜⬜
        ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬛⬜⬜⬛⬜
        ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜
        """)

    else:
        print("""
        Your pokemon is Greninja!
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠂⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⡠⠔⢲
    ⠀⠀⠀⠀⡠⠒⠈⠉⠀⠒⠠⢀⠀⠀⠀⠀⠀⠀⠑⡀⠑⠀⠀⠀⠀⠀⢶⡄⠀⠀⠀⠀⠀⣄⠈⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⠾⠖⠚⠁
    ⠀⠀⠀⠐⡀⠀⠀⠀⠀⠀⠀⠀⠉⠢⣀⠀⠀⠀⠀⠈⢄⠀⠈⢂⠀⠀⢸⠹⣄⢀⡠⠔⠊⠉⢰⠃⠀⠀⠀⡀⠤⠤⢀⡀⢀⣀⣠⢴⣿⣛⣉⣀⡼⠤⠤⣄
    ⠀⠀⠀⠀⠈⠁⠒⠂⠀⠀⠐⠢⢄⡀⠀⠑⠤⣀⠀⠀⠀⠣⡀⠈⡉⠉⠉⢡⠈⠇⠀⠀⠀⣤⠏⠀⢀⡴⢏⣀⣀⡤⢖⡫⠔⠚⠉⠉⠉⠉⠉⠉⠉⠛⠋⠁
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⢄⡀⠀⠉⠐⠒⠒⠒⡄⢣⠄⠒⠉⠀⠀⠉⠑⠒⠻⠖⠚⢉⠤⠐⠶⠒⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠒⠒⠒⡎⠙⢧⢸⠶⡶⢤⡀⠀⢠⠖⢉⣇⣠⠔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡇⡀⢨⣿⣷⣤⠃⠀⠘⢳⣾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⠀⠗⢶⡀⠙⠿⠙⢢⣰⣴⣊⣜⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⢴⡾⠻⣧⠈⠛⠒⠢⠄⠴⡿⣻⠟⠉⠘⡄⠀⠉⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠜⠁⠀⢨⠇⢠⠏⠉⠃⠀⠀⠀⣸⠟⠁⠀⠀⠀⠈⠲⢤⡠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣀⣀⠤⠋⠀⡿⡀⠀⢠⡆⣠⡰⠁⠀⠀⠀⠀⠀⠀⢀⡴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⢋⡠⠴⣄⠀⠀⠀⢡⠙⠉⠁⡛⣩⠤⢤⠀⠀⣤⠔⠒⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠴⢋⣴⠯⠀⠀⠀⠉⠉⠒⢚⡆⠀⡋⠛⠁⠀⢘⡄⠐⠘⠿⢶⣤⠤⠤⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⣀⣀⣤⣴⣖⠉⡤⠚⠉⠀⠀⠀⠀⠀⠀⣀⣴⠿⣷⡗⢷⣄⠀⠀⠻⠔⠚⠋⠁⠀⠈⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠞⣉⣉⠽⠏⠁⠤⣴⠊⠈⣳⠄⠀⠀⢀⣀⣀⠤⣾⠛⠁⣰⡏⡁⠀⢙⡿⠢⠤⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠐⠧⠤⠤⠤⠋⢹⠋⠁⠀⣙⠇⠀⠑⠀⠀⠐⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")


def train():
    print("Your pokemon did 10 pushups!")
    global pokemon_level
    pokemon_level = pokemon_level + 1
    print("Congrats, your pokemon leveled up! Your pokemon is now at level " + str(pokemon_level))
    global day
    day = day + 1

def gym_battle():
    global pokemon_level
    global day
    day = day + 1
    print("Today you will have a gym battle!!!")
    outcome = random.randint(1,2) #50% chance to win or lose
    if outcome == 1:
        print("OH NOOO, your pokemon lost this battle. Your pokemon did not level up :( )")
    else:
        print("CONGRATS! Your pokemon won this battle :)")
        pokemon_level = pokemon_level + (random.randint(0,5))
        print("The battle has now finished. Your pokemon is now at level " + str(pokemon_level))

def display_pokemon():
    print("Today your pokemon will rest :)")
    print("Meanwhile, take a look at some stats!")
    global day
    day = day + 1
    print("Your pokemon is at level " + str(pokemon_level) + " and it is day " + str(day) + "!")
    draw_pokemon()

def evolve_pokemon():
    global pokemon_name
    if pokemon_level < 5 :
        pokemon_name = "Froakie"
    elif pokemon_level >= 5 and pokemon_level < 10:
        pokemon_name = "Frogadier"
        print("Your pokemon evolved into " + pokemon_name + "!!!")
    else:
        pokemon_name = "Greninja"
        print("Your pemon evolved into " + pokemon_name + "!!!")

def pokemon_game():
    global day
    while True:
        print("Welcome to Pokemon Evolution. Today is day " + str(day))
        print("Select an activity for the day")
        print("""
        1. Train
        2. Gym Battle
        3. Rest (Display info)
        4. Quit)
              """)

        activity = int(input("(1-5)Activity: "))

        if activity == 1:
            train()
            draw_pokemon()
        if activity == 2:
            gym_battle()
            draw_pokemon()
        if activity == 3:
            display_pokemon()
        if activity == 4:
           day = day + 1
           print("Thank you for playing the game! Play again soon!")
           break


#Main
pokemon_game()

