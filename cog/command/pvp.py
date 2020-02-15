"""
Pvp command

--

Author : DrLarck

Last update : 15/02/20 (DrLarck)
"""

# dependancies
import asyncio
import discord
from discord.ext import commands

# checker
from utility.command.checker.basic import Basic_checker
from utility.command.checker.fight import Fight_checker

# util
from utility.cog.player.player import Player
from utility.cog.combat_system.combat import Combat

class Cmd_pvp(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.check(Basic_checker.is_game_ready)
    @commands.check(Basic_checker.is_registered)
    @commands.check(Fight_checker.has_team)
    @commands.check(Fight_checker.is_in_fight)
    async def pvp(self, ctx, opponent: discord.Member):
        """
        Start a pvp fight
        """

        # init
        player = Player(ctx, self.client, ctx.message.author)
        opponent = Player(ctx, self.client, opponent)
        
        # get the teams
        player_team = await player.team.character()
        opponent_team = await opponent.team.character()

        # set the teams
        teams = [
            {"owner": player, "team": player_team}, {"owner": opponent, "team": opponent_team}
        ]

        # get the combat object
        combat = Combat(self.client, ctx, teams)

        # run the fight
        winner = await combat.run()

def setup(client):
    client.add_cog(Cmd_pvp(client))