# Meal calculator
# CSC500 - Criticial Assignment #3

# Ask for the charge for the food
charge = float(input("Enter the charge for the food: "))

# Calculate the tip (18%)
tip = charge * 0.18

# Calculate the tax (7%)
tax = charge * 0.07

# Calculate the total
total = charge + tip + tax

# Print out the Charge, Tip, Tax, and Total
print("Charge:  ${:.2f}".format(charge))
print("Tip:     ${:.2f}".format(tip))
print("Tax:     ${:.2f}".format(tax))
print()
print("Total:   ${:.2f}".format(total))
