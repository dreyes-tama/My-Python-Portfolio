#Guessing Game
import random
#difficulty
#Try Again
#too high and too low (hot and cold)

print("Welcome to GUESSING GAME!")
print("To play all you have to do is guess what number I am thinking of.")
print("Choose what difficulty you would like to play at.")

answer1 = random.randint(1,5)
answer2 = random.randint(1,30)
answer3 = random.randint(1,100)

ans = input("Would you like to choose easy, medium, or hard?")

if ans == "easy":
        ans = input("please guess a number from 1-5.")
        if ans > str(answer1):
            print("Oh nooo, that guess is too high!")
        elif ans < str(answer1):
            print("oh nooo, that guess is too low!")
        elif ans == str(answer1):
            print("congratulations you are correct :).")
        else:
            print("That is not the number I was thinking of :(. The correct answer was " + str(answer1) + ".")

if ans == "medium":
        ans = input("Please guess a number from 1-30.")
        if ans > str(answer2):
            print("Oh nooo, that guess is too high!")
        elif ans < str(answer2):
            print("oh nooo, that guess is too low!")
        elif ans == str(answer2):
            print("congratulations you are correct :).")
        else:
            print("That is not the number I was thinking of :(. The correct answer was " + str(answer2) + ".")

if ans == "hard":
        ans = input("please guess a number from 1-100.")
        if ans > str(answer3):
            print("Oh nooo, that guess is too high!")
        elif ans < str(answer3):
            print("oh nooo, that guess is too low!")
        elif ans == str(answer3):
            print("congratulations you are correct :).")
        else:
            print("That is not the number I was thinking of :(. The correct answer was " + str(answer3) + ".")

