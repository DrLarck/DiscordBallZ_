"""
Represents Android 19

--

Author : Zyorhist

Last update : 17/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

class Character_025(Character):
    """
    Represents the Android 19 unit from the Android saga.
    """

    def __init__(self):
        Character.__init__(self)

        # info
        self.info.name = "Android 19"
        self.image.image = "https://i.imgur.com/UjzHDP4.png"
        self.image.thumb = "https://i.imgur.com/HsVVQgR.png"
        self.image.icon = "<:Android19:678951187051053059>"
        self.info.id = 25
        self.info.saga = "Android"

        # stat
        self.health.maximum = 4625
        
        self.damage.physical_max = 400
        self.damage.ki_max = 250

        self.defense.armor = 550
        self.defense.spirit = 625
        self.defense.dodge = 10

        self.critical_chance = 0
       
        self.regeneration.ki = 7
