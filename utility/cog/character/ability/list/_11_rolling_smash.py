"""
Manages the rolling smash ability.

--

Author : DrLarck

Last update : 28/02/20 (DrLarck)
"""

# dependancies
import asyncio
from random import randint

# util
from utility.cog.character.ability.ability import Ability

from utility.cog.combat_system.damage.calculator import Damage_calculator

from utility.cog.displayer.move import Move_displayer

# ability
class Rolling_smash_11(Ability):
    """
    Deal physical damage and ignore the damage reduction.

    CD : 4 Turn
    """

    # attribute
    def __init__(self, client, ctx, caster, target, team_a, team_b):
        # inheritance
        Ability.__init__(
            self,
            client,
            ctx,
            caster,
            target,
            team_a,
            team_b
        )

        # stat
        self.name = "Rolling smash"
        self.description = f"""Inflicts **150 %** of your :punch: damage. Ignores target's damage reduction.
{self.game_icon['cooldown']}**Cooldown** : **4** turns."""
        self.icon = self.game_icon['ability']['rolling_smash']
        self.id = 11

        self.cost = 0
        self.cooldown = 0  # can be used at first turn

        # targetting
        self.need_target = True
        self.target_enemy = True

        self.damage.physical = 150
    
    # method
    async def set_tooltip(self):
        self.tooltip = f"Inflicts **{int(self.caster.damage.physical_min * 1.5):,}** - **{int(self.caster.damage.physical_max * 1.5):,}** :punch: and ignores the target's damage reduction."

        return
        
    async def use(self):
        """
        `coroutine`

        Inflicts 150 % of the character's physical damage and ignore the damage reduction.

        Cooldown : 4 turns.

        --

        Return : str
        """

        # init
        display = ""
        damager = Damage_calculator()
        damage = await self.get_damage()
        
        # inflict the damage to the target
        display = await damager.inflict_damage(self.caster, self.target, damage)

        # set the cooldown
        self.cooldown = 4

        return(display)