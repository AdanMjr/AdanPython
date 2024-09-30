"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
charge = 0.00
numChars = 8
color = "gold"
woodType = "oak"

# Charge for this sign.
charge = 35

# Number of characters.
if numChars > 5:
    additional_chars = numChars - 5
    charge += additional_chars * 4
    
# Color of characters.
if color == "gold":
    charge += 15
    
# Type of wood.
if woodType == "oak":
    charge += 20

# Write assignment and if statements here as appropriate.

# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))