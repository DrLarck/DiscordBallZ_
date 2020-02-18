"""
This command allows the player to level up his characters.

--

Author : DrLarck

Last update : 15/02/20 (DrLarck)
"""

# dependancies
import asyncio

from discord.ext import commands

# utils
from utility.cog.fight_system.fight import Fight
from utility.cog.combat_system.combat import Combat
from utility.cog.combat_system.cpu import CPU
from utility.cog.player.player import Player
from utility.cog.character.getter import Character_getter
from utility.command._train import Train
from utility.cog.level.level import Leveller
    #checker
from utility.command.checker.basic import Basic_checker
from utility.command.checker.fight import Fight_checker
    # translation
from utility.translation.translator import Translator

# command
class Cmd_train(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.check(Basic_checker().is_game_ready)
    @commands.check(Basic_checker().is_registered)
    @commands.check(Fight_checker().is_in_fight)
    @commands.check(Fight_checker().has_team)
    @commands.command()
    async def train(self, ctx):
        """
        `coroutine`

        Start a fight against an adaptative team.

        The opponent team level is scaled on the player team level, same for the rarity.

        If the player wins the fight, his character gain some xp.
        """

        # init
        caller = ctx.message.author 
        player = Player(ctx, self.client, caller)
        cpu = CPU()
        cpu.name = "Trainer"
        train = Train(self.client)
        leveller = Leveller(self.client, ctx)

        cpu.team.team = await train.generate_opponent_team(player)

        combat_teams = [
            {
                "owner" : player,
                "team" : await player.team.character()
            },
            {
                "owner" : cpu,
                "team" : cpu.team.team
            }
        ]

        combat = Combat(self.client, ctx, combat_teams)

        winner = await combat.run()

        if(winner == player):
            # set the xp
            # init
            xp_won = 100
            player_info = await player.team.get_info()
            player_team_level, player_team_rarity = player_info["level"], player_info["rarity"]

            # set the xp gain
            xp_won += (((1.5 * 100) - 100) * player_team_level) + (100 * (player_team_rarity - 1))

            # add xp
            player_team_id = [player.team.team["a"], player.team.team["b"], player.team.team["c"]]
            await leveller.team_add_xp(player, player_team_id, xp_won)

def setup(client):
    client.add_cog(Cmd_train(client))