"""
Mission object

--

Author : DrLarck

Last update : 02/02/20 (DrLarck)
"""

# dependancies
import asyncio

# mission
class Mission():
    """
    Represent a mission

    - Parameter :

    # REWARD

    `dragonstone` (`int`)
    
    `zenis` (`int`)

    `player_xp` (`int`)

    `team_xp` (`int`)

    - Attribute :
    
    # REWARD

    `dragonstone` (`int`)
    
    `zenis` (`int`)

    `player_xp` (`int`)
    
    `team_xp` (`int`) 

    # info

    `opponent` (`list`) : List of `Character()` in the opponent team

    `star` (`int`) : Difficulty

    `level_range` (`dict`) : [min, max] The level range of the opponents 

    - Method 

    :coro:`init()` : `None` - Init the mission

    :coro:`set_opponent()` : `list` - Set the opponent team
    """

    # attribute
    def __init__(self):
        # info
        self.name = ""

        self.opponent = []
        self.star = 1  # difficulty
        self.level_range = {
            "min" : 0,
            "max" : 1
        }

        # reward
        self.dragonstone = 0
        self.zenis = 0
        self.player_xp = 0
        self.team_xp = 0
    
    # method
    async def init(self):
        """
        `coroutine`

        Init the mission

        -- 

        Return : `None`
        """

        await self.set_opponent()

        return
    
    async def set_opponent(self):
        """
        `coroutine`

        Set the opponent team

        --

        Return : `list`
        """

        return(self.opponent)