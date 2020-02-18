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
        

        return