"""
Represents Jiren

--

Author : Zyorhist

Last update : 17/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

class Character_021(Character):
    """
    Represents the Jiren unit from the Universe Survival saga.
    """

    def __init__(self):
        Character.__init__(self)

        # info
        self.info.name = "Jiren"
        self.image.image = "https://i.imgur.com/9cPTvB3.png"
        self.info.id = 21
        self.info.saga = "Universe Survival"

        # stat
        self.health.maximum = 3125
        
        self.damage.physical_max = 475
        self.damage.ki_max = 475

        self.defense.armor = 550
        self.defense.spirit = 625
        self.defense.dodge = 30

        self.critical_chance = 10
       
        self.regeneration.ki = 1
