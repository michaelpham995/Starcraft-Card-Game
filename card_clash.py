import random

class Card:
    def __init__(self, name, attack, health, defense, cost, unit_count):
        self.name = name
        self.attack = attack
        self.health = health
        self.defense = defense
        self.cost = cost
        self.unit_count = unit_count

    def __str__(self):
        return f"{self.name}: Attack={self.attack}, Defense={self.defense}"

class Deck:
    def __init__(self, cards):
        self.cards = cards

    def draw(self):
        if self.is_empty():
            return None
        return self.cards.pop(0)

    def is_empty(self):
        return len(self.cards) == 0

class Player:
    def __init__(self, name, deck, health, minerals):
        self.name = name
        self.deck = deck
        self.hand = []
        self.health = health
        self.field = []
        self.minerals = minerals

    def draw(self):
        card = self.deck.draw()
        if card is not None:
            self.hand.append(card)
        return card

    def play_card(self, card):
        self.field.append(card)

    #Buy Card method - MICHAEL EDIT 2/15
    def buy_troops(self, card_index):
        if self.minerals < self.deck.cards[card_index].cost:
            print(f"{self.name} does not have enough minerals to buy this card.")
            return
        self.minerals -= self.deck.cards[card_index].cost
        self.hand.append(self.deck.cards[card_index])
        self.deck.cards.pop(card_index)
        print(f"{self.name} buys {self.hand[-1].name} for {self.hand[-1].cost} minerals.")



def card_clash(p1, p2):
    while True:
        
        p1.draw()
        p2.draw()

        print(f"{p1.name} has {p1.health} health and {len(p1.field)} cards on the field")
        print(f"{p2.name} has {p2.health} health and {len(p2.field)} cards on the field")

        p1_card = None
        if len(p1.hand) > 0:
            p1_card = random.choice(p1.hand)
            p1.hand.remove(p1_card)
            p1.play_card(p1_card)

        p2_card = None
        if len(p2.hand) > 0:
            p2_card = random.choice(p2.hand)
            p2.hand.remove(p2_card)
            p2.play_card(p2_card)


        if p1_card is not None and p2_card is not None:
            if p1_card.attack > p2_card.defense:
                p2.health -= p1_card.attack - p2_card.defense
                print(f"{p1.name} attacks {p2.name} and deals {p1_card.attack - p2_card.defense} damage!")
                p2.field.remove(p2_card)
            elif p2_card.attack > p1_card.defense:
                p1.health -= p2_card.attack - p1_card.defense
                print(f"{p2.name} attacks {p1.name} and deals {p2_card.attack - p1_card.defense} damage!")
                p1.field.remove(p1_card)

        if p1.health <= 0:
            print(f"{p2.name} wins!")
            return p2
        elif p2.health <= 0:
            print(f"{p1.name} wins!")
            return p1


#protoss_cards = [Card("Zealot", 10, 10, 50), Card("High Templar", 20, 10, 80), Card("Photon Cannon", 5, 30, 100)]
#zerg_cards = [Card("Zergling", 5, 5, 20)]
#terran_cards = [Card("Tank", 50, 25, 200)]

protoss_cards = [Card("Zealot", 19, 100, 1, 100, 1), Card("Stalker", 10, 160, 1, 125, 1), Card("High Templar", 4, 80, 1, 150, 1), Card("Immortal", 20, 300, 1, 275, 1), Card("Colossus", 10, 350, 1, 350, 1), Card("Void Ray", 17, 250, 0, 250, 1), Card("Carrier", 40, 450, 2, 500, 1)]
zerg_cards = [Card("Zergling", 10, 35, 0, 25, 1), Card("Baneling", 25, 35, 0, 50, 1), Card("Roach",11, 145, 1, 75, 1), Card("Hydralisk", 20, 90, 0, 100, 1), Card("Ravager", 14, 120, 1, 125, 1), Card("Mutalisk", 12, 120, 0, 150, 1)]
terran_cards = [Card("Marine", 11, 45, 0, 50, 1), Card("Marauder", 9, 125, 1, 100, 1), Card("Hellion", 5, 90, 0, 100, 1), Card("Siege Tank", 20, 175, 1, 150, 1), Card("Thor", 60, 400, 1, 450, 1), Card("Medivac", 0, 150, 0, 100, 1), Card("Viking", 15, 135, 0, 150, 1), Card("Battlecrusier", 45, 550, 3, 550, 1)]

protoss_deck = Deck(protoss_cards * 8)
zerg_deck = Deck(zerg_cards * 8)
terran_deck = Deck(terran_cards * 8)

#I think we should store troops on map based on dictionary, EDITED by Michael think of it like bwlo
# player1_dict = {"Zealot" : [[2, 2], [10, 160, 1, 125, 1]}
# The first list in the value slot are the coordinates for where the troop is on the map!

player1_troop_dict = {}
player2_troop_dict = {}



choices = {"protoss": protoss_deck, "zerg": zerg_deck, "terran": terran_deck}

p1_choice = None
p2_choice = None

input_p1 = input("Player 1 do you want to play as Zerg, Protoss, or Terran? ")
while input_p1 not in choices.keys():
    input_p1 = input("Pleaes enter zerg, terran, or protoss: ")

p1_choice = choices[input_p1]

input_p2 = input("Player 2 do you want to play as Zerg, Protoss, or Terran? ")
while input_p2 not in choices.keys():
    input_p2 = input("Pleaes enter zerg, terran, or protoss: ")

p2_choice = choices[input_p2]

p1 = Player("Stefan", p1_choice, 500, 1000)
p2 = Player("Matthew", p2_choice, 500, 1000)


#winner = card_clash(p1, p2)






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


#Allows player to buy troops below 
def buy_troops(player, playerdict, deck, buy_more):
    #This is psuedo input below for player to choose what to buy
    while buy_more == True:
        troop = input("Please select the troop you would like to buy")
        

    

print(get_game_grid())
