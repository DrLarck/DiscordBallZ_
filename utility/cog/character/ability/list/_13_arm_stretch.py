"""
Manages the Arm Stretch ability

--

Author : Zyorhist

Last update : 29/02/20 (DrLarck)
"""

# dependance
import asyncio
from random import randint

# utility
from utility.cog.combat_system.damage.calculator import Damage_calculator

from utility.cog.character.ability.ability import Ability

# ability
class Arm_stretch_13(Ability):
    """
    This ability applies performs a sequence attack against any enemy
    """

    # attribute
    def __init__(self, client, ctx, caster, target, team_a, team_b):
        Ability.__init__(
            self,
            client,
            ctx,
            caster,
            target,
            team_a,
            team_b
        )

        self.name = "Arm Stretch"
        #self.icon = self.game_icon['ability']['arm_stretch']
        self.description = f"""Performs a sequence attack against any enemy"""
        self.id = 13

        self.cost = 5
        self.target_enemy = True
        self.need_target = True
        self.ignore_defenders = True

        self.damage.physical = 100
    
    # method
    async def set_tooltip(self):
        self.tooltip = f"Performs a sequence attack against any enemy"

        return

    async def use(self):
        """
        `coroutine`

        Performs a sequence attack against any enemy

        --

        Return : str
        """

        # init
        await self.caster.posture.change_posture("attacking")

        calculator = Damage_calculator()

        # get the damage
        damage = await self.get_damage()

        # define move info
        display = await calculator.inflict_damage(self.caster, self.target, damage)

        return(display)