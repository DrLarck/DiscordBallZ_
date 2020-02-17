"""
Represents Zarbon

--

Author : Zyorhist

Last update : 17/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

class Character_012(Character):
    """
    Represents the Zarbon unit from the Namek saga.
    """

    def __init__(self):
        Character.__init__(self)

        # info
        self.info.name = "Zarbon"
        self.image.image = "https://i.imgur.com/GWF5nTg.png"
        self.image.thumb = "https://i.imgur.com/9xwNjH3.png"
        self.image.icon = "<:Zarbon:678951186476433419>"
        self.info.id = 12
        self.info.saga = "Namek"

        # stat
        self.health.maximum = 2750
        
        self.damage.physical_max = 700
        self.damage.ki_max = 625

        self.defense.armor = 400
        self.defense.spirit = 400
        self.defense.dodge = 0

        self.critical_chance = 10
        self.regeneration.ki = 2