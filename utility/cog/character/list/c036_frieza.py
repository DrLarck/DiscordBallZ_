"""
Represents Frieza

--

Author : Zyorhist

Last update : 17/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

class Character_036(Character):
    """
    Represents the Frieza unit from the Namek saga.
    """

    def __init__(self):
        Character.__init__(self)

        # info
        self.info.name = "Frieza"
        self.image.image = "https://i.imgur.com/WXKCDWk.png"
        self.image.thumb = "https://i.imgur.com/tPDeXTS.png"
        self.image.icon = "<:Frieza:678951187969474560>"
        self.info.id = 36
        self.info.saga = "Namek"

        # stat
        self.health.maximum = 3500
        
        self.damage.physical_max = 850
        self.damage.ki_max = 625

        self.defense.armor = 250
        self.defense.spirit = 325
        self.defense.dodge = 25

        self.critical_chance = 5
       
        self.regeneration.ki = 2
