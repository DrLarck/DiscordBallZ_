"""
Eraser canon ability object

--

Author : DrLarck

Last update : 18/02/20 (DrLarck)
"""

# dependancies
import asyncio
import random

# util
from utility.cog.character.ability.ability import Ability
from utility.cog.fight_system.calculator.damage import Damage_calculator
from utility.cog.character.ability.util.effect_checker import Effect_checker
from utility.cog.displayer.move import Move_displayer

# effect
from utility.cog.character.ability.effect.debuff.stun import Stun

class Eraser_canon(Ability):
    """
    Represents the Eraser canon ability
    """

    def __init__(self, client, ctx, caster, target, team_a, team_b):
        Ability.__init__(self, client, ctx, caster, target, team_a, team_b)

        self.name = "Eraser canon"
        self.description = f"Inflicts **15 %** of your {self.game_icon['ki_ability']} damage to **all** enemies. Stun them for **1** turn."
        self.icon = self.game_icon["ability"]["eraser_canon"]

        self.cost = 75
    
    async def set_tooltip(self):
        self.tooltip = f"Inflicts **{int(self.caster.damage.ki_min * 1.15):,}** - **{int(self.caster.damage.ki_max * 1.15):,}** {self.game_icon['ki_ability']} damage to **all** enemies. **Stun** them for **1** turn."
    
    async def use(self):
        """
        `coroutine`

        Inflicts 15 % of your ki all the enemy team, stun them for 1 turn

        --

        Return : `str`
        """

        # init
        damage = random.randint(int(self.caster.damage.ki_min * 1.15), int(self.caster.damage.ki_max * 1.15))
        final_move = f"__Move__ : `{self.name}`{self.icon}\n__Damage__ : \n"

        for enemy in self.team_b:
            await asyncio.sleep(0)

            # init for the enemy
            stun = Stun(self.client, self.ctx, enemy, self.team_a, self.team_b)
            checker = Effect_checker(enemy)
            damager = Damage_calculator(self.caster, enemy)

            # inflict the damage
            damage_dict = await damager.ki_damage(damage)

            final_move += f"{enemy.image.icon}**{enemy.info.name}**{enemy.type.icon} -**{damage_dict['calculated']:,}** {self.game_icon['ki_ability']}\n"

            await enemy.receive_damage(damage_dict['calculated'])

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