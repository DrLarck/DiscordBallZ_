"""
Represents Zarbon

--

Author : Zyorhist

Last update : 03/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

class Character_012(Character):
    """
    Represents the Zarbon unit from the Namek saga.
    """

    def __init__(self):
        Character.__init__(self)

        # info
        self.info.name = "Zarbon"
        self.info.id = 12
        self.info.saga = "Namek"

        # stat
        self.health.maximum = 2750
        
        self.damage.physical_max = 700
        self.damage.ki_max = 625

        self.defense.armor = 400
        self.defense.spirit = 400
        self.defense.dodge = 0

        self.critical_chance = 10
        self.regeneration.ki = 2