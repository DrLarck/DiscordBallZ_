"""
Eraser canon ability object

--

Author : DrLarck

Last update : 01/03/20 (DrLarck)
"""

# dependancies
import asyncio
import random

# util
from utility.cog.character.ability.ability import Ability
from utility.cog.combat_system.damage.calculator import Damage_calculator
from utility.cog.character.ability.util.effect_checker import Effect_checker
from utility.cog.displayer.move import Move_displayer

# effect
from utility.cog.character.ability.effect.debuff.stun import Stun

class Eraser_canon_15(Ability):
    """
    Represents the Eraser canon ability
    """

    def __init__(self, client, ctx, caster, target, team_a, team_b):
        Ability.__init__(self, client, ctx, caster, target, team_a, team_b)

        self.name = "Eraser canon"
        self.description = f"Inflicts **15 %** of your {self.game_icon['ki_ability']} damage to **all** enemies. Stun them for **1** turn."
        self.icon = self.game_icon["ability"]["eraser_canon"]
        self.id = 15

        self.cost = 75

        self.damage.ki = 15
    
    async def set_tooltip(self):
        self.tooltip = f"Inflicts **{int(self.caster.damage.ki_min * 0.15):,}** - **{int(self.caster.damage.ki_max * 0.15):,}** {self.game_icon['ki_ability']} damage to **all** enemies. **Stun** them for **1** turn."
    
    async def use(self):
        """
        `coroutine`

        Inflicts 15 % of your ki all the enemy team, stun them for 1 turn

        --

        Return : `str`
        """

        # init
        damage = await self.get_damage()
        final_move = f"__Move__ : `{self.name}`{self.icon}\n__Damage__ : \n"

        for enemy in self.team_b:
            await asyncio.sleep(0)

            # init for the enemy
            stun = Stun(self.client, self.ctx, enemy, self.team_a, self.team_b)
            checker = Effect_checker(enemy)
            damager = Damage_calculator()

            # inflict the damage
            _damage = await damager.inflict_damage(self.caster, enemy, damage)

            final_move += f"{enemy.image.icon}**{enemy.info.name}**{enemy.type.icon} -**{damage.ki:,}** {self.game_icon['ki_ability']}\n"

            # check if the enemy is stun
            # if the enmy isn't stun, stun it
            has_stun = await checker.get_debuff(stun)

            if(has_stun == None):  # not stun
                stun.initial_duration = 1
                stun.duration = 1
                enemy.malus.append(stun)

                await enemy.posture.change_posture("stunned")
            
            else:  # is stun, reset duration
                has_stun.duration = has_stun.initial_duration
        
        return(final_move)