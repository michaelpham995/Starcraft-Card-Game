#This file will be the player buying stuff and moving troops

from mapChecker import get_game_grid, check_build_noncommand_structures, check_build_command_structure, check_home_base_build_structure, check_player_troops

def main():
    #Below are the card decks players will be able to select from 
    protoss_cards = [("Zealot", 19, 100, 1, 100, 1), ("Stalker", 10, 160, 1, 125, 1), ("High Templar", 4, 80, 1, 150, 1), ("Immortal", 20, 300, 1, 275, 1), ("Colossus", 10, 350, 1, 350, 1), ("Void Ray", 17, 250, 0, 250, 1), ("Carrier", 40, 450, 2, 500, 1)]
    zerg_cards = [("Zergling", 10, 35, 0, 25, 1), ("Baneling", 25, 35, 0, 50, 1), ("Roach",11, 145, 1, 75, 1), ("Hydralisk", 20, 90, 0, 100, 1), ("Ravager", 14, 120, 1, 125, 1), ("Mutalisk", 12, 120, 0, 150, 1)]
    terran_cards = [("Marine", 11, 45, 0, 50, 1), ("Marauder", 9, 125, 1, 100, 1), ("Hellion", 5, 90, 0, 100, 1), ("Siege Tank", 20, 175, 1, 150, 1), ("Thor", 60, 400, 1, 450, 1), ("Medivac", 0, 150, 0, 100, 1), ("Viking", 15, 135, 0, 150, 1), ("Battlecrusier", 45, 550, 3, 550, 1)]

    #Below initializes the troop map setup
    player1_troops = [[0]] * 100
    player2_troops = [[0]] * 100

    print(player1_troops)

    #Below initializes player starting configurations
    #Index 0 - Name
    #Index 1 - Minerals
    #Index 2 - Troops remaining
    player1_config = ["Name", 1000, 195]
    player2_config = ["Name", 1000, 195]

    #Note troops total is 200  but players start with 5 builders each
    #Max 1 builder per command center for resource collection
    #No rebuilds at the moment
    #Builders collect 20 minerals per move EACH
    #Builders will spawn with command centers and die with command centers



    choices = {"protoss": protoss_cards, "zerg": zerg_cards, "terran": terran_cards}

    p1_choice = None
    p2_choice = None

    #Below players input their names
    name1 = input("Player 1 enter your name!")
    player1_config[0] = name1

    name2 = input("Player 2 enter your name!")
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

    #The winner checker in this while loop is checking whether or not the persons starting 10 building have been destroyed, meaning if they have other bases out there but their starting base is destroyed, they lose the game!
    while (game_map[0][0] != 0 or game_map[1][0] != 0 or game_map[2][0] != 0 or game_map[3][0] != 0 or game_map[4][0] != 0 or game_map[5][0] != 0 or game_map[6][0] != 0 or game_map[7][0] != 0 or game_map[8][0] != 0 or game_map[9][0] != 0) and (game_map[0][-1] != 0 or game_map[1][-1] != 0 or game_map[2][-1] != 0 or game_map[3][-1] != 0 or game_map[4][-1] != 0 or game_map[5][-1] != 0 or game_map[6][-1] != 0 or game_map[7][-1] != 0 or game_map[8][-1] != 0 or game_map[9][-1] != 0):
        turn_count += 1

        #The turns will simulataneously be played in terms of response for game purposes, we will have player 1 go first

        #Map indexes for starting:
        # [0][0] and [1][0] are for troops
        # [2][0] and [3][0] and [4][0] and [6][0] and [7][0] are just command center like buildings
        # [8][0] and [9][0] are for troops

        player_turn(player1_config, p1_choice, player1_troops, game_map)
        player_turn(player2_config, p2_choice, player2_troops, game_map)

        def player_turn(player_config, race_choice, players_troops, game_map):
            print(player_config[0] + "currently you have" + str(player_config[1]) + "minerals and have room to build" + str(player_config[2]) + "more troops!")

            #Create a temporary list to keep track of troops player would like to buy this turn
            buy_troops = []

            continue_buy = "yes"
            while continue_buy == "yes":
                
                continue_buy = input("Enter 'yes' if you want to continue buying more troops")




main()