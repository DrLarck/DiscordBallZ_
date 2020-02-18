"""
Spiritual final canon ability

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
from utility.cog.displayer.move import Move_displayer
from utility.cog.character.ability.util.effect_checker import Effect_checker

# effect
from utility.cog.character.ability.effect.debuff.stun import Stun

class Spiritual_final_canon(Ability):
    """
    Represents the spiritual final canon ability
    """

    def __init__(self, client, ctx, caster, target, team_a, team_b):
        Ability.__init__(self, client, ctx, caster, target, team_a, team_b)

        self.name = "Spiritual final canon"
        self.description = f"Inflicts **150 %** of your {self.game_icon['ki_ability']} damage. **30 %** chance to **stun** the target during **1** turn."
        self.icon = self.game_icon["ability"]["spiritual_final_canon"]

        self.cost = 45

        self.need_target = True
        self.target_enemy = True
    
    async def set_tooltip(self):
        self.tooltip = f"Inflicts **{int(self.caster.damage.ki_min * 2.5):,}** - **{int(self.caster.damage.ki_max * 2.5):,}** {self.game_icon['ki_ability']}. **30 %** chance to stun the target during **1** turn."
    
    async def use(self):
        """
        `coroutine`

        Inflicts 150 % of the caster's damage to the target. 30 % chance to stun for 1 turn

        --

        Return : `str`
        """

        # init
        move = Move_displayer()
        damager = Damage_calculator(self.caster, self.target)

        # set damage
        damage = int(random.randint(self.caster.damage.ki_min, self.caster.damage.ki_max) * 2.5)
        damage = await damager.ki_damage(damage, critable = True, dodgable = True)

        _move = await move.get_new_move()

        _move["name"] = self.name
        _move["icon"] = self.icon
        _move["damage"] = damage["calculated"]
        _move["critical"] = damage["critical"]
        _move["dodge"] = damage["dodge"]
        _move["ki"] = True

        _move = await move.offensive_move(_move)

        # inflict damage
        await self.target.receive_damage(damage["calculated"], self.caster)

        # roll stun
        stun_roll = random.randint(0, 100)

        # 30 % stun chance
        if(stun_roll >= 30):
            # stun the target
            # for 1 turn
            checker = Effect_checker(self.target)
            stun_ref = Stun(self.client, self.ctx, self.target, self.team_a, self.team_b)

            has_stun = await checker.get_debuff(stun_ref)

            # if the target is not stun
            if(has_stun == None):
                # apply the stun to the target
                stun_ref.initial_duration = 1
                stun_ref.duration = 1

                self.target.malus.append(stun_ref)

                await self.target.posture.change_posture("stunned")

            _move += "__Special__ : The target is **stunned** for 1 turn"

        return(_move)