"""
General stun

--

Author : DrLarck

Last update : 18/02/19 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.ability._effect import Effect

class Stun(Effect):
    """
    Represents a stun effect

    The duration and the initial duration have to be set
    """

    def __init__(self, client, ctx, carrier, team_a, team_b):
        Effect.__init__(self, client, ctx, carrier, team_a, team_b)

        self.name = "Stun"
        self.icon = "<:stun:679296251329511424>"

        self.id = 11

        # duration
        self.initial_duration = 0
        self.duration = 0

    async def apply(self):
        """
        `coroutine`

        Change the carrier's posture

        --

        Return : `None`
        """
        
        await self.carrier.posture.change_posture("stunned")

        return
    
    async def on_remove(self):
        """
        `coroutine`

        Change the posture to attacking

        --
        
        Return : `None`
        """
        
        await self.carrier.posture.change_posture("attacking")

        return