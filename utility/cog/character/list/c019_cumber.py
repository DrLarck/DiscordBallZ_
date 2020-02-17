"""
Represents Cumber

--

Author : Zyorhist

Last update : 17/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

class Character_019(Character):
    """
    Represents the Cumber unit from the Universe Conflict saga.
    """

    def __init__(self):
        Character.__init__(self)

        # info
        self.info.name = "Cumber"
        self.image.image = "https://i.imgur.com/XJ0TCd6.png"
        self.info.id = 19
        self.info.saga = "Universe Conflict"

        # stat
        self.health.maximum = 3500
        
        self.damage.physical_max = 550
        self.damage.ki_max = 475

        self.defense.armor = 550
        self.defense.spirit = 475
        self.defense.dodge = 5

        self.critical_chance = 5
       
        self.regeneration.ki = 2
