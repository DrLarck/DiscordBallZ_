"""
Represents Chiaotzu

--

Author : Zyorhist

Last update : 17/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

class Character_014(Character):
    """
    Represents the Chiaotzu unit from the Cell saga.
    """

    def __init__(self):
        Character.__init__(self)

        # info
        self.info.name = "Chiaotzu"
        self.image.image = "https://i.imgur.com/DIRvkt4.png"
        self.info.id = 14
        self.info.saga = "Cell"

        # stat
        self.health.maximum = 2000
        
        self.damage.physical_max = 325
        self.damage.ki_max = 775

        self.defense.armor = 400
        self.defense.spirit = 475
        self.defense.dodge = 25

        self.critical_chance = 00
        self.regeneration.ki = 5