"""
Represents Cell

--

Author : Zyorhist

Last update : 17/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

class Character_038(Character):
    """
    Represents the Cell unit from the Cell saga.
    """

    def __init__(self):
        Character.__init__(self)

        # info
        self.info.name = "Cell"
        self.image.image = "https://i.imgur.com/zV40MJL.png"
        self.info.id = 38
        self.info.saga = "Cell"

        # stat
        self.health.maximum = 4625
        
        self.damage.physical_max = 250
        self.damage.ki_max = 250

        self.defense.armor = 625
        self.defense.spirit = 700
        self.defense.dodge = 15

        self.critical_chance = 10
       
        self.regeneration.ki = 2
