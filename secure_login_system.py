#Diana Reyes Tamayo
#12/5
#Secure Login System

#Init

#Functions
def login():
    # Hardcoded valid username and password (modify these)
    valid_username = "theuser1"
    valid_password = "Baddie#5"

    # Get user input for username and password
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")


    if username == valid_username and password == valid_password:
        print("You have sucessfully logged into your account!")

    # Convert the entered username to lowercase or uppercase by using a method for case-insensitive comparison
    username = "theuser1"
    username = username.lower()
    username = username.upper()
    # Check if the entered username and password match the valid credentials
    if username == valid_username or username and password == valid_password:
        print("login successful")
    else:
        print("login unsuccessful")
# Call the function to check credentials
login()
