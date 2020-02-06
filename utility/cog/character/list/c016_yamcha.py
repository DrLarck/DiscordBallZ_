"""
Represents Yamcha

--

Author : Zyorhist

Last update : 06/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

class Character_016(Character):
    """
    Represents the Yamcha unit from the Cell saga.
    """

    def __init__(self):
        Character.__init__(self)

        # info
        self.info.name = "Yamcha"
        self.info.id = 16
        self.info.saga = "Cell"

        # stat
        self.health.maximum = 2750
        
        self.damage.physical_max = 1000
        self.damage.ki_max = 475

        self.defense.armor = 325
        self.defense.spirit = 400
        self.defense.dodge = 15

        self.critical_chance = 25
       
        self.regeneration.ki = 2