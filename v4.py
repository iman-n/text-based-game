'''
Now the game has six rooms with various items, and the monster moves only to adjacent rooms.
This setup requires the player to be more strategic in their movements.
The game ends when the player's health reaches zero or when the player finds all the treasures.
'''

import random

class Room:
    def __init__(self, description: str, monster: bool, treasure: bool, potion: bool):
        self.description = description
        self.monster = monster
        self.treasure = treasure
        self.potion = potion
        self.connected_rooms = {}

    def add_room(self, direction: str, room):
        self.connected_rooms[direction] = room


class Game:
    def __init__(self):
        self.rooms = self.create_rooms()
        self.current_room = self.rooms[0]
        self.monster_room = self.rooms[random.randint(1, 5)]
        self.game_over = False
        self.health = 100
        self.treasures_found = 0

    def create_rooms(self):
        room1 = Room("You're in a spooky room with four doors.", False, False, False)
        room2 = Room("This room is full of gold.", False, True, False)
        room3 = Room("This room is cold and empty.", False, False, False)
        room4 = Room("This room is warm and cozy.", False, False, True)
        room5 = Room("You see an old library filled with dust.", False, True, False)
        room6 = Room("This room is filled with ancient artifacts.", False, False, False)

        room1.add_room("left", room2)
        room1.add_room("right", room3)
        room1.add_room("forward", room4)
        room1.add_room("backward", room5)
        
        room2.add_room("right", room1)
        room3.add_room("left", room1)
        room4.add_room("backward", room1)
        room5.add_room("forward", room1)
        
        room2.add_room("forward", room6)
        room6.add_room("backward", room2)

        return [room1, room2, room3, room4, room5, room6]

    def move_monster(self):
        possible_rooms = [room for room in self.monster_room.connected_rooms.values() if room != self.current_room]
        self.monster_room.monster = False
        self.monster_room = random.choice(possible_rooms)
        self.monster_room.monster = True

    def play(self):
        while not self.game_over:
            print(self.current_room.description)

            if self.current_room.monster:
                print("Oh no, a monster! You lose 30 health.")
                self.health -= 30
                if self.health <= 0:
                    print("You have 0 health. GAME OVER")
                    self.game_over = True
                else:
                    print(f"You have {self.health} health left.")
                self.move_monster()

            if self.current_room.treasure:
                print("You found a treasure!")
                self.treasures_found += 1
                self.current_room.treasure = False
                if self.treasures_found == 3:
                    print("You found all the treasures! YOU WON")
                    self.game_over = True

            if self.current_room.potion:
                print("You found a healing potion! You regain 50 health.")
                self.health += 50
                self.current_room.potion = False

            command = input("Which way do you want to go?").lower()

            if command in self.current_room.connected_rooms:
                self.current_room = self.current_room.connected_rooms[command]
            else:
                print("You can't go that way!")

if __name__ == "__main__":
    print("Welcome to 'The Labyrinth of Ghouls and Treasures'!")
    print("Your mission is to navigate through the labyrinth, find the gold, and avoid the ghoul.")
    game = Game()
    game.play()

