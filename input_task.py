print("What is your name?")

name = input()

print(f"It is nice to meet you {name}")



# Ask the user for their details
name = input("What is your name?\n")
age = int(input("How old are you (in years)?\n"))
height = float(input("How tall are you (in meters)?\n"))
weight = float(input("How much do you weigh (in kilograms)?\n"))

# Calculate BMI
bmi = weight / (height ** 2)

# Display the result
print(f"{name} you are {age} years old and your bmi is {bmi:.1f}.")
