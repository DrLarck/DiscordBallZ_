"""
Manages the character's defense attribute.

--

Author : DrLarck

Last update : 19/02/20 (DrLarck)
"""

# defense
class Character_defense:
    """
    Manages the character's defense attribute.

    - Attribute :

    `armor` : Represents the armor value.

    `spirit` : Represents the ki defense.

    `dodge` : Represents the dodge chance as %.

    `parry` : Represents the parry chance as %.

    `damage_reduction_physical/ki/neutral` : Represents the damage reduction as %.

    """

    # attribute
    def __init__(self):
        self.armor = 0
        self.spirit = 0
        self.dodge = 0  # % chance
        self.parry = 0  # % chance
        
        self.damage_reduction_physical = 0  # %
        self.damage_reduction_ki = 0  # %
        self.damage_reduction_neutral = 0  # %