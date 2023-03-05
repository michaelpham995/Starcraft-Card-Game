#This function will allow user to choose new coordinates for troops to move towards
def choose_troop_movements(army, name):
    print(str(name) + " here are your troops you can move!")
    print()

    #Here we print out army for user to see
    for troop in range(len(army)):
        print("Troop Name: " + str(army[troop][0]))
        print("Current Coordinates: [" + str(army[troop][5]) + ", " + str(army[troop][6]) + "]")
        print("Troop Moving Towards: [" + str(army[troop][7]) + ", " + str(army[troop][8]) + "]")
        print("Troop Army Index: " + str(troop))
        print("-------------------------")

    #Here we choose where to move troops
    continue_moving = input("Type 'y' if you want to choose troop to move! ")
    while continue_moving == "y":
        troop_to_move = input("Please enter the index of the troop you want to move! ")
        while troop_to_move.isnumeric() != True:
            troop_to_move = input("Please enter the index of the troop you want to move! ")
        while int(troop_to_move) < 0 or int(troop_to_move) >= len(army):
            troop_to_move = input("Please enter an index between 0 and " + str(len(army) - 1))
        
        #Choose x coordinate
        x_axis = input("Please enter the x coordinate between 0 and 9! ")
        while x_axis.isnumeric() != True:
            x_axis = input("Please enter an integer for the x coordinate! ")
        while int(x_axis) < 0 or int(x_axis) > 9:
            x_axis = input("Please enter an integer between 0 and 9! ")
        
        #Choose y coordinate
        y_axis = input("Please enter the y coordinate between 0 and 9! ")
        while y_axis.isnumeric() != True:
            y_axis = input("Please enter an integer for the y coordinate! ")
        while int(y_axis) < 0 or int(y_axis) > 9:
            y_axis = input("Please enter an integer between 0 and 9! ")

        #Update the coordinates of army
        army[int(troop_to_move)][7] = int(x_axis)
        army[int(troop_to_move)][8] = int(y_axis)

        #See if you want to move more troops
        continue_moving = input("Type 'y' if you want to continue choosing troops to move! ")

    return

#This functions prints army list for when user purchases troop
def print_race(army_choice):

    print("Here is a list of troops you can purchase!")
    print()

    for troop in range(len(army_choice)):
        print("Name: " + str(army_choice[troop][0]))
        print("Attack: " + str(army_choice[troop][1]))
        print("Health: " + str(army_choice[troop][2]))
        print("Minerals Cost: " + str(army_choice[troop][3]))
        print("Unit Count: " + str(army_choice[troop][4]))
        print("Index to Order: " + str(troop))
        print("------------------------")

    return
