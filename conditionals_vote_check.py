#conditionals statements

#Init
#Functions
#vote check

def vote_check():
    age = int(input("Please enter your age:"))
    citizen = input("Are you a U.S. citizen?")

    if age >= 18 and citizen == "yes":
        print("You are eligible to vote!")
    else:
        print("You are NOT eligible to vote!")

#a = integer
#b = integer
#c = integer
#Must print the largest of the three
def max_num(a, b, c):
    #No input needed
    #Process data with conditional statements
    if a > b and a > c:
        print("a is the largest. The value of a is: " + str(a))
    if b > a and b > c:
        print("b is the largest. The value of b is: " + str(b))
    if c > b and c > a:
        print("c is the largest. The value of c is: " + str(c))

#score = integer
def score_to_grade(score):
    if score > 90:
        print("Your letter grade is A!")
    elif score >79:
        print ("Your letter grade is B!")
    elif score > 69:
        print ("Your letter grade is a C!")
    elif score > 59:
        print ("Your letter grade is D!")
    else:
        print("Your letter grade is F!")

#Main
score_to_grade(98)

#Boolean: True or False
#Boolean expression

de max_num(a,b,c)
#! = not Equal To

#Logic Operators
# and Both statements must be true
#or one of the statements must be true
