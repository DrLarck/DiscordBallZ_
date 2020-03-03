"""
Represents the Derusting passive

--

Author : DrLarck

Last update : 03/03/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.ability._effect import Effect
from utility.cog.character.ability.util.effect_checker import Effect_checker
from utility.cog.character.ability.effect.buff.derusting import Buff_derusting

# abilities
from utility.cog.character.ability.list._21_mechanical_strike import Mechanical_strike_21

class Passive_derusting(Effect):
    """
    Represents the Derusting passive
    """

    def __init__(self, client, ctx, carrier, team_a, team_b):
        Effect.__init__(self, client, ctx, carrier, team_a, team_b)

        self.name = "Derusting"
        self.description = "Each stack of **[Derusting]** grants this unit **+5 %** stats. New abilities are unlocked based on the number of active **[Derusting]** stacks on this unit."

    async def apply(self):
        """
        Each stack of [Derusting] grants this unit +5 % stats. New abilities are unlocked based on the number of active [Derusting] stacks on this unit.
        """

        # init
        checker = Effect_checker(self.carrier)
        reference = Buff_derusting(self.client, self.ctx, self.carrier, self.team_a, self.team_b)

        # get the active derusting buff on the target
        derusting = await checker.get_buff(reference)

        # if the target has the buff
        if not derusting is None:
            # add ability based on the stacks
            if(derusting.stack < 2):  # only have derusting as ability
                from utility.cog.character.ability.list._20_derusting import Derusting_20
                self.carrier.ability = [Derusting_20]
            
            if(derusting.stack >= 2):  # add mechanical strike to the abilities
                from utility.cog.character.ability.list._20_derusting import Derusting_20
                from utility.cog.character.ability.list._21_mechanical_strike import Mechanical_strike_21

                self.carrier.ability = [Derusting_20, Mechanical_strike_21]
        
        return