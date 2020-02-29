"""
Ki blast

--

Author : DrLarck

Last update : 29/02/20 (DrLarck)
"""

# dependancies
import asyncio
import random

# util
from utility.cog.character.ability.ability import Ability
from utility.cog.combat_system.damage.calculator import Damage_calculator
from utility.cog.displayer.move import Move_displayer

# Ki blast
class Ki_blast_17(Ability):
    """
    Represents the Ki blast ability
    """

    def __init__(self, client, ctx, caster, target, team_a, team_b):
        Ability.__init__(self, client, ctx, caster, target, team_a, team_b)
        
        self.name = "Ki blast"
        self.description = f"Inflicts **120 %** of your {self.game_icon['ki_ability']} damage."
        self.icon = self.game_icon["ability"]["ki_blast"]
        self.id = 17

        self.cost = 20

        self.need_target = True
        self.target_enemy = True

        self.damage.ki = 120

    async def set_tooltip(self):
        self.tooltip = f"Inflicts **{int(self.caster.damage.ki_min * 2.2):,}** - **{int(self.caster.damage.ki_max * 2.2):,}** {self.game_icon['ki_ability']}"

    async def use(self):
        """
        `coroutine`

        Inflicts 120 % of the caster's ki as damage to the target.

        --
        
        Return : `str`
        """

        # init
        damager = Damage_calculator()

        # set damage
        damage = await self.get_damage()

        # inflict damage
        display = await damager.inflict_damage(self.caster, self.target, damage)

        return(display)