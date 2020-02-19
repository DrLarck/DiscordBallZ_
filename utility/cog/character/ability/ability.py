"""
Ability super class.

--

Author : DrLarck

Last update : 19/02/20 (DrLarck)
"""

# dependance
import asyncio

# graphic
from configuration.icon import game_icon

# super class
class Ability:
    """
    Represents an ability.

    - Parameter :

    `client` : Represents the used `discord.Client`

    `ctx` : Represents the invocation `commands.Context`

    `caster` : Represents the ability caster.

    `target` : Represents the ability target as a `Character()` instance.

    `team_a` | `team_b` : Represents a list of `Character()`.
    Team A represents the ally team of the caster, team B the opponent one.

    - Attribute :

    `name` : Represents the ability name.

    `description` : Represents the ability description.

    `icon` : Represents the ability's icon as `discord.Emoji`.

    `cost` : Represents the ability ki cost.

    `cooldown` : Represents the ability cooldown.

    `need_target` : True if the target needs a target to be used.

    `target_ally` : True if the ability can target allies.

    `target_enemy` : True if the ability can target an oponnent.

    - Method :

    :coro:`init()` : Translates the ability name and description.

    :coro:`use()` : Triggers the ability.
    """

    # attribute
    def __init__(self, client, ctx, caster, target, team_a, team_b):
        # client
        self.client = client
        self.ctx = ctx
        self.caster = caster
        self.target = target
        self.team_a = team_a
        self.team_b = team_b

        # attribute
        self.name = None
        self.description = None
        self.tooltip = None
        self.icon = "<:notfound:617735236473585694>"
        self.game_icon = game_icon

        # condition
        self.cost = 0
        self.cooldown = 0

        # targetting
        self.need_target = False
        self.target_ally = False
        self.target_enemy = False
        self.ignore_defenders = False

        # damage
        self.damage = Damage()
    
    # method
    async def set_tooltip(self):
        """
        `coroutine` 

        Allows you to set the tooltip of the ability.

        --

        Return : None
        """

        return

    async def init(self):
        """
        `coroutine`

        Translates the ability name and description.

        --

        Return : None
        """

        # set the tooltip
        await self.set_tooltip()

        return
    
    async def use(self):
        """
        `coroutine`

        Triggers the ability.

        --

        Return : str (formatted string of the ability effect)
        """

        return

class Damage():
    """
    Ability's damage attribute

    - Attribute 

    `physical` (`int`)

    `ki` (`int`)

    `true_phy` (`int`) : True damage based on the phy stat of the caster

    `true_ki` (`int`) : Same as true_phy but based on ki

    `rarity` (`int`) : Bonus damage (flat) based on the caster's rarity

    `ability_level` (`int`) : Bonus damage (flat) based on the ability level

    `force` (`int`) : Defense reduction (flat) bonus
    """

    def __init__(self):
        self.physical = 0
        self.ki = 0

        self.true_phy = 0
        self.true_ki = 0

        self.rarity = 0
        self.ability_level = 0
        self.force = 0