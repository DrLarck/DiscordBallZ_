"""
Courage buff object

--

Author : DrLarck

Last update : 18/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.ability._effect import Effect
from utility.cog.character.getter import Character_getter

class Buff_courage(Effect):
    """
    Represents the courage buff
    """

    def __init__(self, client, ctx, carrier, team_a, team_b):
        Effect.__init__(self, client, ctx, carrier, team_a, team_b)

        self.name = "Courage"
        self.icon = self.game_icon["effect"]["bardock_ssj_courage"]

        self.id = 13

        self.initial_duration = 10
        self.duration = 10

    async def apply(self):
        """
        `coroutine`

        Increase the carrier P and K by 100 % for 10 turns
        """

        # init
        getter = Character_getter()
        ki_bonus, phy_bonus = 0, 0

        # get reference for bonus stats
        carrier_ref = await getter.get_character(self.carrier.info.id)
        carrier_ref.level = self.carrier.level
        carrier_ref.rarity.value = self.carrier.rarity.value

        await carrier_ref.init()

        # calculate the bonus
        ki_bonus = carrier_ref.damage.ki_max
        phy_bonus = carrier_ref.damage.physical_max 

        # add the bonus
        self.carrier.damage.physical_min += phy_bonus
        self.carrier.damage.physical_max += phy_bonus

        self.carrier.damage.ki_min += ki_bonus
        self.carrier.damage.ki_max += ki_bonus

        return