"""
Represents Future Trunks

--

Author : Zyorhist

Last update : 17/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

class Character_045(Character):
    """
    Represents the Trunks unit from the Android saga.
    """

    def __init__(self):
        Character.__init__(self)

        # info
        self.info.name = "Trunks"
        self.image.image = "https://i.imgur.com/zhucWYu.png"
        self.info.id = 45
        self.info.saga = "Android"

        # stat
        self.health.maximum = 2750
        
        self.damage.physical_max = 700
        self.damage.ki_max = 625

        self.defense.armor = 400
        self.defense.spirit = 475
        self.defense.dodge = 15

        self.critical_chance = 25
       
        self.regeneration.ki = 3
