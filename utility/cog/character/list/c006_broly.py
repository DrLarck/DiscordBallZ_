"""
Represents Broly

--

Author : Zyorhist

Last update : 06/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

class Character_006(Character):
    """
    Represents the Broly unit from the Broly saga.
    """

    def __init__(self):
        Character.__init__(self)

        # info
        self.info.name = "Broly"
        self.info.id = 6
        self.info.saga = "Broly"

        # stat
        self.health.maximum = 3125
        
        self.damage.physical_max = 625
        self.damage.ki_max = 475

        self.defense.armor = 550
        self.defense.spirit = 475
        self.defense.dodge = 25

        self.critical_chance = 10
       
        self.regeneration.ki = 2
