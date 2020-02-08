"""
Represents Krillin

--

Author : Zyorhist

Last update : 07/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

class Character_043(Character):
    """
    Represents the Krillin unit from the Frieza saga.
    """

    def __init__(self):
        Character.__init__(self)

        # info
        self.info.name = "Krillin"
        self.info.id = 43
        self.info.saga = "Frieza"

        # stat
        self.health.maximum = 2375
        
        self.damage.physical_max = 700
        self.damage.ki_max = 775

        self.defense.armor = 325
        self.defense.spirit = 400
        self.defense.dodge = 15

        self.critical_chance = 30
       
        self.regeneration.ki = 2