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
            "ki damage" : 0,
            "phy damage" : 0,
            "true damage" : 0,
            "total damage" : 0,
            "critical" : False

        }
        self.type_bonus = 1
        self.critical_bonus = 1
        self.damage_reduction = 1
        self.armor = 0
        self.spirit = 0

    # type advantage calculator
    async def get_type_advantage(self):
        """
        `coroutine`

        Check if the attacker has a type advantage onto the target.

        --

        Return : directly modify the `type_bonus` value and return the multiplier bonus.
        
        """

        # init
        multiplier = 1
        target, attacker = self.target.type.value, self.attacker.type.value

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

        # modify the type advantage
        self.type_bonus = multiplier

        return(multiplier)

    async def total_dam(self, ki_dam, phy_dam, true_dam, momentum, critable):
        #get bonus damage
            #get bonus damage from abilities (added not multiplied damage)

        #type advantage
        await self.get_type_advantage()
        ki_dam = ki_dam * self.type_bonus
        phy_dam = phy_dam * self.type_bonus

        #crit
        if(critable):
            roll_crit = uniform(0, 100)
            if(roll_crit <= self.attacker.critical_chance):
                # crit
                self.damage["critical"] = True
                self.critical_bonus = 1.5 + (self.attacker.critical_bonus)/100
                ki_dam = ki_dam * self.critical_bonus
                phy_dam = phy_dam * self.critical_bonus

        #amplifiers
            #get multipliers from buffs

        #reducers
            #get damage multipliers from debuffs

        #defenses
        self.armor = (2500 + momentum)/(2500 + self.target.defense.armor)
        self.spirit = (2500 + momentum)/(2500 + self.target.defense.spirit)
        ki_dam = ki_dam * self.spirit
        phy_dam = phy_dam * self.armor

        #damage reductions
            # (= 1 * (1-bonus) * (1-bonus).....)

        #add together
        self.damage["ki damage"] = ki_dam
        self.damage["phy damage"] = phy_dam
        self.damage["true damage"] = true_dam
        self.damage["total damage"] = ki_dam + phy_dam + true_dam

        return(self.damage)