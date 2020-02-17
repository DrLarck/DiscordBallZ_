"""
Represents Hercule Satan

--

Author : Zyorhist

Last update : 17/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

class Character_013(Character):
    """
    Represents the Hercule Satan unit from the Android saga.
    """

    def __init__(self):
        Character.__init__(self)

        # info
        self.info.name = "Hercule"
        self.image.image = "https://i.imgur.com/c3UQFit.png"
        self.image.thumb = "https://i.imgur.com/upO4Hne.png"
        self.image.icon = "<:Hercule:678951186413387776>"
        self.info.id = 13
        self.info.saga = "Cell"

        # stat
        self.health.maximum = 2000
        
        self.damage.physical_max = 325
        self.damage.ki_max = 250

        self.defense.armor = 1000
        self.defense.spirit = 775
        self.defense.dodge = 25

        self.critical_chance = 0
       
        self.regeneration.ki = 5
