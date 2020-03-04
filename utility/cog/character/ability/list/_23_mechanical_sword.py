"""
Mechanical sword ability

--

Author : DrLarck

Last update : 04/03/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.combat_system.damage.calculator import Damage_calculator
from utility.cog.character.ability.ability import Ability

class Mechanical_sword_23(Ability):
    """
    Represents the Mechanical sword ability
    """

    def __init__(self, client, ctx, caster, target, team_a, team_b):
        Ability.__init__(self, client, ctx, caster, target, team_a, team_b)
        
        self.name = "Mechanical sword"
        self.description = "Inflicts physical damage to the target."
        self.id = 23

        self.icon = self.game_icon["ability"]["mechanical_sword"]

        self.need_target = True
        self.target_enemy = True

        self.damage.physical = 110
    
    async def set_tooltip(self):
        self.tooltip = f"Inflicts **{int(self.caster.damage.physical_min * 1.1):,}** - **{int(self.caster.damage.physical_max * 1.1):,}**:punch: to the target."
    
    async def use(self):
        """
        Inflicts 150 % physical to the target
        """

        # init
        damager = Damage_calculator()
        damage = await self.get_damage()

        display = f"__Move__ : {self.icon}`{self.name}`\n"
        display += await damager.inflict_damage(self.caster, self.target, damage)

        return(display)