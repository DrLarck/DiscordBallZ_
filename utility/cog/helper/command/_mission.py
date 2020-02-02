"""
Mission help panel

--

Author : DrLarck

Last update : 02/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.helper.command.command_help import Help_command

class Help_mission(Help_command):
    """
    Mission help panel
    """

    def __init__(self):
        Help_command.__init__(self)
        self.name = "Mission"
        self.description = "Allow you to start missions and get rewards"
        self.invoke = "mission"

        self.fields = [
            {
                "name" : "d!mission",
                "value" : "Display the available missions"
            },
            {
                "name" : "d!mission [index]",
                "value" : "Start a mission"
            },
            {
                "name" : "d!mission info [index]",
                "value" : "Display the mission's informations such as rewards, opponents, etc."
            }
        ]