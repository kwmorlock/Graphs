from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

traversal_path = ['n', 's']
# traversal_path = []

#my tips
#que or stack might be counterproductive, since we cant teleport
#dictionary probably?
#might not need a class
#get to every room with least amount of backtracking
#use loop logic, want to keep running program until it does what it needs to do, and then moves onto something else


# class Traversal_is_the_worstal:
#     def __init__(self, player):
#         self.player = player
#         self.traversal_path = []


time_machine = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'}

previous_choice = [None]
gogo = {} #we got rooms to see
got_it = {} #been there done that

def good_choice(room_number):
    choice = []
    if 'n' in room_graph[room_number][1].keys():
        choice.append('n')
    if 'e' in room_graph[room_number][1].keys():
        choice.append('e')
    if 's' in room_graph[room_number][1].keys():
        choice.append('s')
    if 'w' in room_graph[room_number][1].keys():
        choice.append('w')
    
    return choice

while len(got_it) < len(room_graph): #while rooms ive been to is less than total rooms
    roomid = player.current_room.id #You may find the commands `player.current_room.id` useful (directions)
    if roomid not in gogo:

        got_it[roomid] = roomid

        gogo[roomid] = good_choice(roomid)

    if len(gogo[roomid]) < 1:  
        previousDirection = previous_choice.pop()
        traversal_path.append(previousDirection)

        player.travel(previousDirection)

    else:
        nextDirection = gogo[roomid].pop(0) # removes first item in list (index of 0)
        traversal_path.append(nextDirection)

        previous_choice.append(time_machine[nextDirection])
        player.travel(nextDirection)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
