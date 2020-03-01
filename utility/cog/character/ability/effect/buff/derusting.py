"""
Derusting buff

--

Author : DrLarck

Last update : 01/03/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.ability._effect import Effect
from utility.cog.character.getter import Character_getter

class Buff_derusting(Effect):
    """
    Represents the derusting buff
    """

    def __init__(self, client, ctx, carrier, team_a, team_b):
        Effect.__init__(self, client, ctx, carrier, team_a, team_b)

        self.name = "Derusting"
        self.id = 15

        self.is_permanent = True
    
    async def apply(self):
        """
        `coroutine`

        Increase the carrier's stats by 5 % per active stacks
        """

        # init
        getter = Character_getter()
        hp_bonus, physical_bonus, ki_bonus, armor_bonus, spirit_bonus = 0, 0, 0, 0, 0

        # get reference character
        reference = await getter.get_character(self.carrier.info.id)
        reference.level = self.carrier.level
        reference.rarity.value = self.carrier.rarity.value

        await reference.init()

        # get the bonus
        hp_bonus = self.carrier.health.maximum * 0.05
        physical_bonus = self.carrier.damage.physical_max * 0.05
        ki_bonus = self.carrier.damage.ki_max * 0.05
        armor_bonus = self.carrier.defense.armor * 0.05
        spirit_bonus = self.carrier.defense.spirit * 0.05

        # apply the bonus
        self.carrier.health.maximum += hp_bonus

        self.carrier.damage.physical_max += physical_bonus
        self.carrier.damage.physical_min += physical_bonus

        self.carrier.damage.ki_max += ki_bonus
        self.carrier.damage.ki_min += ki_bonus

        self.carrier.defense.armor += armor_bonus
        self.carrier.defense.spirit += spirit_bonus
        
        return