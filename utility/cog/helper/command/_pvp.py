"""
Pvp command help

--

Author : DrLarck

Last update : 15/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.helper.command.command_help import Help_command

class Help_pvp(Help_command):
    """
    Show the pvp help panel
    """

    def __init__(self):
        Help_command.__init__(self)
        self.name = "Pvp"
        self.description = "Start a fight against another player"
        self.invoke = "pvp"

        self.fields = [
            {
                "name" : "d!pvp [user]",
                "value" : "Start a fight against the `user`."
            }
        ]