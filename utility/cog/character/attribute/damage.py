"""
Manages the character's damage attribute.

-- 

Author : DrLarck

Last update : 19/02/20 (DrLarck)
"""

# damage attribute
class Character_damage:
    """
    Manages the character's damage attribute.

    - Attribute :

    `physical_max` | `physical_min` : Represents the max physical damage and min.

    `ki_max` | `ki_min` : Same as physical, but for ki abilities.

    `amplfier_physical/ki/neutral` (`float`)

    `bonus` (`list` of `Bonus()`)
    """

    # attribute
    def __init__(self):
        # physical damage values
        self.physical_max = 0
        self.physical_min = 0
        self.amplifier_physical = 0

        # ki damage values
        self.ki_max = 0
        self.ki_min = 0
        self.amplifier_ki = 0

        # neutral
        self.amplifier_neutral = 0

        self.bonus = []