"""
Represents Dende

--

Author : Zyorhist

Last update : 17/02/20 (DrLarck)
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
        self.image.image = "https://i.imgur.com/XVZETFZ.png"
        self.image.thumb = "https://i.imgur.com/f2STdg0.png"
        self.image.icon = "<:Dende:678951187600375848>"
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
