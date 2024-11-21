# I needed a lot of help from AI for this part but It is actually helping me understand more the more I use it
# Define the filename where the vehicle list will be stored
filename = 'authorized_vehicles.txt'

def load_from_file(filename):
    """Loads vehicles from the file into the AllowedVehiclesList."""
    try:
        with open(filename, 'r') as file:
            return file.read().splitlines()  # Read file and split by newlines
    except FileNotFoundError:
        return []  # Return an empty list if the file does not exist

def save_to_file(AllowedVehiclesList, filename):
    """Saves the AllowedVehiclesList to the file."""
    with open(filename, 'w') as file:
        for vehicle in AllowedVehiclesList:
            file.write(vehicle + '\n')
AllowedVehiclesList = [
    'Ford F-150', 
    'Chevrolet Silverado', 
    'Tesla CyberTruck', 
    'Toyota Tundra', 
    'Rivian R1T',
    'Ram 1500'
]
# The menu is basically the same as 0-1 just the change in 2 and addition of 3 and the input of the full name of the vehicle
def Onload():
    print("********************************")
    print("AutoCountry Vehicle Finder v0.4")
    print("********************************")
    print("Please Enter the following number below from the following menu:")
    
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. DELETE Authorized Vehicle")
    print("5. Exit")
    print("********************************")
# to turn all of the events into functions all I did was use def and made a name for the functions and just added the code from before to define each function
def Printall():
    # input 1 is the same as the 0-1 project assignment
    user_input = input("Enter Your Choice: ")
    if user_input == "1":
        print("The AutoCountry sales manager has authorized the purchase of the following Vehicles: ", AllowedVehiclesList)
        
    

def Searchforvehicle():
    # for input 2 I used AI to help me but it did help me understand what I was programming and I changed it to elif to allow multiple conditions
    user_input = input("Enter Your Choice: ")
    if user_input == "2":
        vehicle_to_search = input("Please Enter the full Vehicle name: ").strip()
        if vehicle_to_search in AllowedVehiclesList:
            print(vehicle_to_search, "is an authorized vehicle")
        else:
            print(vehicle_to_search, "is not an authorized vehicle, if you received this in error please check the spelling and try again")
        

def Addvehicle():
    # for input 3 I used AI to help me but Im getting the hang of it 
    user_input = input("Enter Your Choice: ")
    if user_input == "3":
        new_vehicle = input("Please Enter the full Vehicle name you would like to add: ").strip()
        if new_vehicle in AllowedVehiclesList:
            print(new_vehicle, "is already authorized.")
        else:
            AllowedVehiclesList.append(new_vehicle)
            print(new_vehicle, "has been added to the authorized list." )

        
def Deletevehicle():
    user_input = input("Enter Your Choice: ")
    if user_input == "4":
        vehicle_to_remove = input("Please Enter the full Vehicle name you would like to REMOVE: ").strip()
        if vehicle_to_remove in AllowedVehiclesList:
            conformation = input(f"Are you sure you want to remove {vehicle_to_remove} from the Authorized Vehicles List?")
            if conformation == "yes":
                AllowedVehiclesList.remove(vehicle_to_remove)
                print("You have REMOVED", vehicle_to_remove, "as an authorized vehicle")
            else:
                print("No changes were made")
        
def Exit():
    user_input = input("Enter Your Choice: ")
    if user_input == "5":
        print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")

def Main():
    while True:
        Onload()
        user_input = input("Enter Your Choice: ")
        if user_input == "1":
            Printall()
        elif user_input == "2":
            Searchforvehicle()
        elif user_input == "3":
            Addvehicle()
        elif user_input == "4":
            Deletevehicle()
        elif user_input == "5":
            Exit()
        else:
            print("Invalid choice. Please try again.")
            
            
Main()