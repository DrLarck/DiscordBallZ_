"""
Represents Hit

--

Author : Zyorhist

Last update : 17/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

class Character_018(Character):
    """
    Represents the Hit unit from the Universe 6 saga.
    """

    def __init__(self):
        Character.__init__(self)

        # info
        self.info.name = "Hit"
        self.image.image = "https://i.imgur.com/ZfwWvo3.png"
        self.info.id = 18
        self.info.saga = "Universe 6"

        # stat
        self.health.maximum = 3125
        
        self.damage.physical_max = 625
        self.damage.ki_max = 475

        self.defense.armor = 475
        self.defense.spirit = 550
        self.defense.dodge = 20

        self.critical_chance = 15
       
        self.regeneration.ki = 3
