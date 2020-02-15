"""
Represents Hercule Satan

--

Author : Zyorhist

Last update : 06/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

class Character_013(Character):
    """
    Represents the Hercule Satan unit from the Android saga.
    """

    def __init__(self):
        Character.__init__(self)

        # info
        self.info.name = "Hercule"
        self.info.id = 13
        self.info.saga = "Cell"

        # stat
        self.health.maximum = 2000
        
        self.damage.physical_max = 325
        self.damage.ki_max = 250

        self.defense.armor = 1000
        self.defense.spirit = 775
        self.defense.dodge = 25

        self.critical_chance = 0
       
        self.regeneration.ki = 5