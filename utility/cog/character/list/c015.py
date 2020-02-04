"""
Represents Android 18

--

Author : Zyorhist

Last update : 03/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

class Character_015(Character):
    """
    Represents the Killa unit from the Majin Buu saga.
    """

    def __init__(self):
        Character.__init__(self)

        # info
        self.info.name = "Killa"
        self.info.id = 15
        self.info.saga = "Buu"

        # stat
        self.health.maximum = 3500
        
        self.damage.physical_max = 925
        self.damage.ki_max = 250

        self.defense.armor = 475
        self.defense.spirit = 400
        self.defense.dodge = 10

        self.critical_chance = 20

        # this unit does not have ki
        self.ki.maximum = 0
        self.regeneration.ki = 0