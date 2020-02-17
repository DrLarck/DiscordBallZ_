"""
Represents Tien

--

Author : Zyorhist

Last update : 17/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

class Character_017(Character):
    """
    Represents the Tien unit from the Cell saga.
    """

    def __init__(self):
        Character.__init__(self)

        # info
        self.info.name = "Tien"
        self.image.image = "https://i.imgur.com/GOoa9Ve.png"
        self.info.id = 17
        self.info.saga = "Cell"

        # stat
        self.health.maximum = 2000
        
        self.damage.physical_max = 850
        self.damage.ki_max = 625

        self.defense.armor = 475
        self.defense.spirit = 400
        self.defense.dodge = 5

        self.critical_chance = 35
       
        self.regeneration.ki = 2
