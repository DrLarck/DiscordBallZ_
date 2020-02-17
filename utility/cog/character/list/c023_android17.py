"""
Represents Android 17

--

Author : Zyorhist

Last update : 17/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

class Character_023(Character):
    """
    Represents the Android 17 unit from the Android saga.
    """

    def __init__(self):
        Character.__init__(self)

        # info
        self.info.name = "Android 17"
        self.image.image = "https://i.imgur.com/rXPG331.png"
        self.image.thumb = "https://i.imgur.com/rD88SRO.png"
        self.image.icon = "<:Android17:678951186052939797>"
        self.info.id = 23
        self.info.saga = "Android"

        # stat
        self.health.maximum = 3500
        
        self.damage.physical_max = 400
        self.damage.ki_max = 625

        self.defense.armor = 475
        self.defense.spirit = 550
        self.defense.dodge = 25

        self.critical_chance = 15
       
        self.regeneration.ki = 100
