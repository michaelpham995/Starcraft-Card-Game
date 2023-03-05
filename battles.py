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

    #Sort to put lowest health troops in the coordinate first and highest last
    army1_present.sort(key = lambda i: i[2])
    army2_present.sort(key = lambda i: i[2])

    if len(army1_present) > 0 and len(army2_present) > 0:
        winner, survivors = fight(army1_present, army2_present, army1, army2) 

    #Call the update_army function to update the armies for later rounds
    if winner == "A1":
        army1, army2 = update_army(winner, survivors, army1, army2, coords)
    elif winner == "A2":
        army2, army1 = update_army(winner, survivors, army1, army2, coords)
    else:
        army1, army2 = update_losers(army1, army2, coords)
    
    return army1, army2



#This function determine sht winners and losers of the battle
#For now I'm playing this by a rule of the weaker troops get targeted and destroyed first
#The fight will settle within the turn and the damages are not absolute (as troops need to be killed but) relevant to compare troop strength
def fight(a1_present, a2_present, a1, a2):
    a1_present_health = 0
    a2_present_health = 0
    a1_attack = 0
    a2_attack = 0
    survivors = []

    for troop in a1_present:
        a1_present_health += troop[2]
        a1_attack += troop[1]

    for troop in a2_present:
        a2_present_health += troop[2]
        a2_attack += troop[1]
    
    while a1_present_health > 0 and a2_present_health > 0:
        a1_present_health -= a2_attack
        a2_present_health -= a1_attack

    if a1_present_health > a2_present_health:
        winner = "A1"
    elif a2_present_health > a1_present_health:
        winner = "A2"
    else:
        winner = "None"

    if winner == "A1":
        a2 = []
        remaining_health = a1_present_health
        for i in reversed(a1_present):
            remaining_health -= a1_present[i][2]
            if a1_present_health > 0:
                survivors.append(a1_present[i])          
    elif winner == "A2":
        a1 = []
        remaining_health = a2_present_health
        for i in reversed(a2_present):
            remaining_health -= a2_present[i][2]
            if a2_present_health > 0:
                survivors.append(a2_present[i])
    else:
        a1 = []
        a2 = []


    return winner, survivors
    #We want to return the winner and which army had survivors in it!


#This function will update the army on th esquares where battles occured - One will stand, one will fall 
def update_army(winner, survivors, army1, army2, coords):
    if winner == "A1":
        win, lose = new_placement(army1, army2, survivors, coords)
    else:
        win, lose = new_placement(army2, army1, survivors, coords)

    #Inner function that will handle the new placements of troops
    #Winner of coordinate will get to keep health of survivng troops
    def new_placement(winning_army, losing_army, survivors, coords):
        print(losing_army)
        for army in range(len(losing_army)):
            if losing_army[army][5] == coords[0] and losing_army[army][6] == coords[1]:
                losing_army[army][2] = 'dead'
        losing_army = [x for x in losing_army if x[2] != "dead"]
        print(losing_army)
        for army in range(len(winning_army)):
            if winning_army[army][5] == coords[0] and winning_army[army][6] == coords[1]:
                winning_army[army][2] = 'dead'
        winning_army = [x for x in winning_army if x[2] != "dead"]
        
        for troop in survivors:
            winning_army.append(troop)

        return winning_army, losing_army

    #Return new armies
    return win, lose


#This function is if there is a tie so both armies in coordinates are eliminated
def update_losers(army1, army2, coords):
    for army in range(len(army1)):
        if army1[army][5] == coords[0] and army1[army][6] == coords[1]:
            army1[army][2] = 'dead'
    army1 = [x for x in army1 if x[2] != "dead"]

    for army in range(len(army2)):
        if army2[army][5] == coords[0] and army2[army][6] == coords[1]:
            army2[army][2] = 'dead'
    army2 = [x for x in army2 if x[2] != "dead"]   
    
    return army1, army2


