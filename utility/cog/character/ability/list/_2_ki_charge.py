"""
Ki charage ability

--

Author : DrLarck

Last update : 25/02/20 (DrLarck)
"""

# dependancies
import asyncio
import random

# util
from utility.cog.character.ability.ability import Ability

class Ki_charge_2(Ability):
    """
    Represents the global Ki charge ability
    """

    def __init__(self, client, ctx, caster, target, team_a, team_b):
        Ability.__init__(self, client, ctx, caster, target, team_a, team_b)

        self.name = "Ki charge"
        self.description = "The unit regenerates its **Ki** points."
        self.icon = ":fire:"
        self.id = 2

    async def set_tooltip(self):
        # get the missing ki
        missing_ki = self.caster.ki.maximum - self.caster.ki.current
            # take 10 % of the missing ki
        missing_ki *= 0.1

        # get the ki gain
        # based on misisng ki and rarity of the character
        ki_gain = int(self.caster.rarity.value + missing_ki)

        self.tooltip = f"Generates **{ki_gain:,}** - **{ki_gain + 5:,}**:fire: ki points."
    
    async def use(self):
        # changing posture
        await self.caster.posture.change_posture("charging")

        # get the missing ki
        missing_ki = self.caster.ki.maximum - self.caster.ki.current
            # take 10 % of the missing ki
        missing_ki *= 0.1

        # get the ki gain
        # based on misisng ki and rarity of the character
        ki_gain = int(random.randint(1, 5) + self.caster.rarity.value + missing_ki)

        # add the ki to the character
        self.caster.ki.current += ki_gain

        await self.caster.ki.ki_limit()

        display = f"__Move__ : {self.icon}`{self.name}`\n__Ki__ : **+{ki_gain:,}**:fire:"

        return(display)