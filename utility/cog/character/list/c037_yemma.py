"""
Represents King Yemma

--

Author : Zyorhist

Last update : 07/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

class Character_037(Character):
    """
    Represents the Yemma unit from the Buu saga.
    """

    def __init__(self):
        Character.__init__(self)

        # info
        self.info.name = "Yemma"
        self.info.id = 37
        self.info.saga = "Buu"

        # stat
        self.health.maximum = 3500
        
        self.damage.physical_max = 250
        self.damage.ki_max = 375

        self.defense.armor = 700
        self.defense.spirit = 775
        self.defense.dodge = 20

        self.critical_chance = 0
       
        self.regeneration.ki = 5
