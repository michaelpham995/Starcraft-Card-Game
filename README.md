# Meet the Developer
My name is Matthew Pham and I am a senior from George Ranch High School who will be attending the University of Texas at Austin in the coming Fall. I am interested in game development and mobile app development and take inspiration from companies such as Supercell, Blizzard, and Mojang. I eventually want to pursue a career in this field and wish to contribute to the growing availability of enjoyable pasttimes for all people of all ages around the globe.

# Game Objective
This is a game that aims to create a simulation of an actual Starcraft PvP match in a 1v1 format!

## Inspiration
This game is inspired from Starcraft 1 and Starcraft 2, both of which were produced from Blizzard

## Game Rules

### Starting Rules
1.There are two players that take part in this game
2.The two players can choose 1 of 3 races: zerg, protoss, and terran
3.The players choose their names and start with 1000 minerals and the ability to build up to 25 troop units at a time
4.The first player to destroy the other players 10 buildings wins the game!


### Game Rules
For each turn the players have the ability to do the following
1.Build units for their army
2.Choose coordinates for troop movement to attack opponent troops and structures.
3.If a player loses all 4 of their barracks they can no longer produce troops.
4.If a player loses mineral collectors, they collect less minerals each turn. If they lose all 6, they can no longer produce minerals.
5.When troops are on the same square, they prioritze attacking each other rather than the buildings that are on those squares first.


### Softwares used
1.Visual Studio Code
2.Github and Command Line


### File breakdown
##### main.py 
The game runs entirely on this file and calls from functions from all other files. This contains functions to update troops and initialize player properties and race selections.

##### mapChecker.py 
This serves to initialize the buildings on the map for each players. In addition it calculates it contributes to checking where troops are on the map for the player and checks which buildings are still functional for the player. This helps determine what they are able to do on their turn.

##### moveAndPrint.py 
This file serves to produce clean output which lists a players options for recruiting troops and moving troops. It is a clean layout that improves from printing dictionaries and lists onto the output.

##### resouceChecker.py 
Here is where players are notified if they have available resources and unit availability to produce troops.

##### attackStructures.py 
This detects if troops are on enemy structues and deals damage to those structures.

##### battles.py
This file detects coordinates where battles transpires on the map. Automatically conducts battles between opposing armies and updates survivors of the battle!


### Looking into the Future
In the future I want to add troop visualization and detection that will allow troops to change the direction they are moving in based upon nearby opponents. In addition to this I am currently learning React and would like to build a web application that hosts this game and uses graphics to display it!
