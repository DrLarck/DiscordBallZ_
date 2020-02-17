"""
Represents Guldo

--

Author : Zyorhist

Last update : 17/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

class Character_031(Character):
    """
    Represents the Guldo unit from the Namek saga.
    """

    def __init__(self):
        Character.__init__(self)

        # info
        self.info.name = "Guldo"
        self.image.image = "https://i.imgur.com/VLQnIoh.png"
        self.info.id = 31
        self.info.saga = "Namek"

        # stat
        self.health.maximum = 2375
        
        self.damage.physical_max = 250
        self.damage.ki_max = 1000

        self.defense.armor = 550
        self.defense.spirit = 475
        self.defense.dodge = 10

        self.critical_chance = 0
       
        self.regeneration.ki = 5
