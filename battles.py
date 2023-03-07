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


#This is incomplete - In progress action item
#This function serves to detect enemy troops within 1 square of an x/y coordinate and allows a battle to commence
def dfs_nearby_conflict(tmp1, tmp2, pres1, pres2, coords):

    #Checks bottom left, bottom, and left squares adjacent to coordinate
    if (coords[0] - 1) >= 0 and (coords[1] - 1 >= 0):
        for i in range(len(tmp1)):
            if (tmp1[i][5] == (coords[0] - 1) and tmp1[i][6] == (coords[1] - 1)) or (tmp1[i][5] == (coords[0]) and tmp1[i][6] == (coords[1] - 1)) or (tmp1[i][5] == (coords[0] - 1) and tmp1[i][6] == (coords[1])):
                pres1.append(tmp1[i])
        for i in range(len(tmp2)):
            if tmp2[i][5] == (coords[0] - 1) and tmp2[i][6] == (coords[1] - 1) or (tmp2[i][5] == (coords[0]) and tmp2[i][6] == (coords[1] - 1)) or (tmp2[i][5] == (coords[0] - 1) and tmp2[i][6] == (coords[1])):
                pres2.append(tmp2[i])
    #Checks top right, top, and right squares adjacent to coordinate
    if (coords[0] + 1) < 10 and (coords[1] + 1) < 10:
        for i in range(len(tmp1)):
            if (tmp1[i][5] == (coords[0] + 1) and tmp1[i][6] == (coords[1] + 1)) or (tmp1[i][5] == (coords[0]) and tmp1[i][6] == (coords[1] + 1)) or (tmp1[i][5] == (coords[0] +1) and tmp1[i][6] == (coords[1])):
                pres1.append(tmp1[i])
        for i in range(len(tmp2)):
            if tmp2[i][5] == (coords[0] + 1) and tmp2[i][6] == (coords[1] + 1) or (tmp2[i][5] == (coords[0]) and tmp2[i][6] == (coords[1] + 1)) or (tmp2[i][5] == (coords[0] + 1) and tmp2[i][6] == (coords[1])):
                pres2.append(tmp2[i]) 
    #Checks top left
    if (coords[0] + 1) < 10 and (coords[1] - 1) >= 0:
        for i in range(len(tmp1)):
            if (tmp1[i][5] == (coords[0] + 1)) and (tmp1[i][6] == (coords[1] - 1)):
                pres1.append(tmp1[i])
        for i in range(len(tmp2)):
            if (tmp2[i][5] == (coords[0] + 1)) and (tmp2[i][6] == (coords[1] - 1)):
                pres1.append(tmp2[i]) 
    #Checks bottom right
    if (coords[0] - 1) >= 0 and (coords[1] + 1) < 10:
        for i in range(len(tmp1)):
            if (tmp1[i][5] == (coords[0] + 1)) and (tmp1[i][6] == (coords[1] - 1)):
                pres1.append(tmp1[i])
        for i in range(len(tmp2)):
            if (tmp2[i][5] == (coords[0] + 1)) and (tmp2[i][6] == (coords[1] - 1)):
                pres1.append(tmp2[i]) 

    return pres1, pres2


#This function handles battles present on the map
def battle(army1, army2, coords, config1, config2):

    army1_present = []
    army2_present = []


    for i in range(len(army1)):
        if army1[i][5] == coords[0] and army1[i][6] == coords[1] and army1[i][2] != 'dead':
            army1_present.append(army1[i])
    
    for i in range(len(army2)):
        if army2[i][5] == coords[0] and army2[i][6] == coords[1] and army2[i][2] != 'dead':
            army2_present.append(army2[i])

    dfs_nearby_conflict(army1, army2, army1_present, army2_present, coords)
    

    #Sort to put lowest health troops in the coordinate first and highest last
    army1_present.sort(key = lambda i: i[2])
    army2_present.sort(key = lambda i: i[2])

    if len(army1_present) > 0 and len(army2_present) > 0:
        fight(army1_present, army2_present, army1, army2, coords) 


    backup1, backup2 = [], []

    #backup updater
    for i in range(len(army1)):
        if army1[i][2] != 'dead':
            backup1.append(army1[i])
    for j in range(len(army2)):
        if army2[j][2] != 'dead':
            backup2.append(army2[j])


    #Update player configurations for army size
    config1[2], config2[2] = 25 - len(backup1), 25 - len(backup2)

    return backup1, backup2



#This function determine sht winners and losers of the battle
#For now I'm playing this by a rule of the weaker troops get targeted and destroyed first
#The fight will settle within the turn and the damages are not absolute (as troops need to be killed but) relevant to compare troop strength
def fight(a1_present, a2_present, army1, army2, coords):
    a1_present_health = 0
    a2_present_health = 0
    a1_attack = 0
    a2_attack = 0
    survivors = []

    for i in range(len(a1_present)):
        a1_present_health += a1_present[i][2]
        a1_attack += a1_present[i][1]

    for i in range(len(a2_present)):
        a2_present_health += a2_present[i][2]
        a2_attack += a2_present[i][1]
    
    while a1_present_health > 0 and a2_present_health > 0:
        a1_present_health -= a2_attack
        a2_present_health -= a1_attack

    if a1_present_health > a2_present_health:
        winner = "A1"
    elif a2_present_health > a1_present_health:
        winner = "A2"
    else:
        winner = "None"

    #Call the update_army function to update the armies for later rounds
    if winner == "A1":
        army1, army2 = update_army(winner, army1, army2, coords)     
    elif winner == "A2":
        army2, army1 = update_army(winner, army1, army2, coords)   
    else:
        army1, army2 = update_losers(army1, army2, coords)


    return army1, army2
    #We want to return the winner and which army had survivors in it!


#This function will update the army on th esquares where battles occured - One will stand, one will fall 
def update_army(winner, army1, army2, coords):

    #Inner function that will handle the new placements of troops
    #Winner of coordinate will get to keep health of survivng troops
    def new_placement(winning_army, losing_army, coords):
        
        for army in range(len(losing_army)):
            if losing_army[army][5] == coords[0] and losing_army[army][6] == coords[1]:
                losing_army[army][2] = 'dead'

        print(losing_army)
        tmp_lose = losing_army
        losing_army = []
        for army in range(len(tmp_lose)):
            if tmp_lose[army][2] != 'dead':
                losing_army.append(tmp_lose[army])


        return winning_army, losing_army
    

    if winner == "A1":
        win, lose = new_placement(army1, army2, coords)
    else:
        win, lose = new_placement(army2, army1, coords)


    #Return new armies
    return win, lose


#This function is if there is a tie so both armies in coordinates are eliminated
def update_losers(army1, army2, coords):
    for army in range(len(army1)):
        if army1[army][5] == coords[0] and army1[army][6] == coords[1]:
            army1[army][2] = 'dead'
    tmpArmy1 = army1
    army1 = []
    for army in range(len(tmpArmy1)):
        if tmpArmy1[army][2] != "dead":
            army1.append(army1[army])
        
    for army in range(len(army2)):
        if army2[army][5] == coords[0] and army2[army][6] == coords[1]:
            army2[army][2] = 'dead'
    tmpArmy2 = army2
    army2 = []
    for army in range(len(tmpArmy2)):
        if tmpArmy2[army][2] != "dead":
            army2.append(army2[army])
        
    
    return army1, army2