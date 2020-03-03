"""
Derusting ability

--

Author : DrLarck

Last update : 03/03/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.ability.ability import Ability
from utility.cog.character.ability.util.effect_checker import Effect_checker

# effect
from utility.cog.character.ability.effect.buff.derusting import Buff_derusting

class Derusting_20(Ability):
    """
    Represents the Derusting ability
    """

    def __init__(self, client, ctx, caster, target, team_a, team_b):
        Ability.__init__(self, client, ctx, caster, target, team_a, team_b)

        self.name = "Derusting"
        self.description = f"Add a stack of **[Derusting]** to this unit."
        self.id = 20
    
    async def use(self):
        """
        `coroutine`

        Applies a stack of Derusting to this unit
        """

        # init
        display = f"__Move__ : {self.icon}`{self.name}`"
        checker = Effect_checker(self.caster)
        reference = Buff_derusting(self.client, self.ctx, self.caster, self.team_a, self.team_b)

        # check if the caster has the derusting buff
        derusting = await checker.get_buff(reference)

        if not derusting is None:  # if the caster has the buff
            derusting.stack += 1  # increase the number of stacks
        
        else:  # the caster doesn't have derusting
            self.caster.bonus.append(reference)

        return(display)