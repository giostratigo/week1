# print("What is your name?")
#
# name = input()
#
# print(f"It is nice to meet you {name}")
#
#
#
# # Ask the user for their details
# name = input("What is your name?\n")
# age = int(input("How old are you (in years)?\n"))
# height = float(input("How tall are you (in meters)?\n"))
# weight = float(input("How much do you weigh (in kilograms)?\n"))
#
# # Calculate BMI
# bmi = weight / (height ** 2)
#
# # Display the result
# print(f"{name} you are {age} years old and your bmi is {bmi:.1f}.")


# Asking the user to enter character stats
lives = int(input("Please enter the number of lives.\n"))
energy = int(input("Please enter the energy level.\n"))
shield = int(input("Please enter the shield level.\n"))

# Display confirmation
print("Health has been set.\n")

# Display character status using symbols
print(f"Lives:  {'♥' * lives}")
print(f"Energy: {'♦' * energy}")
print(f"Shield: {'♦' * shield}")
