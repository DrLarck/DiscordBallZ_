"""
Manages the character 3

--

Author : DrLarck

Last update : 28/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

# test
from utility.cog.character.ability.list._1_sequence import Sequence_1
from utility.cog.character.ability.list._2_ki_charge import Ki_charge_2
from utility.cog.character.ability.list._3_defend import Defend_3
from utility.cog.character.ability.list._4_acid import Acid_4
from utility.cog.character.ability.list._7_spreading_acid import Spreading_acid_7
from utility.cog.character.ability.list._6_paralyzing_burns import Paralyzing_burns_6

from utility.cog.character.ability.passive.saibaiman_red import Passive_red_saibaiman
from utility.cog.character.ability.leader.saibaiman_red import Leader_saibaiman_red

# Red Saibaiman
class Character_003(Character):
    """
    Represents a Red Saibaiman
    """

    def __init__(self):
        # inheritance
        Character.__init__(self)

        # info
        self.info.id = 3
        self.info.name = "Red Saibaiman"
        self.info.saga = "Saiyan"
        self.rarity.value = 0

        # image
        self.image.image = "https://i.imgur.com/mIIt7jL.png"
        self.image.thumb = "https://i.imgur.com/LEjhrtw.png"
        self.image.icon = "<:saibaiman_c:589492379447197699>"

        # stat
        # health
        self.health.maximum = 1625
        self.health.current = 1625

        # damage
        self.damage.physical_max = 475
        self.damage.ki_max = 550

        # defense
        self.defense.armor = 625
        self.defense.spirit = 475
        self.defense.dodge = 10

        # crit
        self.critical_chance = 10
        
        #ki regeneration
        self.regeneration.ki = 4

        # ability
        self.ability = [Sequence_1, Ki_charge_2, Defend_3, Acid_4, Spreading_acid_7, Paralyzing_burns_6]
        self.leader = [Leader_saibaiman_red]
        self.passive_start = [Passive_red_saibaiman]
