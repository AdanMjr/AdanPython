AllowedVehiclesList = [
    'Ford F-150', 
    'Chevrolet Silverado', 
    'Tesla CyberTruck', 
    'Toyota Tundra', 
    'Nissan Titan',
    'Rivian R1T',
    'Ram 1500'
]
# The menu is basically the same as 0-1 just the change in 2 and addition of 3 and the input of the full name of the vehicle
def Onload():
    print("********************************")
    print("AutoCountry Vehicle Finder v0.2")
    print("********************************")
    print("Please Enter the following number below from the following menu:")
    
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. DELETE Authorized Vehicle")
    print("5. Exit")
    print("********************************")
 # input 1 is the same as the 0-1 project assignment
    user_input = input("Enter Your Choice: ")
    if user_input == "1":
        print("The AutoCountry sales manager has authorized the purchase of the following Vehicles: ", AllowedVehiclesList)
        Onload()
    # for input 2 I used AI to help me but it did help me understand what I was programming and I changed it to elif to allow multiple conditions
    elif user_input == "2":
        vehicle_to_search = input("Please Enter the full Vehicle name: ").strip()
        if vehicle_to_search in AllowedVehiclesList:
            print(vehicle_to_search, "is an authorized vehicle")
        else:
            print(vehicle_to_search, "is not an authorized vehicle, if you received this in error please check the spelling and try again")
        Onload()
        
# for input 3 I used AI to help me but Im getting the hang of it 
    elif user_input == "3":
        new_vehicle = input("Please Enter the full Vehicle name you would like to add: ").strip()
        if new_vehicle in AllowedVehiclesList:
            print(new_vehicle, "is already authorized.")
        else:
            AllowedVehiclesList.append(new_vehicle)
            print(new_vehicle, "has been added to the authorized list." )
        Onload()
    
# for input 4 I tried to use the understanding I already had and I completed most of it myself but AI was still used for small amounts of help
# this was to remove a vehicle from the allowed vehicle list
# I used the f-string for line 53 because it wouldn't include the spaces between the vehicle and the rest of the text
    elif user_input == "4":
        vehicle_to_remove = input("Please Enter the full Vehicle name you would like to REMOVE: ").strip()
        if vehicle_to_remove in AllowedVehiclesList:
            conformation = input(f"Are you sure you want to remove {vehicle_to_remove} from the Authorized Vehicles List?")
            if conformation == "yes":
                AllowedVehiclesList.remove(vehicle_to_remove)
                print("You have REMOVED", vehicle_to_remove, "as an authorized vehicle")
            else:
                print("No changes were made")
        Onload()
   
    elif user_input == "5":
        print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
Onload()