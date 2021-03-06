"""
CPU user for combats

--

Author : DrLarck

Last update : 17/02/20 (DrLarck)
"""

# dependancies
import asyncio
import random

# utils
from utility.cog.character.getter import Character_getter

class CPU():
    """
    Represents a bot user

    - Attribute 

    `name` (`str`)

    `avatar` (`str` as `url`)

    `team` : `team` (list), `level_min` (int), `level_max` (int)
    """

    # attribute
    def __init__(self):
        self.name = ""
        self.avatar = ""
        self.is_cpu = True

        self.team = Team()
    
    async def pick_fighter(self):
        """
        `coroutine`

        Randomly choose a fighter

        --

        Return : `str` digit
        """

        # init
        fighter_index = 1
        playable = []

        # get the index of playable characters
        for fighter in self.team.team:
            await asyncio.sleep(0)

            # if the char is playable
            # add its index into the list
            if(fighter.health.current > 0 and fighter.posture.stunned == False):
                playable.append(fighter_index)

            fighter_index += 1

        # pick a random playable
        if(len(playable) > 0):
            choice = str(random.choice(playable))

        return(choice)
    
    async def make_move(self, character, move_object, client, ctx, team_a, team_b, turn):
        """
        `coroutine`

        Randomly generate a move

        --

        Return : `Move()`
        """

        # init 
        move = await character.bot(client, ctx, self, team_a, team_b, turn)

        move_object.index = move["move"]
        move_object.target = move["target"]

        return(move_object)

class Team():
    """
    Represents the cpu's team
    """

    def __init__(self):
        self.team = []
        self.level_min = 1
        self.level_max = 1
    
    async def character(self):
        """
        `coroutine`

        Generates a team for the CPU

        --

        Return : `list` of `Character()`
        """

        # init
        getter = Character_getter()

        if(len(self.team) < 3):
            self.team = []

            for i in range(3):  # generates 3 characters
                await asyncio.sleep(0)

                # pick a random id in the list
                char_id = random.choice(getter.character_list) 

                character = await getter.get_character(char_id)

                character.level = random.randint(self.level_min, self.level_max)

                type_value = random.randint(0, 4)

                character.type.value = type_value

                self.team.append(character)
            
        return(self.team)

