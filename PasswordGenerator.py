import random  # Import the random module for generating random numbers
import math

def generate_password(length):
    # Initialize an empty string for the password
    password = ""

    # Define the character pool for generating the password
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

    for i in range(length):
        # Generate a random index to select a character from the character pool
        random_index = math.floor(random.random() * len(characters))

        # Append the selected character to the password
        password += characters[random_index]

    # Return the generated password
    return password

# Prompt the user to enter the desired password length
password_length = int(input("Enter password length: "))

# Generate a password of the specified length
generated_password = generate_password(password_length)

# Display the generated password
print("Your password is:", generated_password)