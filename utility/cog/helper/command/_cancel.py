"""
Cancel help panel

--

Author : DrLarck

Last update : 02/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.helper.command.command_help import Help_command

class Help_cancel(Help_command):
    """
    Canccel help panel
    """

    def __init__(self):
        Help_command.__init__(self)
        self.name = "Cancel"
        self.description = "Allow you to unstuck yourself during a blocking action"
        self.invoke = "cancel"

        self.fields = [
            {
                "name" : "d!cancel fight",
                "value" : "Reset your fighting status, usefull if you get the `'You are already in a fight'` error message."
            }
        ]