# Asking user for inputs of name, location, dream car & favprite statement
name = input("What is your name?: ")
location = input("Where do you live?: ")
car = input("What is your dream car?: ")
mantra = input("What is your favorite saying?: ")

intro = f"My name is {name}, I stay at {location}, my dream car is the {car} and my favorite \n statemnt is {mantra}"
# Combining user input to create an introductory statement for the user.
print("\n"+intro+"\n")



# Printing the introductory statement in lowercase
print(intro.lower())

# Printing the introductory statement in uppercase
print(intro.upper()+"\n")

# Checking the length of the introductory statement
print(len(intro))
print("The length of the text is "+str(len(intro)))

# Finding the letter "A" in the introductory statement
intro.find("A")
print("Is there letter A in the text? ", str(intro.find("A")))