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

    :coro:`get_play_order()` : `None` - Defines the play order (player a and player b)

    :coro:`get_teams()` : `list`, `list` - Init the characters of both teams

    :coro:`display_teams()` : `None` - Display both teams as a single embed

    # combat
    :coro:`run()` : `Player()` - Run the fight
    """

    # attribute
    def __init__(self, client, ctx, teams):
        # bot
        self.client = client
        self.ctx = ctx
        self.teams = teams

        # players
        self.player_a, self.player_b = None, None
        self.team_a, self.team_b = None, None

    # method
        # init
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

    async def get_teams(self):
        """
        `coroutine`

        Init the characters of both teams

        --

        Return : `list` team a, `list` team b
        """

        # init
        team_a, team_b = [], []

        # get team a 
        team_a = await self.player_a.team.character()

        for char_a in team_a:
            await asyncio.sleep(0)

            await char_a.init()

        self.team_a = team_a

        # get team b 
        team_b = await self.player_b.team.character()

        for char_b in team_b:
            await asyncio.sleep(0)

            await char_b.init()
        
        self.team_b = team_b

        return(team_a, team_b)

    async def display_teams(self):
        """
        `coroutine`

        Display both teams as a single embed

        --

        Return : `None`
        """

        # init
        team_a_display, team_b_display = "", ""

        embed = await Custom_embed(
            self.client,
            title = "Teams"
        ).setup_embed()

        # displaying
        # team a
        for char_a in self.team_a:
            await asyncio.sleep(0)

            team_a_display += f"{char_a.image.icon}**{char_a.info.name}** - lv.**{char_a.level:,}**{char_a.type.icon} {char_a.rarity.icon}"

            team_a_display += "\n"
        
        for char_b in self.team_b:
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
    
    async def get_player_fighter(self, order):
        """
        `coroutine`

        Ask the player which character he wants to use this turn

        - Parameter : 

        `order` (`int`) : 0 for player A, 1 for player B
        
        --

        Return : `Character()`
        """

        # init
        team_display = ""
        index = 1

        team = None

        # if player a
        if(order == 0):
            team = self.team_a
            player = self.player_a
            circle = "🔵"
        
        else:
            team = self.team_b
            player = self.player_b
            circle = "🔴"
        
        # set embed
        embed = await Custom_embed(
            self.client,
            title = "Fighters",
            thumb = player.avatar
        ).setup_embed()
        
        # set player team display
        for char in team:
            await asyncio.sleep(0)

            posture, posture_icon = await char.posture.get_posture()
            team_display += f"`{index}`. {char.image.icon}**{char.info.name}** - **{char.health.current:,}**:hearts: *({int((char.health.current * 100) / char.health.maximum)} %)* {posture_icon}"

            team_display += "\n"
            index += 1
        
        embed.add_field(
            name = f"{circle}**{player.name}**'s team",
            value = team_display,
            inline = False
        )

        await self.ctx.send(embed = embed)
        await self.ctx.send("Please select a fighter : Type its **index** number.")
    
    # combat
    async def run(self):
        """
        `coroutine`

        Run the combat

        --

        Return : `Player()`
        """ 

        # init
        await self.get_play_order()
        self.team_a, self.team_b = await self.get_teams()

        turn = 1

        if(turn == 1):
            await self.display_teams()
        
        # get player fighter
        await self.get_player_fighter(0)

        return