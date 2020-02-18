"""
Saiyan spirit ability

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
from utility.cog.character.ability.effect.buff.saiyan_spirit import Buff_saiyan_spirit

class Saiyan_spirit(Ability):
    """
    Represents the Saiyan spirit ability
    """

    def __init__(self, client, ctx, caster, target, team_a, team_b):
        Ability.__init__(self, client, ctx, caster, target, team_a, team_b)

        self.name = "Saiyan spirit"
        self.description = f"Inflicts **200 %** of your {self.game_icon['ki_ability']} damage, increase your {self.game_icon['ki_ability']} and :punch: by **20 %** (stackable). **50 %** chance to **stun** the target."
        self.icon = self.game_icon["ability"]["saiyan_spirit"]

        self.cost = 70

        self.need_target = True
        self.target_enemy = True
    
    async def set_tooltip(self):
        self.tooltip = f"Inflicts **{int(self.caster.damage.ki_min * 3):,}** - **{int(self.caster.damage.ki_max * 3):,}** {self.game_icon['ki_ability']}. Increase your {self.game_icon['ki_ability']} and :punch: by **20 %** (stackable). **50 %** chance to **stun** the target."
    
    async def use(self):
        """
        `coroutine`

        Inflicts 200 % of your ki damage, 50 % chance to stun the target and increase your P and K by 20 %

        --

        Return : `str`
        """

        # init
        move = Move_displayer()
        damager = Damage_calculator(self.caster, self.target)

        # set damage
        damage = int(random.randint(self.caster.damage.ki_min, self.caster.damage.ki_max) * 3)
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

        # 50 % stun chance
        if(stun_roll >= 50):
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
        
        # apply saiyan spirit buff
        checker = Effect_checker(self.caster)
        saiyan_spirit_ref = Buff_saiyan_spirit(self.client, self.ctx, self.caster, self.team_a, self.team_b)
        
        saiyan_spirit_buff = await checker.get_buff(saiyan_spirit_ref)

        # if the buff has not been found
        # add it
        if(saiyan_spirit_buff == None):
            saiyan_spirit_buff = saiyan_spirit_ref
            saiyan_spirit_buff.stack = 1

            self.caster.bonus.append(saiyan_spirit_buff)
        
        # the buff is already on the caster
        # add a stack
        else:
            saiyan_spirit_buff.stack += 1
        
        return(_move)