"""
Powered shell buff object

--

Author : DrLarck

Last update : 18/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.ability._effect import Effect
from utility.cog.character.getter import Character_getter

class Buff_powered_shell(Effect):
    """
    Represents the Powered shell buff
    """

    def __init__(self, client, ctx, carrier, team_a, team_b):
        Effect.__init__(self, client, ctx, carrier, team_a, team_b)

        self.name = "Powered shell"
        self.icon = self.game_icon["effect"]["powered_shell_buff"]
        self.id = 14

        self.initial_duration = 5
        
    async def apply(self):
        """
        `coroutine`

        Increase the defense of the carrier by 10 % for 5 turns

        --

        Return : `None`
        """

        # init
        armor_bonus, spirit_bonus = 0, 0
        getter = Character_getter()

        # init the reference
        carrier_ref = await getter.get_character(self.carrier.info.id)

        carrier_ref.level = self.carrier.level
        carrier_ref.rarity.value = self.carrier.rarity.value

        await carrier_ref.init()

        # calculate the bonus
        armor_bonus = int(carrier_ref.defense.armor * 0.1)
        spirit_bonus = int(carrier_ref.defense.spirit * 0.1)

        # apply the bonus
        self.carrier.defense.armor += armor_bonus
        self.carrier.defense.spirit += spirit_bonus

        return