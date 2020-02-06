"""
Represents Borgos

--

Author : Zyorhist

Last update : 06/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

class Character_029(Character):
    """
    Represents the Borgos unit from the Bardock saga.
    """

    def __init__(self):
        Character.__init__(self)

        # info
        self.info.name = "Borgos"
        self.info.id = 29
        self.info.saga = "Bardock"

        # stat
        self.health.maximum = 3125
        
        self.damage.physical_max = 400
        self.damage.ki_max = 250

        self.defense.armor = 775
        self.defense.spirit = 700
        self.defense.dodge = 15

        self.critical_chance = 0
       
        self.regeneration.ki = 2
