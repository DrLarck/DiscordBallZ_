"""
Represents Dende

--

Author : Zyorhist

Last update : 06/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

class Character_020(Character):
    """
    Represents the Dende unit from the Namek saga.
    """

    def __init__(self):
        Character.__init__(self)

        # info
        self.info.name = "Dende"
        self.info.id = 20
        self.info.saga = "Namek"

        # stat
        self.health.maximum = 2375
        
        self.damage.physical_max = 400
        self.damage.ki_max = 1000

        self.defense.armor = 400
        self.defense.spirit = 475
        self.defense.dodge = 50

        self.critical_chance = 0
       
        self.regeneration.ki = 4
