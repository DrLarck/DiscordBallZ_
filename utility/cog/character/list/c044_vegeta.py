"""
Represents Vegeta

--

Author : Zyorhist

Last update : 17/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

class Character_044(Character):
    """
    Represents the Vegeta unit from the Android saga.
    """

    def __init__(self):
        Character.__init__(self)

        # info
        self.info.name = "Vegeta"
        self.image.image = "https://i.imgur.com/qM6jwW6.png"
        self.image.thumb = "https://i.imgur.com/rqt8ehJ.png"
        self.image.icon = "<:Vegeta:678951187029950475>"
        self.info.id = 44
        self.info.saga = "Android"

        # stat
        self.health.maximum = 3500
        
        self.damage.physical_max = 550
        self.damage.ki_max = 400

        self.defense.armor = 625
        self.defense.spirit = 550
        self.defense.dodge = 20

        self.critical_chance = 10
       
        self.regeneration.ki = 4
