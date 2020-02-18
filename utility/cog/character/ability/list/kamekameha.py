"""
Manages the kamekameha ability

--

Author : Zyorhist

Last update : 18/02/20 (DrLarck)
"""

# dependancies
import asyncio
from random import randint

# util
from utility.cog.character.ability.ability import Ability

from utility.cog.fight_system.calculator.damage import Damage_calculator

from utility.cog.displayer.move import Move_displayer

# ability
class Kamekameha(Ability):
    """
    Deals a ki attack to the opponent
    
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

        # stat
        self.name = "Kamekameha"
        self.description = f"""Inflicts **200 %** of your  {self.game_icon['ki_ability']} damage as ki damage"""
        
        # self.icon = self.game_icon['ability']['kamekameha']

        self.cost = 50

        # targetting
        self.need_target = True
        self.target_enemy = True
    
    # method
    async def set_tooltip(self):
        self.tooltip = f"Inflicts **{int(self.caster.damage.ki_min * 2):,}** - **{int(self.caster.damage.ki_max * 2):,}** ki damage."

        return
        
    async def use(self):
        """
        `coroutine`

        Inflicts 200% of users ki as ki damage 

        --

        Return : str
        """

        # init
        move = Move_displayer()
        damage_calculator = Damage_calculator(self.caster, self.target)

        roll_damage = int((randint(self.caster.damage.ki_min, self.caster.damage.ki_max)) * 2)
        damage_done = await damage_calculator.physical_damage(
            roll_damage,
            dodgable = True,
            critable = False,
            ignore_defense = False
        )
        
        # inflict the damage to the target
        await self.target.receive_damage(damage_done["calculated"], self.caster)

        # set the move
        _move = await move.get_new_move()

        _move["name"] = self.name
        _move["icon"] = self.icon
        _move["damage"] = damage_done["calculated"]
        _move["dodge"] = damage_done["dodge"]
        _move["critical"] = damage_done["critical"]
        _move["physical"] = False
        _move["ki"] = True

        _move = await move.offensive_move(_move)

        return(_move)
