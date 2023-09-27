import random

# Names of everyone in class
class_list = ["Kristal", "Henry", "Dice", "Abena", "Precious", "Nehemia", "Praise", "Caleb", "Maya", "Stanley", "Pee", "Shekwonya"]

print("\n\nClass list before Shuffle. ")
for i in range(0, len(class_list)):
    print(class_list[i])

# Shuffle the class list
print("\n\nClass List after Shuffle")
random.shuffle(class_list)
for item in class_list:
    print(item)

print("\n\nRandomly selected student name")
print(random.choice(class_list))

# Adding three more names
print("\nNew List of names after adding new names")
class_list.extend(["Hugo", "Saint", "Mario"])

# Shuffle Student Name List After Adding the new names
random.shuffle(class_list)
for names in class_list:
    print(names)
print("\n\nNewly Selected name")
print(random.choice(class_list))
