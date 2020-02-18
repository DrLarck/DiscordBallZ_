"""
Saiyan spirit buff object

--

Author : DrLarck

Last update : 18/02/20 (DrLarck)
"""

# dependancies
import asyncio

# config
from configuration.icon import game_icon

# util
from utility.cog.character.getter import Character_getter
from utility.cog.character.ability._effect import Effect

class Buff_saiyan_spirit(Effect):
    """
    Represents the Saiyan spirit buff
    """

    def __init__(self, client, ctx, carrier, team_a, team_b):
        Effect.__init__(self, client, ctx, carrier, team_a, team_b)

        self.name = "Saiyan spirit"
        self.icon = game_icon["effect"]["saiyan_spirit_buff"]
        
        self.id = 12

        self.is_permanent = True
    
    async def apply(self):
        """
        `coroutine`

        The carrier gains 20 % P and K infinite stack

        --

        Return : `None`
        """

        # init
        phy_bonus, ki_bonus = 0, 0
        getter = Character_getter()

        char_ref = await getter.get_character(self.carrier.info.id)
        char_ref.level = self.carrier.level
        char_ref.rarity.value = self.carrier.rarity.value

        await char_ref.init()

        phy_bonus = int(char_ref.damage.physical_max * 0.2) * self.stack
        ki_bonus = int(char_ref.damage.ki_max * 0.2) * self.stack

        # apply the bonus
        self.carrier.damage.physical_min += phy_bonus
        self.carrier.damage.physical_max += phy_bonus

        self.carrier.damage.ki_min += ki_bonus
        self.carrier.damage.ki_max += ki_bonus

        return