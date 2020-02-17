"""
Represents Recoome

--

Author : Zyorhist

Last update : 17/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

class Character_034(Character):
    """
    Represents the Recoome unit from the Namek saga.
    """

    def __init__(self):
        Character.__init__(self)

        # info
        self.info.name = "Recoome"
        self.image.image = "https://i.imgur.com/xuInQsX.png"
        self.info.id = 34
        self.info.saga = "Namek"

        # stat
        self.health.maximum = 4250
        
        self.damage.physical_max = 250
        self.damage.ki_max = 325

        self.defense.armor = 700
        self.defense.spirit = 625
        self.defense.dodge = 15

        self.critical_chance = 15
       
        self.regeneration.ki = 2
