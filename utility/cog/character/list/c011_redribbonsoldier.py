"""
Represents Red Ribbon Soldier

--

Author : Zyorhist

Last update : 17/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

class Character_011(Character):
    """
    Represents the Red Ribbon Soldier unit from the Red Ribbon Army saga.
    """

    def __init__(self):
        Character.__init__(self) 

        # info
        self.info.name = "Red Ribbon Soldier"
        self.image.image = "https://i.imgur.com/BeEGFpv.png"
        self.info.id = 11
        self.info.saga = "Red Ribbon Army"

        # stat
        self.health.maximum = 2000
        
        self.damage.physical_max = 775
        self.damage.ki_max = 625

        self.defense.armor = 550
        self.defense.spirit = 400
        self.defense.dodge = 5

        self.critical_chance = 20
        self.regeneration.ki = 5