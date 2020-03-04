"""
Rocket launcher ability

--

Author : DrLarck

Last update : 04/03/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.ability.ability import Ability
from utility.cog.combat_system.damage.calculator import Damage_calculator

class Rocket_launcher_23(Ability):
    """
    Represents the rocket launcher ability
    """

    def __init__(self, client, ctx, caster, target, team_a, team_b):
        Ability.__init__(self, client, ctx, caster, target, team_a, team_b)

        self.name = "Rocket launcher"
        self.icon = self.game_icon["ability"]["emergency_destruction"]
        self.id = 24

        self.damage.physical = 50
    
    async def set_tooltip(self):
        self.tooltip = f"Inflicts **{int(self.caster.damage.physical_min * 0.5):,}** - **{int(self.caster.damage.physical_max * 0.5):,}**:punch: to **all enemies**."
    
    async def use(self):
        """
        Inflicts 80 % physical to all enemies
        """

        # init
        damager = Damage_calculator()
        display = f"__Move__ : {self.icon}`{self.name}`\n"
        damage = await self.get_damage()

        for enemy in self.team_b:
            await asyncio.sleep(0)

            damage_ = await damager.inflict_damage(self.caster, enemy, damage)

            display += f"{damage_} - {enemy.image.icon}**{enemy.info.name}**{enemy.type.icon}\n"
        
        return (display)