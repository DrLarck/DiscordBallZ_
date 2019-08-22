"""
Summon command

--

Author : DrLarck

Last update : 22/08/19 (DrLarck)
"""

# dependancies
import asyncio
from discord.ext import commands

# utils
from utility.graphic.embed import Custom_embed
    # checker
from utility.command.checker.basic import Basic_checker
    # summon
from utility.command._summon import Summoner
    # displayer
from utility.cog.displayer.character import Character_displayer

class Cmd_summon(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.check(Basic_checker().is_game_ready)
    @commands.group(aliases = ["sum"])
    async def summon(self, ctx):
        """
        Command group :

        - basic {multi} default {single}
        """

        # init
        embed = Custom_embed(self.client)
        embed = await embed.setup_embed()

        # display the summon help


        return
    
    @commands.check(Basic_checker().is_game_ready)
    @summon.command()
    async def basic(self, ctx):
        """
        Summon a character from the basic banner.
        """

        # init
        player = ctx.message.author 
        summoner = Summoner(self.client)
        displayer = Character_displayer(self.client, ctx, player)

        # draw 
        drawn_character = await summoner.summon(player)
        await drawn_character.init()

        # display
        displayer.character = drawn_character
        await displayer.display(summon_format = True)

def setup(client):
    client.add_cog(Cmd_summon(client))