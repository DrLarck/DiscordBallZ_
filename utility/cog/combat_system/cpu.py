"""
CPU user for combats

--

Author : DrLarck

Last update : 15/02/20 (DrLarck)
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

        self.team = Team()

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

                self.team.append(character)
            
        return(self.team)

