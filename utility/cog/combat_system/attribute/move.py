"""
Player move object

--

Author : DrLarck

Last update : 08/02/20 (DrLarck)
"""

class Move():
    """
    Stores the player's move

    - Attribute 

    `index` (`int`) : The player's move index

    `target` (`Character()`) : `None` - The player move's target
    """
    
    def __init__(self):
        self.index = 0
        self.target = None