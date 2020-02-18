"""
Courage passive object

--

Author : DrLarck

Last update : 18/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.ability._effect import Effect
from utility.cog.character.ability.util.effect_checker import Effect_checker
from utility.cog.character.getter import Character_getter

# effect
from utility.cog.character.ability.effect.buff.courage import Buff_courage

class Passive_courage(Effect):
    """
    Represents the Courage passive
    """

    def __init__(self, client, ctx, carrier, team_a, team_b):
        Effect.__init__(self, client, ctx, carrier, team_a, team_b)

        self.name = "Courage"
        self.icon = self.game_icon["effect"]["bardock_ssj_courage"]
        self.description = f"Gains **100 %** of its {self.game_icon['ki_ability']} and :punch: at the **beginning** of the turn for **10** turns. Gains **1 %** {self.game_icon['ki_ability']} and :punch: per **Max health**:hearts: **%** lost."

        # private
        self.applied_buff = False

    async def apply(self):
        """
        `coroutine`

        Gains 100 % K and P fort 10 turns and increase carrier's stats by 4 % per % MH lost

        --

        Return : `None`
        """

        # init
        courage = Buff_courage(self.client, self.ctx, self.carrier, self.team_a, self.team_b)
        checker = Effect_checker(self.carrier)
        getter = Character_getter()
        phy_bonus, ki_bonus = 0, 0
        carrier_ref = await getter.get_character(self.carrier.info.id)

        carrier_ref.level = self.carrier.level
        carrier_ref.rarity.value = self.carrier.rarity.value
        await carrier_ref.init()

        # if the passive has not applied courage yet
        if not self.applied_buff:
            self.carrier.bonus.append(courage)
            self.applied_buff = True
        
        # now calculate the bonus
        missing_percent = int((self.carrier.health.current * 100) / self.carrier.health.maximum)

        phy_bonus = int((carrier_ref.damage.physical_max  * 0.04) * missing_percent)
        ki_bonus = int((carrier_ref.damage.ki_max  * 0.04) * missing_percent)

        # apply bonus
        self.carrier.damage.physical_min += phy_bonus
        self.carrier.damage.physical_max += phy_bonus

        self.carrier.damage.ki_min += ki_bonus
        self.carrier.damage.ki_max += ki_bonus

        return