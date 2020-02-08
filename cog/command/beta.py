"""
BETA test commands
"""

# dependancies
import asyncio
from discord.ext import commands

class Cmd_beta(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    

def setup(client):
    client.add_cog(Cmd_beta(client))