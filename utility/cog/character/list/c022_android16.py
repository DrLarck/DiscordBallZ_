"""
Represents Android 16

--

Author : Zyorhist

Last update : 17/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

class Character_022(Character):
    """
    Represents the Android 16 unit from the Android saga.
    """

    def __init__(self):
        Character.__init__(self)

        # info
        self.info.name = "Android 16"
        self.image.image = "https://i.imgur.com/6hDogxC.png"
        self.image.thumb = "https://i.imgur.com/WC0vyjK.png"
        self.image.icon = "<:Android16:678951177873915923>"
        self.info.id = 22
        self.info.saga = "Android"

        # stat
        self.health.maximum = 4250
        
        self.damage.physical_max = 550
        self.damage.ki_max = 250

        self.defense.armor = 625
        self.defense.spirit = 475
        self.defense.dodge = 15

        self.critical_chance = 5
       
        self.ki.maximum = 0
        self.regeneration.ki = 0
