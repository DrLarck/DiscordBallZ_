"""
Defend ability

--

Author : DrLarck

Last update : 25/02/20 (DrLarck)
"""

# dependancies
import asyncio
import random

# util
from utility.cog.character.ability.ability import Ability

class Defend_3(Ability):
    """
    Represents the defend ability
    """

    def __init__(self, client, ctx, caster, target, team_a, team_b):
        Ability.__init__(self, client, ctx, caster, target, team_a, team_b)

        self.name = "Defend"
        self.description = "The unit's posture changes to **Defending**."
        self.icon = ":shield:"
        self.id = 3

    async def set_tooltip(self):
        self.tooltip = "The unit's posture changes to **Defending**."
    
    async def use(self):
        await self.caster.posture.change_posture("defending")

        display = f"__Move__ : :shield:`{self.name}`"

        return(display)