"""
Represents Android 18

--

Author : Zyorhist

Last update : 17/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

class Character_024(Character):
    """
    Represents the Android 18 unit from the Android saga.
    """

    def __init__(self):
        Character.__init__(self)

        # info
        self.info.name = "Android 18"
        self.image.image = "https://i.imgur.com/7Be5WNO.png"
        self.image.thumb = "https://i.imgur.com/Cz4l3BE.png"
        self.image.icon = "<:Android18:678951186455461918>"
        self.info.id = 24
        self.info.saga = "Android"

        # stat
        self.health.maximum = 2000
        
        self.damage.physical_max = 625
        self.damage.ki_max = 775

        self.defense.armor = 400
        self.defense.spirit = 550
        self.defense.dodge = 10

        self.critical_chance = 30
        self.regeneration.ki = 100
