"""
Super Saiyan Bardock

--

Author : DrLarck

Last update : 01/03/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

# ability
from utility.cog.character.ability.list._1_sequence import Sequence_1
from utility.cog.character.ability.list._2_ki_charge import Ki_charge_2
from utility.cog.character.ability.list._3_defend import Defend_3
from utility.cog.character.ability.list._17_ki_blast import Ki_blast_17
from utility.cog.character.ability.list._18_spiritual_final_canon import Spiritual_final_canon_18
from utility.cog.character.ability.list._19_saiyan_spirit import Saiyan_spirit_19

# passive
from utility.cog.character.ability.passive.courage import Passive_courage

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
        self.damage.ki_max = 1150

        self.defense.armor = 700
        self.defense.spirit = 985
        self.defense.dodge = 10

        self.regeneration.ki = 4

        self.ability = [Sequence_1, Ki_charge_2, Defend_3, Ki_blast_17, Spiritual_final_canon_18, Saiyan_spirit_19]

        self.passive_start = [Passive_courage]