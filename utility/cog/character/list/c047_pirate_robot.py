"""
Pirate robot character

--

Author : DrLarck

Last update : 01/03/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

class Character_047(Character):
    """
    Represents Pirate robot
    """

    def __init__(self):
        Character.__init__(self)

        self.info.id = 47
        self.info.name = "Pirate Robot"
        self.rarity.value = 1  # rare

        self.image.image = "https://i.imgur.com/jgseMqC.png"

        self.health.maximum = 3000

        self.damage.physical_max = 600
        
        self.defense.armor = 500
        self.defense.spirit = 420

        self.ki.maximum = 0