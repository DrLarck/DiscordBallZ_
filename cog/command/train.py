"""
This command allows the player to level up his characters.

--

Author : DrLarck

Last update : 14/07/19
"""

# dependancies
import asyncio

from discord.ext import commands

# utils
from utility.cog.fight_system.fight import Fight

    # translation
from utility.translation.translator import Translator

# test
from utility.cog.character.list.c1 import Character_1

# command
class Cmd_train(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def train(self, ctx):
        """
        `coroutine`

        Start a fight against an adaptative team.

        The opponent team level is scaled on the player team level, same for the rarity.

        If the player wins the fight, his character gain some xp.
        """

        caller = ctx.message.author 

        # test shit
        chara = Character_1()
        charb = Character_1()
        charc = Character_1()

        caller_team = [chara, charb, charc]

        for char in caller_team:
            await char.init()

        team = [caller_team, caller_team]

        fight = Fight(self.client, ctx, caller)
        await fight.run_fight(team)
        
        return

def setup(client):
    client.add_cog(Cmd_train(client))