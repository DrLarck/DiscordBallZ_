"""
Pirate robot character

--

Author : DrLarck

Last update : 04/03/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

# passive
from utility.cog.character.ability.passive.derusting import Passive_derusting

# ability
from utility.cog.character.ability.list._20_derusting import Derusting_20

class Character_005(Character):
    """
    Represents Pirate robot
    """

    def __init__(self):
        Character.__init__(self)

        self.info.id = 5
        self.info.name = "Pirate Robot"
        self.rarity.value = 1  # rare

        self.image.image = "https://i.imgur.com/jgseMqC.png"
        self.image.icon = "<:PirateRobot:684784065483636756>"
        self.image.thumb = "https://i.imgur.com/JwEHf59.png"

        self.health.maximum = 2000

        self.damage.physical_max = 400
        
        self.defense.armor = 500
        self.defense.spirit = 420

        self.ki.maximum = 0

        self.passive_start = [Passive_derusting]
        self.ability = [Derusting_20]