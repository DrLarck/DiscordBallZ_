"""
Ki blast

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

# Ki blast
class Ki_blast(Ability):
    """
    Represents the Ki blast ability
    """

    def __init__(self, client, ctx, caster, target, team_a, team_b):
        Ability.__init__(self, client, ctx, caster, target, team_a, team_b)
        
        self.name = "Ki blast"
        self.description = f"Inflicts **120 %** of your {self.game_icon['ki_ability']} damage."
        self.icon = self.game_icon["ability"]["ki_blast"]

        self.cost = 20

        self.need_target = True
        self.target_enemy = True

    async def set_tooltip(self):
        self.tooltip = f"Inflicts **{int(self.caster.damage.ki_min * 2.2):,}** - **{int(self.caster.damage.ki_max * 2.2):,}** {self.game_icon['ki_ability']}"

    async def use(self):
        """
        `coroutine`

        Inflicts 120 % of the caster's ki as damage to the target.

        --
        
        Return : `str`
        """

        # init
        move = Move_displayer()
        damager = Damage_calculator(self.caster, self.target)

        # set damage
        damage = int(random.randint(self.caster.damage.ki_min, self.caster.damage.ki_max) * 2.2)
        damage = await damager.ki_damage(damage, dodgable = True)

        _move = await move.get_new_move()

        _move["name"] = self.name
        _move["icon"] = self.icon
        _move["damage"] = damage["calculated"]
        _move["critical"] = damage["critical"]
        _move["dodge"] = damage["dodge"]
        _move["ki"] = True

        _move = await move.offensive_move(_move)

        # inflict damage
        await self.target.receive_damage(damage["calculated"])

        return(_move)