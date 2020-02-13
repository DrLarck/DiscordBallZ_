"""
Manages the Arm Stretch ability

--

Author : Zyorhist

Last update : 30/01/20 (DrLarck)
"""

# dependance
import asyncio
from random import randint
from random import uniform

# utility
from utility.cog.character.ability.ability import Ability
from utility.cog.displayer.move import Move_displayer
from utility.cog.fight_system.calculator.damage1 import Damage_calculator

# ability
class Arm_stretch(Ability):
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
            team_b,

        )

        #basics
        self.phy_dam = self.caster.damage.physical_max,
        self.ki_dam = 0
        self.true_dam = 0
        self.momentum = 0
        self.critable = True
        self.type = 1
        self.cost = 5


        #targeting changes possible
        self.target_enemy = True
        self.need_target = True

        self.name = "Arm Stretch"
        self.description = f"""Performs a sequence attack against any enemy"""
    
    # method
    async def set_tooltip(self):
        self.tooltip = f"Performs a sequence attack against any enemy, deals {int(self.phy_dam)} physical damage"

        return

    async def use(self):

        move = Move_displayer()
        _move = await move.get_new_move()

        damage_calculator = Damage_calculator(self.caster, self.target)

        _move["name"] = self.name
        # _move["icon"] = self.icon
        

        roll_dodge = uniform(0, 100)

        if(roll_dodge <= self.target.defense.dodge):
            # dodged, this ability does nothing
            _move["dodge"] = True
            return (_move)

        else:
            total_dam = await damage_calculator.total_dam(
                ki_dam = self.ki_dam,
                phy_dam = self.phy_dam,
                true_dam = self.true_dam,
                momentum = self.momentum,
                critable = self.critable,
            )

        return(_move)