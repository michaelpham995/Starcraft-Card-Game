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

protoss_cards = [Card("Zealot", 19, 100, 1, 100), Card("Stalker", 10, 160, 1, 125), Card("High Templar", 4, 80, 1, 150), Card("Immortal", 20, 300, 1, 275), Card("Colossus", 10, 350, 1, 350), Card("Void Ray", 17, 250, 0, 250), Card("Carrier", 40, 450, 2, 500)]
zerg_cards = [Card("Zergling", 10, 35, 0, 25), Card("Baneling", 25, 35, 0, 50), Card("Roach",11, 145, 1, 75), Card("Hydralisk", 20, 90, 0, 100), Card("Ravager", 14, 120, 1, 125), Card("Mutalisk", 12, 120, 0, 150)]
terran_cards = [Card("Marine", 11, 45, 0, 50), Card("Marauder", 9, 125, 1, 100), Card("Hellion", 5, 90, 0, 100), Card("Siege Tank", 20, 175, 1, 150), Card("Thor", 60, 400, 1, 450), Card("Medivac", 0, 150, 0, 100), Card("Viking", 15, 135, 0, 150), Card("Battlecrusier", 45, 550, 3, 550)]

protoss_deck = Deck(protoss_cards * 8)
zerg_deck = Deck(zerg_cards * 8)
terran_deck = Deck(terran_cards * 8)

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


winner = card_clash(p1, p2)
