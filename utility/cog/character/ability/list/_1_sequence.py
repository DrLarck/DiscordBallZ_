"""
Manages the Sequence ability

--

Author : DrLarck

Last update : 04/03/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.combat_system.damage.calculator import Damage_calculator
from utility.cog.character.ability.ability import Ability

class Sequence_1(Ability):
    """
    Global sequence ability
    """

    def __init__(self, client, ctx, caster, target, team_a, team_b):
        Ability.__init__(self, client, ctx, caster, target ,team_a, team_b)

        self.name = "Sequence"
        self.description = "The unit performs a **Sequence** attack, inflicting physical damage."
        self.icon = ":punch:"
        self.id = 1

        # targeting
        self.need_target = True
        self.target_enemy = True

        # damage
        self.damage.physical = 100

    async def set_tooltip(self):
        self.tooltip = f"Inflicts **{int(self.caster.damage.physical_min):,}** - **{int(self.caster.damage.physical_max):,}** :punch: to the target."
    
    async def use(self):
        damager = Damage_calculator()
        damage = await self.get_damage()

        display = f"__Move__ : {self.icon}`{self.name}`\n"

        display = await damager.inflict_damage(self.caster, self.target, damage)

        return(display)