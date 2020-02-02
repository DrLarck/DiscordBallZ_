"""
Mission command

--

Author : DrLarck

Last update : 02/02/20 (DrLarck)
"""

# dependancies
import asyncio
from discord.ext import commands

# checker
from utility.command.checker.basic import Basic_checker

# graphic
from utility.graphic.embed import Custom_embed
from configuration.icon import game_icon

# util
from utility.cog.player.player import Player
from utility.cog.mission.mission_manager import Mission_manager

# mission command
class Cmd_mission(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.check(Basic_checker().is_game_ready)
    @commands.check(Basic_checker().is_registered)
    @commands.group(invoke_without_command = True)
    async def mission(self, ctx, choice : int = None):
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

    @commands.check(Basic_checker().is_game_ready)
    @commands.check(Basic_checker().is_registered)
    @mission.command()
    async def info(self, ctx, choice : int = None):
        """
        Send infos about the mission
        """

        # init
        mission = Mission_manager()
        embed = await Custom_embed(
            self.client, title = f"Mission `#{choice}` info"
        ).setup_embed()

        opponent = ""
        reward = ""
        difficulty = ""

        if(choice != None):
            if(choice > 0 and choice - 1 < len(mission.missions)):
                _mission = mission.missions[choice - 1]

                # init the mission
                await _mission.init()

                # get the opponent
                for char in _mission.opponent:
                    await asyncio.sleep(0) 

                    await char.init()

                    opponent += f"{char.image.icon}**{char.info.name}** - lv.{_mission.level_range['min']:,} - {_mission.level_range['max']:,}{char.rarity.icon}\n"

                # set the reward
                reward = f"{game_icon['dragonstone']} : **{_mission.reward['dragonstone']:,}**\n{game_icon['zenis']} : **{_mission.reward['zenis']:,}**\nPlayer xp : **{_mission.reward['player_xp']:,}**\nTeam xp : **{_mission.reward['team_xp']:,}**"
                
                # get the difficulty
                for a in range(_mission.star):
                    await asyncio.sleep(0)

                    difficulty += ":star:"
                
                # setup the embed
                embed.add_field(
                    name = "Name",
                    value = f"{_mission.name}",
                    inline = False
                )

                embed.add_field(
                    name = "Difficulty",
                    value = difficulty,
                    inline = False
                )

                embed.add_field(
                    name = "Opponents",
                    value = opponent,
                    inline = False
                )

                embed.add_field(
                    name = "Rewards",
                    value = reward,
                    inline = False
                )

                await ctx.send(embed = embed)

            else:
                await ctx.send("Mission not found.")

        else:
            await ctx.send("You didn't choose any mission. Please follow this example : `d!mission info 1`")

def setup(client):
    client.add_cog(Cmd_mission(client))