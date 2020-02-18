"""
Powered shell ability object

--

Author : DrLarck

Last update : 18/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.ability.ability import Ability
from utility.cog.displayer.move import Move_displayer

class Powered_shell(Ability):
    """
    Represents the Powered Shelle ability
    """

    def __init__(self, client, ctx, caster, target, team_a, team_b):
        Ability.__init__(self, client, ctx, caster, target, team_a, team_b)

        self.name = "Powered shell"
        self.description = f"The carrier gains **10 %** damage reduction for **5** turns."
        self.icon = self.game_icon["ability"]["power_shell"]

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
        