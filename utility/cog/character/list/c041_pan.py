"""
Represents Pan

--

Author : Zyorhist

Last update : 17/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

class Character_041(Character):
    """
    Represents the Pan unit from the Black Star Dragon Ball saga.
    """

    def __init__(self):
        Character.__init__(self)

        # info
        self.info.name = "Pan"
        self.image.image = "https://i.imgur.com/LmUkkm0.png"
        self.info.id = 41
        self.info.saga = "Black Star Dragon Ball"

        # stat
        self.health.maximum = 2000
        
        self.damage.physical_max = 325
        self.damage.ki_max = 925

        self.defense.armor = 725
        self.defense.spirit = 400
        self.defense.dodge = 10

        self.critical_chance = 15
       
        self.regeneration.ki = 5
