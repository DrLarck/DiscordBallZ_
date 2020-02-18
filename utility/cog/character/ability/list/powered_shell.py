"""
Powered shell ability object

--

Author : DrLarck

Last update : 18/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.ability.util.effect_checker import Effect_checker
from utility.cog.character.ability.ability import Ability
from utility.cog.displayer.move import Move_displayer

# buff
from utility.cog.character.ability.effect.buff.powered_shell import Buff_powered_shell

class Powered_shell(Ability):
    """
    Represents the Powered Shelle ability
    """

    def __init__(self, client, ctx, caster, target, team_a, team_b):
        Ability.__init__(self, client, ctx, caster, target, team_a, team_b)

        self.name = "Powered shell"
        self.description = f"The carrier gains **10 %** damage reduction for **5** turns."
        self.icon = self.game_icon["ability"]["powered_shell"]

        self.cost = 25

        self.need_target = False
    
    async def use(self):
        """
        `coroutine`

        Applies Power shell buff to the caster

        --

        Return : `str`
        """

        # init
        move = Move_displayer()
        checker = Effect_checker(self.caster)
        powered_shell = Buff_powered_shell(self.client, self.ctx, self.caster, self.team_a, self.team_b)

        # check if the caster already has the buff
        # if the caster has the buff : reset duration
        # else add the buff
        has_buff = await checker.get_buff(powered_shell)

        if(has_buff != None):  # has the buff
            # reset duration
            has_buff.duration = has_buff.initial_duration
        
        else:  # doesn't have the buff
            powered_shell.duration = powered_shell.initial_duration
            self.caster.bonus.append(powered_shell)
        
        # setup move
        _move = await move.get_new_move()

        _move["name"] = self.name
        _move["icon"] = self.icon

        _move = await move.effect_move(_move)

        return(_move)
