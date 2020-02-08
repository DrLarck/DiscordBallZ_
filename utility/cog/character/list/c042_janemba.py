"""
Represents Janemba

--

Author : Zyorhist

Last update : 07/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

class Character_042(Character):
    """
    Represents the Janemba unit from the Janemba saga.
    """

    def __init__(self):
        Character.__init__(self)

        # info
        self.info.name = "Janemba"
        self.info.id = 42
        self.info.saga = "Janemba"

        # stat
        self.health.maximum = 2750
        
        self.damage.physical_max = 475
        self.damage.ki_max = 1000

        self.defense.armor = 325
        self.defense.spirit = 400
        self.defense.dodge = 45

        self.critical_chance = 10
       
        self.regeneration.ki = 1
