"""
Manages the syphon ability

--

Author : DrLarck

Last update : 27/02/20 (DrLarck)
"""

# dependancies
import asyncio
from random import randint

# util
from utility.cog.character.ability.ability import Ability
from utility.cog.displayer.move import Move_displayer
from utility.cog.character.ability.util.effect_checker import Effect_checker
from utility.cog.combat_system.damage.calculator import Damage_calculator

# syphon
class Syphon_8(Ability):
    """
    Represents the syphon ability.

    Consums all the acid stacks on the target and inflict huge damage according to the

    target missing health.
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

        self.name = "Syphon"
        self.description = f"""Inflicts **10 % (+ 2 % of the target's Missing :hearts: per __Acid__ stacks on the target)** of your {self.game_icon['ki_ability']} damage.
Heals you for an amount of **50 %** of the damage dealt."""
        self.id = 8
        
        self.icon = self.game_icon['ability']['syphon']
        self.cost = 25

        # targetting
        self.need_target = True
        self.target_enemy = True

        self.damage.ki = 10
    
    # method
    async def set_tooltip(self):
        self.tooltip = f"Inflicts **{int(self.caster.damage.ki_min * 0.10):,}** - **{int(self.caster.damage.ki_max * 0.10):,}** (+ **2 %** of target's **Missing** :hearts:) {self.game_icon['ki_ability']}. Heals your for **50 %** of damage done."

        return

    async def use(self):
        """
        `coroutine`

        See class description.

        --

        Return : str
        """

        # init
        effect_checker = Effect_checker(self.target)
        damager = Damage_calculator()

        missing_health = self.target.health.maximum - self.target.health.current
        roll_damage = await self.get_damage()

        # check if the target has acid stack active on it
        acid = await effect_checker.get_effect(
            1,
            self.client,
            self.ctx,
            self.target,
            self.team_a,
            self.team_b
        )

        has_acid = await effect_checker.get_debuff(acid)

        if(has_acid != None):
            roll_damage.ki += int(((2 * missing_health)/100) * has_acid.stack)
            
            # remove the acid debuff to the target
            # consums it
            self.target.malus.remove(has_acid)
        
        else:  # doesn't have acid active on it
            pass
        
        # deal damage to the target
        display = await damager.inflict_damage(self.caster, self.target, roll_damage)
        
        # heal the caster
        # of 50 % of damage done
        healing = int(roll_damage.ki / 2)
        self.caster.health.current += healing
        await self.caster.health.health_limit()

        # healing display
        if(healing > 0):
            display += f"__Heal__ : +**{healing}** :hearts:\n"

        return(display)