"""
Represents Jeice

--

Author : Zyorhist

Last update : 07/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

class Character_033(Character):
    """
    Represents the Jeice unit from the Namek saga.
    """

    def __init__(self):
        Character.__init__(self)

        # info
        self.info.name = "Jeice"
        self.info.id = 33
        self.info.saga = "Namek"

        # stat
        self.health.maximum = 2000
        
        self.damage.physical_max = 475
        self.damage.ki_max = 925

        self.defense.armor = 400
        self.defense.spirit = 550
        self.defense.dodge = 5

        self.critical_chance = 20
       
        self.regeneration.ki = 4