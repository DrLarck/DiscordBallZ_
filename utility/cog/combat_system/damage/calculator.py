"""
Damage calculator object

--

Author : DrLarck

Last update : 19/02/20 (DrLarck)
"""

# dependancies
import asyncio
import random

class Damage_calculator():
    """
    Allow the damage calculation

    - Attribute

    """

    # util
    async def get_type_advantage(self, attacker, target):
        """
        `coroutine`

        Get the type advantage multiplier

        --

        Return : `float`
        """

        # init
        multiplier = 1
        attacker = attacker.type.value
        target = target.type.value

        # advantage
            # phy > int
        if(attacker == 3 and target == 4):
            multiplier = 1.2

            # int > teq
        elif(attacker == 4 and target == 1):
            multiplier = 1.2

            # agl > str
        elif(attacker == 0 and target == 2):
            multiplier = 1.2

            # str > phy
        elif(attacker == 2 and target == 3):
            multiplier = 1.2

            # teq > agl
        elif(attacker == 1 and target == 0):
            multiplier = 1.2
        
        # disadvantage
            # just reverse
        elif(attacker == 4 and target == 3):
            multiplier = 0.8

        elif(attacker == 1 and target == 4):
            multiplier = 0.8
        
        elif(attacker == 2 and target == 0):
            multiplier = 0.8
        
        elif(attacker == 3 and target == 2):
            multiplier = 0.8
        
        elif(attacker == 0 and target == 1):
            multiplier = 0.8
        
        # if not found
        else:
            pass

        return(multiplier)