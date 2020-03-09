"""
Learning machine ability

--

Author : DrLarck

Last update : 04/03/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.ability.ability import Ability
from utility.cog.character.ability.util.effect_checker import Effect_checker
from utility.cog.character.ability.effect.buff.derusting import Buff_derusting
from utility.cog.combat_system.damage.calculator import Damage_calculator

class Learning_machine_22(Ability):
    """
    Represents the learning machine ability
    """

    def __init__(self, client, ctx, caster, target, team_a, team_b):
        Ability.__init__(self, client, ctx, caster, target, team_a, team_b)

        self.name = "Learning machine"
        self.description = "This ability evolves based on the **[Derusting]** stacks this unit has."
        self.id = 22

        self.need_target = True
        self.target_enemy = True

        # private
        self.multi = False

    async def set_tooltip(self):
        self.tooltip = "This ability evolves based on the amount of **[Derusting]** stacks you have."
    
    async def init(self):
        """
        Changes the ability based on the caster's derusting stacks
        """

        # set the tooltip
        await self.set_tooltip()
        await self.get_damage()

        # custom
        checker = Effect_checker(self.caster)
        reference = Buff_derusting(self.client, self.ctx, self.caster, self.team_a, self.team_b)

        # check derusting
        derusting = await checker.get_buff(reference)
            
            if(derusting.stack >= 13):
                self.name = "Machine gun"
                self.icon = self.game_icon["ability"]["machine_gun"]
                self.tooltip = f"Inflicts **{int(self.caster.damage.physical_min * 2.5):,}** - **{int(self.caster.damage.physical_max * 2.5):,}**:punch: to **all opponents**."
                self.damage.physical = 250
                self.multi = True

            if(derusting.stack >= 20):
                self.name = "Emergency destruction"
                self.icon = self.game_icon["ability"]["emergency_destruction"]
                self.tooltip = f"Inflicts **{int(self.caster.damage.physical_min * 4):,}** - **{int(self.caster.damage.physical_max * 4):,}**:punch: to **all opponents**."
                self.damage.physical = 400
                self.multi = True

    async def use(self):
        """
        • 8 stacks : Mechanical sequence : Inflicts 180 % :punch: to the target (3 :hourglass: )
        • 13 stacks : Rocket launcher : Inflicts 200 % :punch: to all opponents (4 :hourglass: )
        • 20 stacks : Machine gun : Inflicts 250 % :punch: to all opponents (5 :hourglass: )
        • 30 stacks : Emergency destruction : Inflicts 400 % :punch: to all opponents (only once per combat). Reduces your current and maximum :hearts: to 1 for the rest of the fight, consums all your [Derusting] stacks.
        """

        # init
        damager = Damage_calculator()
    
        # inflict the damage
        damage = await self.get_damage()
        display = f"__Move__ : {self.icon}`{self.name}`\n"

        if(self.multi):  # if AOE
            for enemy in self.team_b:
                await asyncio.sleep(0)

                damage_ = await damager.inflict_damage(self.caster, enemy, damage)
            
                display += f"{damage_} - {enemy.image.icon}**{enemy.info.name}**{enemy.type.icon}\n"
        
        else:
            damage_ = await damager.inflict_damage(self.caster, self.target, damage)

            display += damage_
        
        return(display)
