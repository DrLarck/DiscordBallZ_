"""
Learning machine ability

--

Author : DrLarck

Last update : 03/03/20 (DrLarck)
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
        self.description = "This ability changes based on the **[Derusting]** stacks this unit has."
        self.id = 22
    
    async def use(self):
        """
        • 8 stacks : Mechanical sequence : Inflicts 180 % :punch: to the target (3 :hourglass: )
        • 13 stacks : Rocket launcher : Inflicts 200 % :punch: to all opponents (4 :hourglass: )
        • 20 stacks : Machine gun : Inflicts 250 % :punch: to all opponents (5 :hourglass: )
        • 30 stacks : Emergency destruction : Inflicts 400 % :punch: to all opponents (only once per combat). Reduces your current and maximum :hearts: to 1 for the rest of the fight, consums all your [Derusting] stacks.
        """

        # init
        damager = Damage_calculator()
        checker = Effect_checker(self.caster)
        reference = Buff_derusting(self.client, self.ctx, self.caster, self.team_a, self.team_b)
        multi = False

        # check derusting
        derusting = await checker.get_buff(reference)

        if not derusting is None:
            if(derusting.stack >= 8):
                self.name = "Mechanical sequence"
                self.tooltip = f"Inflicts **{int(self.caster.damage.physical_min * 1.8):,}** - **{int(self.caster.damage.physical_max * 1.8):,}**:punch: to the target."
                self.damage.physical = 180
            
            elif(derusting.stack >= 13):
                self.name = "Rocket launcher"
                self.tooltip = f"Inflicts **{int(self.caster.damage.physical_min * 2):,}** - **{int(self.caster.damage.physical_max * 2):,}**:punch: to **all opponents**."
                self.damage.physical = 200
                multi = True
            
            elif(derusting.stack >= 20):
                self.name = "Machine gun"
                self.tooltip = f"Inflicts **{int(self.caster.damage.physical_min * 2.5):,}** - **{int(self.caster.damage.physical_max * 2.5):,}**:punch: to **all opponents**."
                self.damage.physical = 250
                multi = True

            elif(derusting.stack >= 30):
                self.name = "Emergency destruction"
                self.tooltip = f"Inflicts **{int(self.caster.damage.physical_min * 4):,}** - **{int(self.caster.damage.physical_max * 4):,}**:punch: to **all opponents**."
                self.damage.physical = 400
                multi = True
        
        else:
            self.name = "Mechanical sequence"
            self.tooltip = f"Inflicts **{int(self.caster.damage.physical_min * 2):,}** - **{int(self.caster.damage.physical_max * 2):,}**:punch: to the target."
            self.damage.physical = 200
            multi = False
        
        # inflict the damage
        damage = await self.get_damage()
        display = f"__Move__ : `{self.name}`{self.icon}\n__Damage__ : \n"

        if(multi):  # if AOE
            for enemy in self.team_b:
                await asyncio.sleep(0)

                damage_ = await damager.inflict_damage(self.caster, enemy, damage)

                display += f"{enemy.image.icon}**{enemy.info.name}**{enemy.type.icon} -**{damage_:,}**:punch:\n"
        
        else:
            damage_ = await damager.inflict_damage(self.caster, self.target, damage)

            display += damage_
        
        return(display)
