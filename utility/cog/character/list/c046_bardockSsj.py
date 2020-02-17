"""
Super Saiyan Bardock

--

Author : DrLarck

Last update : 17/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

# ability

# passive

# SSJ bardock
class Character_046(Character):
    """
    Represents Super Saiyan Bardock
    """

    def __init__(self):
        Character.__init__(self)

        self.info.id = 46
        self.info.name = "Super Saiyan Bardock"

        self.image.image = "https://i.imgur.com/wvsYkZ3.png"
        self.image.thumb = "https://i.imgur.com/rnkhdsm.png"
        self.image.icon = "<:BardockSSJ:679002937074384896>"

        self.rarity.value = 3

        self.health.maximum = 4600

        self.damage.physical_max = 650
        self.damage.ki_max = 1200

        self.defense.armor = 700
        self.defense.spirit = 985
        self.defense.dodge = 10

        self.regeneration.ki = 10

        