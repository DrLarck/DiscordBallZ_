"""
Represents Burter

--

Author : Zyorhist

Last update : 17/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

class Character_032(Character):
    """
    Represents the Burter unit from the Namek saga.
    """

    def __init__(self):
        Character.__init__(self)

        # info
        self.info.name = "Burter"
        self.image.image = "https://i.imgur.com/0NmIqJE.png"
        self.info.id = 32
        self.info.saga = "Namek"

        # stat
        self.health.maximum = 2750
        
        self.damage.physical_max = 925
        self.damage.ki_max = 475

        self.defense.armor = 400
        self.defense.spirit = 400
        self.defense.dodge = 15

        self.critical_chance = 15
       
        self.regeneration.ki = 2
