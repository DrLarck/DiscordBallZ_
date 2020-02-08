"""
Represents the mission n°1

--

Author : DrLarck

Last update : 03/02/20 (DrLarck)
"""

# dependancies
import asyncio
import random

# util
from utility.cog.mission.mission import Mission

# opponent
from utility.cog.character.list.c001_sabimen import Character_001
from utility.cog.character.list.c002_sabimen import Character_002
from utility.cog.character.list.c003_sabimen import Character_003

class Mission_1(Mission):
    """
    Opponent : Team of Saibaiman

    Reward :

    - dragonstone 10

    - zenis 100

    - team xp 150

    Level : [5, 10]
    """

    # attribute
    def __init__(self):
        Mission.__init__(self)
        self.name = "Saibaiman attack"
        self.star = 5

        self.level_range = {
            "min" : 5,
            "max" : 10
        }

        # reward
        self.dragonstone = 666
        self.zenis = 42
        self.player_xp = 69
        self.team_xp = 420

    async def set_opponent(self):
        
        # init
        self.opponent = [
            Character_001(),
            Character_002(),
            Character_003()
        ]

        # set the level
        for character in self.opponent:
            await asyncio.sleep(0)

            rand_level = random.randint(self.level_range["min"], self.level_range["max"])

            character.level = rand_level
            character.is_npc = True

        return(self.opponent)