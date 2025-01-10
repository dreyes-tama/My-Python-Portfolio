#Diana Reyes Tamayo
#12/10
#MadLibs

#Init

#functions
adjective = ''
clothing = ''
emotion = ''
animal = ''
sound = ''
sport = ''
animal2 = ''
number = ''
number2 = ''

def Intro():
    global adjective

    global clothes

    global emotion

    global animal

    global sound

    global sport

    global animal2

    global number

    global number2

    print("Welcome to MadLib! Today you will be entering responses to generate your unique MadLib :)")
    print("Make sure to answer the prompts as requested.")

    adjective = input('Enter an adjective: ')
    clothes = input('Enter an article of clothing: ')
    emotion = input('Enter an emotion: ')
    animal = input('Enter an animal: ')
    animal2 = input('Enter a second animal: ')
    sound = input ('Enter a sound: ')
    number = int(input('Enter a number: '))
    number2 = int(input('Enter a second number: '))
    sport = input('Enter a sport: ')

def madLib():
    Intro()
    print("Once upon a time, a long long time ago, begins the story of a " + animal + ". This " + animal + " was well known for being very active and was the best at playing "
    + sport + ". One day a " + animal2 + " challenged " + animal + " to a match. " + animal + " felt " + emotion + ". To prepare for the match, " + animal + " then proceeded to change into their favorite "
    + clothes + ". The match finished and " + animal + " beat " + animal2 + " "+ str(number) + " times. To celebrate, " + animal + " did " + str(number2) + " cartwheels and said " + sound + "!!! Since then, all the other animals described " +
    animal + " as " + adjective + ".")

#Main
madLib()
