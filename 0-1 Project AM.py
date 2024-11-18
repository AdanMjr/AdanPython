# This is going to take me forever and I only have 6 days so let me lock in
# This is the Allowed Vehicles List
AllowedVehiclesList = [
    'Ford F-150', 
    'Chevrolet Silverado', 
    'Tesla CyberTruck', 
    'Toyota Tundra', 
    'Nissan Titan'
]

# I am trying to find a way to print a menu
def OnLoad():
    print("********************************")
    print("AutoCountry Vehicle Finder v0.1")
    print("********************************")
    print("Please Enter the following number below from the following menu:\n")
    print("1. PRINT all Authorized Vehicles")
    print("2. Exit")
OnLoad()
# I asked a good friend named AI for help just for that for right now I promise

# Now I must to add the input part
user_input = input("Enter Your Choice: ")
if user_input == "1":
    print("The AutoCountry sales manager has authorized the purchase of the following Vehicles: ", AllowedVehiclesList)

if user_input == "2":
    print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
# This honestly wasn't that hard to complete but I did need some help from AI but I only needed it for the menu and input
