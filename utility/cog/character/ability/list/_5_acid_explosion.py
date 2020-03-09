"""
Manages the Acid Explosion ability.

--

Author : DrLarck

Last update : 04/03/20 (DrLarck)
"""

# dependancies
import asyncio
from random import randint

# util
from utility.cog.character.ability.ability import Ability
from utility.cog.combat_system.damage.calculator import Damage_calculator
from utility.cog.character.ability.util.effect_checker import Effect_checker

# acid explosion
class Acid_explosion_5(Ability):
    """
    Represents the Acid explosion ability.
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

        self.name = "Acid explosion"
        self.description = f"""Inflicts **50 %** of your {self.game_icon['ki_ability']} damage.
If the target has at least **3** stacks of **__Acid__** : **Add** a stack of **__Acid__** to all the target's team members.
Applies the **__Acid explosion__** malus to the **main target** which will reduce the target's :rosette: by **2 %** : Lasts **2** turns."""
        self.id = 5

        self.icon = self.game_icon['ability']['acid_explosion']
        self.cost = 30

        self.need_target = True
        self.target_enemy = True

        self.damage.ki = 50
    
    # method
    async def set_tooltip(self):
        self.tooltip = f"Inflicts **{int(self.caster.damage.ki_min * 0.50):,}** - **{int(self.caster.damage.ki_max * 0.50):,}** {self.game_icon['ki_ability']}.\nIf the target has at least **3** stacks of **__Acid__**{self.game_icon['effect']['acid']} applies **__Acid Explosion__**{self.game_icon['effect']['acid_explosion']} malus to the target wich reduces its **Spirit**:rosette: by **2 %**."

        return

    async def use(self):
        """
        `coroutine`

        Inflicts 50 % of the caster's ki damage to the target.

        If the target has at least 3 stacks of acid, splashes it onto all of the target's team members.

        Applies the Acid explosion debuff that increases the ki damages that they take by 2 %.

        --

        Return : str
        """

        # init
        effect_checker = Effect_checker(self.target)
        damager = Damage_calculator()
        
        # debuff
        acid_ref = await effect_checker.get_effect(
            1,
            self.client,
            self.ctx,
            self.target,
            self.team_a,
            self.team_b
        )

        explosion_ref = await effect_checker.get_effect(
            3,
            self.client,
            self.ctx,
            self.target,
            self.team_a,
            self.team_b
        )

        # set the damage
        damage = await self.get_damage()

        # check if the target has acid
        has_acid = await effect_checker.get_debuff(acid_ref)

        if(has_acid != None):  # the target has an acid dot active on it
            # now check if the target has at least 3 stacks of acid
            if(has_acid.stack >= 3):
                # spread the dot onto the enemy members
                
                for unit in self.team_b:
                    await asyncio.sleep(0)

                    # init
                    effect_checker = Effect_checker(unit)

                    # check if the unit has acid stack
                    unit_has_acid = await effect_checker.get_debuff(acid_ref)

                    if(unit_has_acid != None):
                        await unit_has_acid.add_stack()
                        unit_has_acid.duration = unit_has_acid.initial_duration
                    
                    else:  # the unit doesn't have acid active on it
                        # create a new acid instance for the target
                        unit_acid = await effect_checker.get_effect(
                            1,
                            self.client,
                            self.ctx,
                            unit,
                            self.team_a,
                            self.team_b
                        )
                        # applies the new acid instance
                        await unit_acid.add_stack()
        
        # now check if the target already have explosion debuff active
        has_explosion = await effect_checker.get_debuff(explosion_ref)

        if(has_explosion != None):
            # reset the duration
            has_explosion.duration = has_explosion.initial_duration
        
        else:
            self.target.malus.append(explosion_ref)
        
        # display
        display = f"__Move__ : {self.icon}`{self.name}`\n"
        display += await damager.inflict_damage(self.caster, self.target, damage)

        return(display)