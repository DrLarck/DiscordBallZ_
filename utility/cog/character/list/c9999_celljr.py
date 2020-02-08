"""
Represents Cell Jr

--

Author : Zyorhist

Last update : 07/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

class Character_9999(Character):
    """
    Represents the Cell Jr unit from the Android Cell.
    """

    def __init__(self):
        Character.__init__(self)

        # info
        self.info.name = "Cell Jr"
        self.info.id = 9999
        self.info.saga = "Cell"

        # stat
        self.health.maximum = 500
        
        self.damage.physical_max = 700
        self.damage.ki_max = 475

        self.defense.armor = 400
        self.defense.spirit = 400
        self.defense.dodge = 0

        self.critical_chance = 0
       
        self.regeneration.ki = 0
