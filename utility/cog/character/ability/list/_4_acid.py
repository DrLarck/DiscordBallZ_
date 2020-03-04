"""
Manages the Acid ability.

--

Author : DrLarck

Last update : 04/03/20 (DrLarck)
"""

# dependance
import asyncio
from random import randint

# utility
from utility.cog.displayer.move import Move_displayer
from utility.cog.combat_system.damage.calculator import Damage_calculator

from utility.cog.character.ability.ability import Ability
from utility.cog.character.ability.effect.dot.dot_acid import Dot_acid
from utility.cog.character.ability.util.effect_checker import Effect_checker

# ability
class Acid_4(Ability):
    """
    This ability applies a DOT on the target. This DOT inflicts damage
    at each turn.
    """

    # attribute
    def __init__(self, client, ctx, caster, target, team_a, team_b):
        Ability.__init__(
            self,
            client,
            ctx,
            caster,
            target,
            team_a,
            team_b
        )

        self.name = "Acid"
        self.icon = self.game_icon['ability']['acid']
        self.description = f"""Inflicts **25 %** of your {self.game_icon['ki_ability']} damage and applies a stack of **__Acid__** to the target.
Each stack of **__Acid__** inflicts an amount of **1.5 % (+ 5 % of the highest Saibaiman {self.game_icon['ki_ability']} /250 in your team)** of the target's **Maximum** :hearts: as {self.game_icon['ki_ability']} damage per stack each turn.
Lasts **3** turns."""
        self.id = 4

        self.cost = 8
        self.need_target = True
        self.target_enemy = True

        # damage
        self.damage.ki = 25
    
    # method
    async def set_tooltip(self):
        self.tooltip = f"Inflicts **{int(self.caster.damage.ki_min * 0.25):,}** - **{int(self.caster.damage.ki_max * 0.25):,}** {self.game_icon['ki_ability']} and add a stack of **__Acid__**{self.game_icon['effect']['acid']} to the target."

        return

    async def use(self):
        """
        `coroutine`

        Inflicts damage and applies a dot to the target.

        --

        Return : str
        """

        # init
        await self.caster.posture.change_posture("attacking")

        damager = Damage_calculator()

        damage = await self.get_damage()

        display = f"__Move__ : {self.icon}`{self.name}`\n"

        display += await damager.inflict_damage(self.caster, self.target, damage)

        # add a stack of acid on the target
        _acid = Dot_acid(
            self.client,
            self.ctx,
            self.target,
            self.team_a,
            self.team_b
        )

        await _acid.add_stack()

        return(display)