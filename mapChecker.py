#Michael 2/15 EDIT
#Build grid functions/establish map capability with the functions below
def get_game_grid():
    map_array = [[100, 0, 0, 0, 0, 0, 0, 0, 0, 100], [100, 0, 0, 0, 0, 0, 0, 0, 0, 100], [100, 0, 0, 0, 0, 0, 0, 0, 0, 100]
    ,[100, 0, 0, 0, 0, 0, 0, 0, 0, 100], [100, 0, 0, 0, 0, 0, 0, 0, 0, 100], [100, 0, 0, 0, 0, 0, 0, 0, 0, 100], [100, 0, 0, 0, 0, 0, 0, 0, 0, 100]
    , [100, 0, 0, 0, 0, 0, 0, 0, 0, 100], [100, 0, 0, 0, 0, 0, 0, 0, 0, 100], [100, 0, 0, 0, 0, 0, 0, 0, 0, 100]]

    return map_array

#Here we update how many minerals a player can receive next round based on their current structures that have not fallen
def check_mineral_buildings(game_map, player):
    mineral_producers_remaining = 0
    if player == "P1":
        if game_map[2][0] > 0:
            mineral_producers_remaining += 1
        if game_map[3][0] > 0:
            mineral_producers_remaining += 1
        if game_map[4][0] > 0:
            mineral_producers_remaining += 1
        if game_map[5][0] > 0:
            mineral_producers_remaining += 1
        if game_map[6][0] > 0:
            mineral_producers_remaining += 1
        if game_map[7][0] > 0:
            mineral_producers_remaining += 1

    elif player == "P2":
        if game_map[2][-1] > 0:
            mineral_producers_remaining += 1
        if game_map[3][-1] > 0:
            mineral_producers_remaining += 1
        if game_map[4][-1] > 0:
            mineral_producers_remaining += 1
        if game_map[5][-1] > 0:
            mineral_producers_remaining += 1
        if game_map[6][-1] > 0:
            mineral_producers_remaining += 1
        if game_map[7][-1] > 0:
            mineral_producers_remaining += 1

    return (mineral_producers_remaining * 17)

#This function is responsible for checking if a player has an active barracks to recruit troops
def check_troop_buildings(game_map, player):
    if player == "P1":
        if game_map[0][0] > 0 or game_map[1][0] > 0 or game_map[8][0] > 0 or game_map[9][0] > 0:
            return True
        else:
            return False

    elif player == "P2":
        if game_map[0][-1] > 0 or game_map[1][-1] > 0 or game_map[8][-1] > 0 or game_map[9][-1] > 0:
            return True
        else:
            return False
    

#Unfinished function
def check_player_troops(player1_troops, player2_troops, xcoord, ycoord):
    if player2_troops[xcoord * 10 + ycoord] != []:
        return "The opposing player has troops here!"
    else:
        return "There are no opposing troops here!"
