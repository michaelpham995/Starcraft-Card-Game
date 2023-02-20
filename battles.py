#This is the file where fight results will come from

def is_there_conflict(p1_map, p2_map):
    conflict_squares = []
    for i in range(len(p1_map)):
        for j in range(len(p1_map[0])):
            if p1_map[i][j] != 0 and p2_map[i][j] != 0:
                conflict_squares.append([i, j])
    return conflict_squares