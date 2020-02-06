"""
Represents Shugesh

--

Author : Zyorhist

Last update : 06/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

class Character_028(Character):
    """
    Represents the Shugesh unit from the Bardock saga.
    """

    def __init__(self):
        Character.__init__(self)

        # info
        self.info.name = "Shugesh"
        self.info.id = 28
        self.info.saga = "Bardock"

        # stat
        self.health.maximum = 2750
        
        self.damage.physical_max = 550
        self.damage.ki_max = 475

        self.defense.armor = 700
        self.defense.spirit = 475
        self.defense.dodge = 15

        self.critical_chance = 0
       
        self.regeneration.ki = 4
