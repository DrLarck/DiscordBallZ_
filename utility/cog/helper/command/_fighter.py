"""
Fighter help pannel

--

Author : DrLarck

Last update : 02/02/2020 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.helper.command.command_help import Help_command

class Help_fighter(Help_command):
    """
    Fighter help pannel
    """

    def __init__(self):
        Help_command.__init__(self)
        self.name = "Fighter"
        self.description = "Allow you to manage your team of fighters"
        self.invoke = "fighter"
        
        self.fields = [
            {
                "name" : "d!fighter team",
                "value" : "Display your team"
            },
            {
                "name" : "d!fighter set [a/b/c] [unique id]",
                "value" : "Set the fighter with the `unique id` at the slot `a`, `b` or `c`"
            },
            {
                "name" : "d!fighter remove [a/b/c]",
                "value" : "Remove the fighter at the specified slot"
            }
        ]