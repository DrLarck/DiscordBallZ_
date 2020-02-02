"""
Mission command

--

Author : DrLarck

Last update : 01/02/20 (DrLarck)
"""

# dependancies
import asyncio
from discord.ext import commands

# checker
from utility.command.checker.basic import Basic_checker

# graphic
from utility.graphic.embed import Custom_embed

# util
from utility.cog.player.player import Player
from utility.cog.mission.mission_manager import Mission_manager

# mission command
class Cmd_mission(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.check(Basic_checker().is_game_ready)
    @commands.check(Basic_checker().is_registered)
    @commands.command()
    async def mission(self, ctx, choice = None):
        """
        Allow the player to display the mission panel

        Or to start a mission if the `choice` parameter is != `None`

        - Parameter :

        `choice` (`int`) : Mission index
        """

        # init
        player = Player(ctx, self.client, ctx.message.author)
        mission = Mission_manager()
        embed = await Custom_embed(
            self.client, title = "Missions", description = "Welcome to the Missions panel\nUse `d!mission [index]` to start a mission"
        ).setup_embed()    
        
        # start mission
        if(choice != None):
            if(choice.isdigit()):
                choice = int(choice)
                await mission.start_mission(ctx, self.client, player, choice)

        else:
            # display the missions panel
            panel = ""
            mission_star = ""   
            mission_index = 1

            # manage the mission displaying
            for _mission in mission.missions:
                await asyncio.sleep(0)

                panel += f"`{mission_index}.` {_mission.name}"

                for a in range(_mission.star):
                    await asyncio.sleep(0)

                    mission_star += ":star:"
                
                panel += f" {mission_star}\n"

                mission_index += 1
            
            # set the embed
            embed.add_field(
                name = "Available missions",
                value = panel
            )

            await ctx.send(embed = embed)

def setup(client):
    client.add_cog(Cmd_mission(client))