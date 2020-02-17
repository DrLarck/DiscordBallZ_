"""
Represents Goku

--

Author : Zyorhist

Last update : 17/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

class Character_039(Character):
    """
    Represents the Goku unit from the Cell saga.
    """

    def __init__(self):
        Character.__init__(self)

        # info
        self.info.name = "Goku"
        self.image.image = "https://i.imgur.com/ZLCPJih.png"
        self.info.id = 39
        self.info.saga = "Cell"

        # stat
        self.health.maximum = 3500
        
        self.damage.physical_max = 400
        self.damage.ki_max = 550

        self.defense.armor = 625
        self.defense.spirit = 475
        self.defense.dodge = 20

        self.critical_chance = 0
       
        self.regeneration.ki = 3
