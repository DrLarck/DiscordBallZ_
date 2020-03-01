"""
Manages the character 5

--

Author : DrLarck

Last update : 29/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

# ability
from utility.cog.character.ability.list._1_sequence import Sequence_1
from utility.cog.character.ability.list._2_ki_charge import Ki_charge_2
from utility.cog.character.ability.list._3_defend import Defend_3
from utility.cog.character.ability.list._13_arm_stretch import Arm_stretch_13
from utility.cog.character.ability.list._14_special_beam_cannon import Special_beam_cannon_14

# Piccolo
class Character_005(Character):
    """
    Represents Picolo
    """

    def __init__(self):
        # inheritance
        Character.__init__(self)

        # info
        self.info.id = 5
        self.info.name = "Piccolo"
        self.info.saga = "Saiyan"
        self.rarity.value = 0

        # image
        self.image.image = "https://i.imgur.com/pCv2cyO.png"
        self.image.thumb = "https://i.imgur.com/kDoU9ZH.png"
        self.image.icon = "<:piccolo:619492513673248778>"

        # stat
        # health
        self.health.maximum = 3875
        
        # damage 
        self.damage.physical_max = 325
        self.damage.ki_max = 400

        # defense
        self.defense.armor = 625
        self.defense.spirit = 625
        self.defense.dodge = 10

        # crit
        self.critical_chance = 10

        self.ability = [Sequence_1, Ki_charge_2, Defend_3, Arm_stretch_13, Special_beam_cannon_14]