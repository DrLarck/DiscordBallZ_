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

    async def inflict_damage(self, attacker, target, damage):
        """
        `coroutine`

        Inflict the damage to the target

        - Parameter 

        `attacker` (`Character()`)

        `target` (`Character()`)

        `damage` (`Damage()`)

        --

        Return : `str`
        """

        # init
        display = ""

        # check physical damage from damage object
        # if there is physical damage
        # calculate the physical damage

        # check ki damage
        # if there is ki damage
        # calculate ki damage

        # check true damage
        # if there is true damage
        # add it to the final damage

        # edit the damage object
        
        # get the display

        # inflict damage

        # return the display
        return(display)

    # util
    async def get_type_advantage(self, attacker, target):
        """
        `coroutine`

        Get the type advantage multiplier

        - Parameter

        `attacker` (`Character()`)

        `target` (`Target()`)

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
    
    async def get_critical(self, critical_chance):
        """
        `coroutine`

        Tells if it's a critical strike or not

        - Parameter

        `critical_chance` (`float`)

        --

        Return : `bool`
        """

        # init
        roll = random.uniform(0, 100)
        critical = False

        if(roll <= critical_chance):
            critical = True

        return(critical)
    
    async def get_bonus(self, attacker):
        """
        `coroutine`

        Get the bonus total value

        --

        Return : `int`
        """ 

        # init
        bonus = 0

        # get the bonus
        for _bonus in attacker.damage.bonus:
            await asyncio.sleep(0)

            bonus += _bonus.value

        return(bonus)
    
    async def get_defense(self, target, damage, physical = False, ki = False):
        """
        `coroutine`

        Make the defense calculation

        - Parameter 

        `target` (`Character()`)

        `damage` (`Damage()`)

        `physical` (`bool`)

        `ki` (`bool`)

        --

        Return : `float`
        """

        # init
        defense = 1

        if(physical):
            defense = ((2500 + damage.force) / (2500 + target.defense.armor))        
        
        elif(ki):
            defense = ((2500 + damage.force) / (2500 + target.defense.spirit))        

        return(defense)
    
    async def get_physical_damage(self, attacker, target, damage):
        """
        `coroutine`

        Calculate the physical damage

        - Parameter

        `attacker` (`Character()`)

        `target` (`Character()`)

        `damage` (`Damage()`)

        --

        Return : `Damage()`
        """

        # init
        type_advantage = await self.get_type_advantage(attacker, target)
        critical = await self.get_critical(attacker.critical_chance)
        multiplier_crit = 1

        # increase the critical multiplier
        # in case of crit
        if(critical):
            multiplier_crit = 1.5 + (attacker.critical_bonus / 100)

        # get bonus value
        bonus = await self.get_bonus(attacker)

        # get defense value
        defense = await self.get_defense(target, damage, physical = True)

        # get damage reduction
        physical_reduction = 1 - (target.defense.damage_reduction_physical / 100)
        neutral_reduction = 1 - (target.defense.damage_reduction_neutral / 100)

        # get physical damage
        physical = (
            (((damage.physical + bonus) * (attacker.damage.amplifier_neutral + attacker.amplifier_physical) *
            (defense ) * (1 - (physical_reduction * neutral_reduction))) * type_advantage) * multiplier_crit
        )

        # edit damage object
        damage.physical = physical

        return(damage)