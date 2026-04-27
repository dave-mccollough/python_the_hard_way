# Exercise 5: More variables and printing

my_name = "Dave McCollough"
my_age = 21
my_height = 71 # Inches
my_weight = 200 # Lbs
my_eyes = "Green"
my_teeth = "White"
my_hair = "Nonexistant"

print(f"Lets talk about {my_name}.")
print(f"I'm {my_height} inches tall.")
print(f"I weight {my_weight}")
print(f"My eyes are {my_eyes} and my hair is {my_hair}")
print(f"My teeth are usually {my_teeth} depending on coffee consumption")

total = my_age + my_height + my_weight
print(f"if I add {my_age}, {my_height}, and {my_weight}, I get {total}")

# Study Drills

# Remove my_
name = "Dave McCollough"
age = 21
height = 71 # Inches
weight = 200 # Lbs
eyes = "Green"
teeth = "White"
hair = "Nonexistant"

print(f"Lets talk about {name}.")
print(f"I'm {height} inches tall.")
print(f"I weight {weight}")
print(f"My eyes are {eyes} and my hair is {hair}")
print(f"My teeth are usually {teeth} depending on coffee consumption")

total = age + height + weight
print(f"if I add {age}, {height}, and {weight}, I get {total}")

# Convert to centimeters and KG

# 1 inch = 2.54 cm
# 1 lb = 0.453592 kg
name = "Dave McCollough"
age = 21
height = 71 # Inches
weight = 200 # Lbs
eyes = "Green"
teeth = "White"
hair = "Nonexistant"

height = round(height * 2.54, 2)
age = round(age * 2.54, 2)
weight = round(weight * 0.453592, 2)

print(f"Lets talk about {name}.")
print(f"I'm {height} centimeters tall.")
print(f"I weight {weight} kg")
print(f"My eyes are {eyes} and my hair is {hair}")
print(f"My teeth are usually {teeth} depending on coffee consumption")

total = age + height + weight
print(f"if I add {age}, {height}, and {weight}, I get {round(total, 2)}")

