AllowedVehiclesList = [
    'Ford F-150', 
    'Chevrolet Silverado', 
    'Tesla CyberTruck', 
    'Toyota Tundra', 
    'Nissan Titan'
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
    print("4. Exit")
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
    

    elif user_input == "4":
        print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
        

Onload()