"""
Represents Broly

--

Author : Zyorhist

Last update : 18/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

# ability
from utility.cog.character.ability.list.powered_shell import Powered_shell

class Character_006(Character):
    """
    Represents the Broly unit from the Broly saga.
    """

    def __init__(self):
        Character.__init__(self)

        # info
        self.info.name = "Broly"
        self.image.image = "https://i.imgur.com/LkRGDjf.png"
        self.image.thumb = "https://i.imgur.com/ukQY1s1.png"
        self.image.icon = "<:Broly:678951186090688533>"
        self.info.id = 6
        self.info.saga = "Broly"

        # stat
        self.health.maximum = 3125
        
        self.damage.physical_max = 625
        self.damage.ki_max = 475

        self.defense.armor = 550
        self.defense.spirit = 475
        self.defense.dodge = 25

        self.critical_chance = 10
       
        self.regeneration.ki = 2

        self.ability = [Powered_shell]