"""
BETA test commands
"""

# dependancies
import asyncio
from discord.ext import commands

# util
from utility.cog.player.player import Player

# characters
from utility.cog.character.list import c001_sabimen
from utility.cog.character.list import c002_sabimen
from utility.cog.character.list import c003_sabimen

class Cmd_beta(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.group()
    async def beta(self, ctx):
        return
    
    @beta.command()
    async def new_combat(self, ctx):
        """
        new combat system
        """
        # import
        from utility.cog.combat_system.combat import Combat

        # init
        player = Player(ctx, self.client, ctx.message.author)

        teams = [
            {
                "owner" : player,
                "team" : await player.team.character()
            },
            {
                "owner" : player,
                "team" : await player.team.character()
            }
        ]

        combat = Combat(self.client, ctx, teams)

        await combat.display_teams()

def setup(client):
    client.add_cog(Cmd_beta(client))