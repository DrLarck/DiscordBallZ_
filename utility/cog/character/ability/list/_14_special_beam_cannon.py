"""
Manages the special beam canon ability

--

Author : Zyorhist

Last update : 29/02/20 (DrLarck)
"""

# dependancies
import asyncio
from random import randint

# util
from utility.cog.character.ability.ability import Ability

from utility.cog.combat_system.damage.calculator import Damage_calculator

# ability
class Special_beam_cannon_14(Ability):
    """
    Deal true damage to opponent
    
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
        self.name = "Special Beam Cannon"
        self.description = f"""Inflicts **50 %** of your  {self.game_icon['ki_ability']} damage as true damage"""
        self.id = 14
        
        # self.icon = self.game_icon['ability']['special_beam_cannon']

        self.cost = 40

        # targetting
        self.need_target = True
        self.target_enemy = True

        self.damage.ki = 50
    
    # method
    async def set_tooltip(self):
        self.tooltip = f"Inflicts **{int(self.caster.damage.ki_min * 0.5):,}** - **{int(self.caster.damage.ki_max * 0.5):,}** true damage."

        return
        
    async def use(self):
        """
        `coroutine`

        Inflicts 50% of users ki as true damage 

        --

        Return : str
        """

        # init
        damage_calculator = Damage_calculator()

        damage = await self.get_damage()
        
        # inflict the damage to the target
        display = await damage_calculator.inflict_damage(self.caster, self.target, damage)

        return(display)