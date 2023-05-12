parking_lot = {
    'Level A': {
        'spaces': 20,
        'occupancy': 0,
        'vehicles': [],
    },
    'Level B': {
        'spaces': 20,
        'occupancy': 0,
        'vehicles': [],
    }
}

def assign_parking_space(vehicle_number):
    # get the current occupancy of each level
    level_a_occupancy = parking_lot['Level A']['occupancy']
    level_b_occupancy = parking_lot['Level B']['occupancy']

    # check if level A is full
    if level_a_occupancy == 20:
        # if it is, assign the space to Level B
        parking_spot = level_b_occupancy + 21
        parking_lot['Level B']['occupancy'] += 1
        parking_lot['Level B']['vehicles'].append(vehicle_number)
    
    elif level_a_occupancy == 20 and level_b_occupancy == 20:
        print("Parking is Full and not available")

    else:
        # otherwise, assign the space to Level A
        parking_spot = level_a_occupancy + 1
        parking_lot['Level A']['occupancy'] += 1
        parking_lot['Level A']['vehicles'].append(vehicle_number)

        return {'level': 'A' if parking_spot <= 20 else 'B', 'spot': parking_spot}


def find_parking_spot(vehicle_number):
    # search for the vehicle number in the parking lot
    for level, info in parking_lot.items():
        if vehicle_number in info['vehicles']:
            # if found, return the corresponding spot number
            return {'level': level[-1], 'spot': info['vehicles'].index(vehicle_number) + 1}
        
    return None

while True:
   print("Parking Lot")
   print("1. Park Car")
   print("2. Find Car ")
   option=int(input("Please Type 1 or 2 to choose from above options"))

   if(option == 1 ):
      vehicle_number= str(input("Please enter the number of car you want to park:"))
      assign_parking_space(vehicle_number)    
      print("car Parked Successfully")

   elif(option == 2):
      vehicle_number= input("Please enter the number of car you want to find:")
      print("Your car is parked at " + str(find_parking_spot(vehicle_number)))




