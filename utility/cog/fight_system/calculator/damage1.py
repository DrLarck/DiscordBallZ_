"""
Manages the damage calculator.

--

Author : DrLarck

Last update : 11/09/19 (DrLarck)
"""

# dependancies
import asyncio
from random import uniform

# damage calculator
class Damage_calculator:

    def __init__(self, attacker, target):
        # param
        self.attacker = attacker
        self.target = target

        # attr
        self.damage = {
            "calculated" : 0,
            "critical" : False
        }
        self.type_bonus = 1
        self.critical_bonus = 1
        self.damage_reduction = 1 + self.target.defense.damage_reduction
        self.armor = 2500/(2500 + self.target.defense.armor)
        self.spirit = 2500/(2500 + self.target.defense.spirit)

    async def total_dam(self, ki_dam, phy_dam, true_dam, momentum, critable):
        #type advantage
        #crit
        #defenses
        #damage reductions
        #add together

        return(self.damage)