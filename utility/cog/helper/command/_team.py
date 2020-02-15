"""
Fighter help pannel

--

Author : DrLarck

Last update : 15/02/2020 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.helper.command.command_help import Help_command

class Help_team(Help_command):
    """
    Fighter help pannel
    """

    def __init__(self):
        Help_command.__init__(self)
        self.name = "Team"
        self.description = "Allow you to manage your team of fighters"
        self.invoke = "team"
        
        self.fields = [
            {
                "name" : "d!team",
                "value" : "Display your team"
            },
            {
                "name" : "d!team set [a/b/c] [unique id]",
                "value" : "Set the fighter with the `unique id` at the slot `a`, `b` or `c`"
            },
            {
                "name" : "d!team remove [a/b/c]",
                "value" : "Remove the fighter at the specified slot"
            }
        ]