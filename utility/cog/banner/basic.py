"""
Manages the basic banner.

--

Author : DrLarck

Last update : 18/02/20 (DrLarck)
"""

# dependancies
import asyncio

# utils
from utility.cog.banner._banner import Banner
from utility.command._summon import Summoner

# basic banner
class Basic_banner(Banner):
    """
    Represents a basic banner.
    """

    # class attr
    summonable = None

    # attribute
    def __init__(self):
        # inheritance
        Banner.__init__(self)
        # attr
        self.all = [
            1, 2, 3, 4, 5,
            6, 7, 8, 9, 10,
            11, 12, 13, 14,
            15, 16, 17, 18,
            19, 20, 21, 22,
            23, 24, 25, 26,
            27, 28, 29, 30,
            31, 32, 33, 34,
            35, 36, 37, 38,
            39, 40, 41, 42,
            43, 44, 45
        ]