# Furniture.py - This program calculates profits and sales prices for a furniture company.

itemName = "TV Stand"
retailPrice = 325.00
wholesalePrice = 200.00
profit = retailPrice - wholesalePrice
# The 81.25 is the 25% deducted from the retail price
salePrice = retailPrice - 81.25
saleProfit = salePrice - wholesalePrice


# Write your assignment statements here for profit, salePrice, and saleProfit

print("Item Name: " + itemName)
print("Retail Price: $" + str(retailPrice))
print("Wholesale Price: $" + str(wholesalePrice))
print("Profit: $" + str(profit))
print("Sale Price: $" + str(salePrice))
print("Sale Profit: $" + str(saleProfit))