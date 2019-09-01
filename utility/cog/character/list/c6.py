"""
Represents the character 6

--

Author : DrLarck

Last update : 01/09/19 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

# Bardock
class Character_6(Character):
    """
    Represents Bardock
    """

    def __init__(self):
        # inheritance
        Character.__init__(self)

        # info
        self.info.id = 6
        self.info.name = "Bardock"
        self.info.saga = "Bardock"
        self.rarity.value = 0

        # image
        self.image.image = "https://imgur.com/FWJSzJb"
        
        # stat
        # health
        self.health.maximum = 3500
        
        # damage
        self.damage.physical_max = 475
        self.damage.ki_max = 325

        # defense
        self.defense.armor = 700
        self.defense.spirit = 550
        self.defense.dodge = 10

        # crit
        self.critical_chance = 15