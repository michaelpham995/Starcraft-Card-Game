#This is the file where fight results will come from

#This determines if the opponents have 2 armies in the same area of the map
def is_there_conflict(p1_map, p2_map):
    conflict_squares = []
    p1_coords, p2_coords = [], []
    for i in range(len(p1_map)):
        p1_coords.append([p1_map[i][5], p1_map[i][6]])
    for i in range(len(p2_map)):
        p2_coords.append([p2_map[i][5], p2_map[i][6]])

    for location in p1_coords:
        if location in p2_coords:
            conflict_squares.append(location)
    return conflict_squares

#This function handles battles present on the map
def battle(army1, army2, coords):

    army1_present = []
    army2_present = []


    for i in range(len(army1)):
        if army1[i][5] == coords[0] and army1[i][6] == coords[1]:
            army1_present.append(army1[i])
    
    for i in range(len(army2)):
        if army2[i][5] == coords[0] and army2[i][6] == coords[1]:
            army2_present.append(army2[i])

    if len(army1_present) > 0 and len(army2_present) > 0:
        a1_casulaties, a2_casulaties = fight(army1_present, army2_present, army1, army2) 


#This function determine sht winners and losers of the battle
#For now I'm playing this by a rule of the weaker troops get targeted and destroyed first
#The fight will settle within the turn and the damages are not absolute (as troops need to be killed but) relevant to compare troop strength
def fight(a1_present, a2_present, a1, a2):
    return
    #We want to return an updated version of a1_present and a2_present
    #The goal them is we will call the update_army function from the battle function to update the army


#This function will update the army on teh squares where battles occured - One will stand, one will fall 
def update_army():
    return




