"""
Represents Gohan

--

Author : Zyorhist

Last update : 17/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

class Character_040(Character):
    """
    Represents the Gohan unit from the Cell saga.
    """

    def __init__(self):
        Character.__init__(self)

        # info
        self.info.name = "Gohan"
        self.image.image = "https://i.imgur.com/6Q0eTBi.png"
        self.info.id = 40
        self.info.saga = "Cell"

        # stat
        self.health.maximum = 2000
        
        self.damage.physical_max = 550
        self.damage.ki_max = 925

        self.defense.armor = 475
        self.defense.spirit = 475
        self.defense.dodge = 0

        self.critical_chance = 0
       
        self.regeneration.ki = 5
