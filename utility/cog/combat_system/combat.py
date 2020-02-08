"""
Combat object

--

Author : DrLarck

Last update : 08/02/20 (DrLarck)
"""

# dependancies
import asyncio
import random

# graphic
from utility.graphic.embed import Custom_embed

class Combat():
    """
    Manages a combat

    - Parameter : 

    `client` (`discord.ext.commands.Bot`)

    `ctx` (`discord.ext.commands.context`)

    `teams` (`list` of `dict`) : {owner(str), team(list)}

    - Attribute :

    `player_a/b` (`Player()`) : Represents the play order, the player a plays before the player b

    - Method :

    :coro:`display_teams()` : `None` - Display both teams as a single embed
    """

    # attribute
    def __init__(self, client, ctx, teams):
        # bot
        self.client = client
        self.ctx = ctx
        self.teams = teams

        # players
        self.player_a, self.player_b = None, None

    # method
    async def get_play_order(self):
        """
        `coroutine`

        Defines the play order (player a and player b)

        --

        Return : `None`
        """

        # init 
        first = random.randint(0, 1)

        self.player_a = self.teams[first]["owner"]

        if(first == 0):
            self.player_b = self.teams[1]["owner"]
        
        else:
            self.player_b = self.teams[0]["owner"]

        return

    async def display_teams(self, sorted_team):
        """
        `coroutine`

        Display both teams as a single embed

        - Parameter :

        `sorted_team` (`list`) : The `sorted_team[0]` has to be the team of the first player to play

        --

        Return : `None`
        """

        # init
        team_a, team_b = sorted_team[0], sorted_team[1]
        team_a_display, team_b_display = "", ""

        embed = await Custom_embed(
            self.client,
            title = "Teams"
        ).setup_embed()

        # displaying
        # team a
        for char_a in team_a:
            await asyncio.sleep(0)

            team_a_display += f"{char_a.image.icon}**{char_a.info.name}** - lv.**{char_a.level:,}**{char_a.type.icon} {char_a.rarity.icon}"

            team_a_display += "\n"
        
        for char_b in team_b:
            await asyncio.sleep(0)
        
            team_b_display += f"{char_b.image.icon}**{char_b.info.name}** - lv.**{char_b.level:,}**{char_b.type.icon} {char_b.rarity.icon}"

            team_b_display += "\n"

        # setting up the embed
        embed.add_field(
            name = f"🔵 **{self.player_a.name}**'s team",
            value = team_a_display,
            inline = False
        )

        embed.add_field(
            name = f"🔴 **{self.player_b.name}**'s team",
            value = team_b_display,
            inline = False
        )

        # sending the embed
        await self.ctx.send(embed = embed)

        return