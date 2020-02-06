"""
Represents Tora

--

Author : Zyorhist

Last update : 06/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

class Character_030(Character):
    """
    Represents the Tora unit from the Bardock saga.
    """

    def __init__(self):
        Character.__init__(self)

        # info
        self.info.name = "Tora"
        self.info.id = 30
        self.info.saga = "Bardock"

        # stat
        self.health.maximum = 2375
        
        self.damage.physical_max = 325
        self.damage.ki_max = 925

        self.defense.armor = 475
        self.defense.spirit = 550
        self.defense.dodge = 5

        self.critical_chance = 5
       
        self.regeneration.ki = 3
