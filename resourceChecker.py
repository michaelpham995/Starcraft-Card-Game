
def check_enough_minerals(player_config, race_choice, choose_unit):
    if player_config[1] - race_choice[choose_unit][3] >= 0:
        return True
    return False

def check_enough_space(player_config, race_choice, choose_unit):
    if player_config[2] - race_choice[choose_unit][4] >= 0:
        return True
    return False