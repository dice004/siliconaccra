# Take inputes froom the user as exam results
# Convert the inputs to floats and make provision to round decimal inputs
# Compare the user input wiith a range of a grading system 
# make a print Function to return a sentence to tell the user the grade they received



# Asking User for input on test scores
score = input("What was your test score for the assignment?: ")

# Converting and rounding up user input to better compare in the marking scheme
score = round(float(score))

print(score)

# Writing conditionals for better grade placement
if (100 >= score >= 80):
    print("You got an 'A' ")

elif (79 >= score >= 70):
    print("You got a 'B' ")

elif (69 >= score >= 60):
    print("You got a 'C' ")

elif (59 >= score >= 50):
    print("You got a 'D' ")

elif (49 >= score >= 40):
    print("You got an 'E' ")

else:
    print("You got an 'F' ")

