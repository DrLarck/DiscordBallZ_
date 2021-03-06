"""
Represents the character 2

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
from utility.cog.character.ability.list._5_acid_explosion import Acid_explosion_5

from utility.cog.character.ability.leader.saibaiman_blue import Leader_blue_saibaiman
from utility.cog.character.ability.effect.buff.saibaiman_last_will_acid import Buff_last_will_acid

# blue saibaiman
class Character_002(Character):
    """
    Represents a Blue Saibaiman
    """

    def __init__(self):
        # inheritance
        Character.__init__(self)

        # stats
        self.info.id = 2
        self.info.name = "Blue Saibaiman"
        self.info.saga = "Saiyan"
        self.rarity.value = 0

        # image
        self.image.icon = "<:saibaiman_b:589492373130706964>"
        self.image.image = "https://i.imgur.com/syjNBd2.png"
        self.image.thumb = "https://i.imgur.com/wcKoXiB.png"

        # health
        self.health.maximum = 4250
        self.health.current = 4250

        # damage
        self.damage.physical_max = 250
        self.damage.ki_max = 400

        # def
        self.defense.armor = 700
        self.defense.spirit = 625
        self.defense.dodge = 20

        # crit
        self.critical_chance = 10
        
        #ki regeneration
        self.regeneration.ki = 2

        # ability
        self.ability = [Sequence_1, Ki_charge_2, Defend_3, Acid_4, Acid_explosion_5]
        self.passive_start = [Buff_last_will_acid]
        self.leader = [Leader_blue_saibaiman]
