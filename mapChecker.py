#Michael 2/15 EDIT
#Build grid functions/establish map capability with the functions below
def get_game_grid():
    map_array = [[100, 0, 0, 0, 0, 0, 0, 0, 0, 100], [100, 0, 0, 0, 0, 0, 0, 0, 0, 100], [100, 0, -1, 0, 0, 0, 0, -1, 0, 100]
    ,[100, 0, 0, 0, 0, 0, 0, 0, 0, 100], [100, 0, 0, 0, 0, 0, 0, 0, 0, 100], [100, 0, 0, 0, 0, 0, 0, 0, 0, 100], [100, 0, 0, 0, 0, 0, 0, 0, 0, 100]
    , [100, 0, -1, 0, 0, 0, 0, -1, 0, 100], [100, 0, 0, 0, 0, 0, 0, 0, 0, 100], [100, 0, 0, 0, 0, 0, 0, 0, 0, 100]]
    #-1s we can build command centers on and will also signify mineral fields (will be command centers on mineral fields for ease)

    return map_array

def check_build_noncommand_structures(map_array, xcoord, ycoord):
    return (map_array[xcoord - 1][ycoord] == 75 or map_array[xcoord + 1][ycoord] == 75 or map_array[xcoord][ycoord - 1] == 75 or map_array[xcoord][ycoord + 1] == 75)
    #Assuming that command center built at new base health is 75 and other new base buildings will be 50

def check_build_command_structure(map_array, xcoord, ycoord):
    return map_array[xcoord][ycoord] == -1
    #-1 is the placeholder for new base structures

def check_home_base_build_structure(map_array, xcoord, ycoord):
    return map_array[xcoord][ycoord] == -2
    #-2 will be placeholderr for starting base structures that are destroyed

    

#Unfinished function
def check_player_troops(player1_troops, player2_troops, xcoord, ycoord):
    if player2_troops[xcoord * 10 + ycoord] != []:
        return "The opposing player has troops here!"
    else:
        return "There are no opposing troops here!"
