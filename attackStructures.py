#This functions checks to see if any enemy troops are on any enemy structures
def check_buildings(map, army, player):
    if player == "P2":
        i = 0
        for j in range(len(map)):
            if map[j][i] > 0:
                coords = [j, i]
                attack_buildings(map, coords, army)
    elif player == "P1":
        i = 9
        for j in range(len(map)):
            if map[j][i] > 0:
                coords = [j, i]
                attack_buildings(map, coords, army)

    return

#This function is where we reduce the buildings health
def attack_buildings(map, coords, army):
    for troop in range(len(army)):
        if army[troop][5] == coords[0] and army[troop][6] == coords[1]:
            map[coords[0]][coords[1]] -= army[troop][1]
    return
    