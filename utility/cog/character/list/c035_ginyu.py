"""
Represents Gaptain Ginyu

--

Author : Zyorhist

Last update : 07/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

class Character_035(Character):
    """
    Represents the Captain Ginyu unit from the Namek saga.
    """

    def __init__(self):
        Character.__init__(self)

        # info
        self.info.name = "Ginyu"
        self.info.id = 35
        self.info.saga = "Namek"

        # stat
        self.health.maximum = 3125
        
        self.damage.physical_max = 475
        self.damage.ki_max = 775

        self.defense.armor = 475
        self.defense.spirit = 400
        self.defense.dodge = 10

        self.critical_chance = 10
       
        self.regeneration.ki = 3
