#This file will be the player buying stuff and moving troops

from mapChecker import get_game_grid, check_build_noncommand_structures, check_build_command_structure, check_home_base_build_structure, check_player_troops
from resourceChecker import check_enough_minerals, check_enough_space
from battles import is_there_conflict, battle
from moveAndPrint import choose_troop_movements, print_race
from attackStructures import check_buildings, attack_buildings

def main():
    #Below are the card decks players will be able to select from 
    protoss_cards = [["Zealot", 19, 100, 100, 1, 0, 0, 0, 0], ["Stalker", 10, 160, 125, 1, 0, 0, 0, 0], ["High Templar", 4, 80, 150, 1, 0, 0, 0, 0], ["Immortal", 20, 300, 275, 1, 0, 0, 0, 0], ["Colossus", 10, 350, 350, 1, 0, 0, 0, 0], ["Void Ray", 17, 250, 250, 1, 0, 0, 0, 0], ["Carrier", 40, 450, 500, 1, 0, 0, 0, 0]]
    zerg_cards = [["Zergling", 10, 35, 25, 1, 0, 0, 0, 0], ["Baneling", 25, 35, 50, 1, 0, 0, 0, 0], ["Roach",11, 145, 75, 1, 0, 0, 0, 0], ["Hydralisk", 20, 90, 100, 1, 0, 0, 0, 0], ["Ravager", 14, 120, 125, 1, 0, 0, 0, 0], ["Mutalisk", 12, 120, 150, 1, 0, 0, 0, 0]]
    terran_cards = [["Marine", 11, 45, 50, 1, 0, 0, 0, 0], ["Marauder", 9, 125, 100, 1, 0, 0, 0, 0], ["Hellion", 5, 90, 100, 1, 0, 0, 0, 0], ["Siege Tank", 20, 175, 150, 1, 0, 0, 0, 0], ["Thor", 60, 400, 450, 1, 0, 0, 0, 0], ["Medivac", 0, 150, 100, 1, 0, 0, 0, 0], ["Viking", 15, 135, 150, 1, 0, 0, 0, 0], ["Battlecrusier", 45, 550, 550, 1, 0, 0, 0, 0]]

    #Below initializes the troop map setup
    player1_troops = []
    player2_troops = []

    print(player1_troops)

    #Below initializes player starting configurations
    #Index 0 - Name
    #Index 1 - Minerals
    #Index 2 - Troops remaining
        #I changed index 2 to 25 troops
    player1_config = ["Name", 1000, 25]
    player2_config = ["Name", 1000, 25]

    #Note troops total is 200  but players start with 5 builders each
    #Max 1 builder per command center for resource collection
    #No rebuilds at the moment
    #Builders collect 20 minerals per move EACH
    #Builders will spawn with command centers and die with command centers



    choices = {"protoss": protoss_cards, "zerg": zerg_cards, "terran": terran_cards}

    p1_choice = None
    p2_choice = None

    #Below players input their names
    name1 = input("Player 1 enter your name! ")
    player1_config[0] = name1

    name2 = input("Player 2 enter your name! ")
    player2_config[0] = name2


    #Below players input what race they want to choose
    input_p1 = input("Player 1 do you want to play as Zerg, Protoss, or Terran? ")
    while input_p1 not in choices.keys():
        input_p1 = input("Pleaes enter zerg, terran, or protoss: ")

    p1_choice = choices[input_p1]

    input_p2 = input("Player 2 do you want to play as Zerg, Protoss, or Terran? ")
    while input_p2 not in choices.keys():
        input_p2 = input("Pleaes enter zerg, terran, or protoss: ")

    p2_choice = choices[input_p2]

    #Importing game_map from the mapChecker.py file
    game_map = get_game_grid()

    game(player1_config, player2_config, p1_choice, p2_choice, player1_troops, player2_troops, game_map)



def game(player1_config, player2_config, p1_choice, p2_choice, player1_troops, player2_troops, game_map):

    turn_count = 0



    def player_turn(player_config, race_choice, player_choice, map):
        print(player_config[0] + ", currently you have " + str(player_config[1]) + " minerals and have room to build " + str(player_config[2]) + " more troops!")

        #Create a temporary list to keep track of troops player would like to buy this turn
        buy_troops = []

        #Remember: The order of a units attributes are the following
        #   Name
        #   Attack
        #   Health
        #   Cost
        #   Unit Cost
        #   Current x axis
        #   Current y axis
        #   Target x axis
        #   Target y axis

        continue_buy = input("Enter 'y' if you want to buy troops! ")
        while continue_buy == "y":
                
            print_race(race_choice)
            
            choose_unit = -1


            while type(choose_unit) != int or choose_unit < 0 or choose_unit >= len(race_choice):
                try:
                    choose_unit = int(input("Type index of unit that you want to recruit! ")) 
                except ValueError:
                    print("Please enter an integer in the range of the troop list")

                
        
            if check_enough_minerals(player_config, race_choice, choose_unit) and check_enough_space(player_config, race_choice, choose_unit):
                buy_troops.append(race_choice[choose_unit])
                #Reduce minerals
                player_config[1] -= race_choice[choose_unit][3]
                #Reduce remaining player space
                player_config[2] -= race_choice[choose_unit][4]
            
            elif check_enough_minerals(player_config, race_choice, choose_unit) and not check_enough_space(player_config, race_choice, choose_unit):
                print("You do not have enough remaining army space to purchase this unit")
            elif check_enough_space(player_config, race_choice, choose_unit) and not check_enough_minerals(player_config, race_choice, choose_unit):
                print("You do not havce enough minerals to purchase this unit")
            else:
                print("You do not have enough minerals to purchase this unit and you do not have enough remaining army space to purchae this unit.")

            continue_buy = input("Enter 'y' if you want to continue buying more troops and 'n' if you wish to stop! ")



        return buy_troops

    #This function adds troops to the map
    #If there is only one troop unit recruited, they will spawn at the uppermost point in the map
    #If there are multuple troop units recruited, half will spawn at the uppermost barracks and half at the lower barracks

    def add_troops_to_map(player_troops, new_troops, which_player):
        if len(new_troops) == 0:
            return
        elif len(new_troops) == 1 and which_player == "P1":
            for troop in range(len(new_troops)):
                new_troops[troop][5] = 0 
                new_troops[troop][6] = 0
                new_troops[troop][7] = 0
                new_troops[troop][8] = 0
        elif len(new_troops) == 1 and which_player == "P2":
            for troop in range(len(new_troops)):
                new_troops[troop][5] = 0 
                new_troops[troop][6] = -1
                new_troops[troop][7] = 0
                new_troops[troop][8] = -1
        elif len(new_troops) > 1 and which_player == "P1":

            #here we are adding the troops current location in the 5th/6th index of the troop unit in the list of army
            #Here we are also adding the 7th/8th index to be the target location of the unit

            low, high = 0, len(new_troops)
            mid = (low + high) // 2
            for troop in range(low, mid + 1):
                new_troops[troop][5] = 0
                new_troops[troop][6] = 0
                new_troops[troop][7] = 0 
                new_troops[troop][8] = 0

            for troop in range(mid + 1, high):
                new_troops[troop][5] = 1
                new_troops[troop][6] = 0
                new_troops[troop][7] = 1
                new_troops[troop][8] = 0



        elif len(new_troops) > 1 and which_player == "P2":
            low, high = 0, len(new_troops)
            mid = (low + high) // 2
            for troop in range(low, mid + 1):

                new_troops[troop][5] = 0
                new_troops[troop][6] = -1
                new_troops[troop][7] = 0
                new_troops[troop][8] = -1

                new_troops[troop][5] = 0
                new_troops[troop][6] = -1
                new_troops[troop][7] = 0 
                new_troops[troop][8] = -1 

            for troop in range(mid + 1, high):
                new_troops[troop][5] = 1
                new_troops[troop][6] = -1
                new_troops[troop][7] = 1
                new_troops[troop][8] = -1
    
        for troop in new_troops:
            player_troops.append(troop)



    def move_troops(player_army):
        for unit in player_army:
            if unit[-2] != unit[-4] or unit[-1] != unit[-3]:
                xdiff = unit[-2] - unit[-4]
                ydiff = unit[-1] - unit[-3]

                if xdiff == 0 and ydiff > 0:
                    unit[-3] += 1
                elif xdiff == 0 and ydiff < 0:
                    unit[-3] -= 1
                elif ydiff == 0 and xdiff > 0:
                    unit[-4] += 1
                elif ydiff == 0 and xdiff < 0:
                    unit[-4] -= 1
                elif ydiff > 0 and xdiff > 0:
                    unit[-4] += 1
                    unit[-3] += 1
                elif ydiff > 0 and xdiff < 0:
                    unit[-3] -= 1
                    unit[-4] += 1
                elif ydiff < 0 and xdiff > 0:
                    unit[-4] += 1
                    unit[-3] -= 1
                elif ydiff < 0 and xdiff < 0:
                    unit[-3] -= 1
                    unit[-4] -= 1



    #The winner checker in this while loop is checking whether or not the persons starting 10 building have been destroyed, meaning if they have other bases out there but their starting base is destroyed, they lose the game!
    while (game_map[0][0] != 0 or game_map[1][0] != 0 or game_map[2][0] != 0 or game_map[3][0] != 0 or game_map[4][0] != 0 or game_map[5][0] != 0 or game_map[6][0] != 0 or game_map[7][0] != 0 or game_map[8][0] != 0 or game_map[9][0] != 0) and (game_map[0][-1] != 0 or game_map[1][-1] != 0 or game_map[2][-1] != 0 or game_map[3][-1] != 0 or game_map[4][-1] != 0 or game_map[5][-1] != 0 or game_map[6][-1] != 0 or game_map[7][-1] != 0 or game_map[8][-1] != 0 or game_map[9][-1] != 0):
        turn_count += 1

        #The turns will simulataneously be played in terms of response for game purposes, we will have player 1 go first

        #Map indexes for starting:
        # [0][0] and [1][0] are for troops
        # [2][0] and [3][0] and [4][0] and [6][0] and [7][0] are just command center like buildings
        # [8][0] and [9][0] are for troops

        #Here players recruit troops
        newTroops_player1 = player_turn(player1_config, p1_choice, player1_troops, game_map)
        newtroops_player2 = player_turn(player2_config, p2_choice, player2_troops, game_map)

        #Here we add to troops to each of the players barracks that have been recruited
        add_troops_to_map(player1_troops, newTroops_player1, "P1")
        add_troops_to_map(player2_troops, newtroops_player2, "P2")


        #Test
        print(player1_troops)
    



        #Here we go to the battles.py file and see if there are any conflicts
        conflict_spots = is_there_conflict(player1_troops, player2_troops)
        print(conflict_spots)

        #If there are conflict spots the battle will be settled here
        if len(conflict_spots) > 0:
            for coords in conflict_spots:
                battle(player1_troops, player2_troops, coords)

        #NEXT STEP IS TO CHECK FOR BUILDINGS BEING DESTROYED

        #This is where players choose new coordinates for troops
        choose_troop_movements(player1_troops, player1_config[0])
        choose_troop_movements(player2_troops, player2_config[0])

        #Move troops by 1 'square' per move
        move_troops(player1_troops)
        move_troops(player2_troops)

        #Just a test
        print(player1_troops)
        
main()