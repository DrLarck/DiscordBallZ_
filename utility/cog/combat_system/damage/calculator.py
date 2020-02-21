"""
Damage calculator object

--

Author : DrLarck

Last update : 21/02/20 (DrLarck)
"""

# dependancies
import asyncio
import random

# graphic
from configuration.icon import game_icon

class Damage_calculator():
    """
    Allow the damage calculation

    - Method

    `inflict_damage(attacker, target, damage)` (`Character()`, `Character()`, `Damage()`) : `str` - Inflict the damages from the `Damage()` object and trigger `on_death()` effects

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
        detail = ""
        detail_cpt = 0
        total = 0
        dodge = random.uniform(0, 100)

        if(dodge >= target.defense.dodge):  # if the target doesn't dodge the attack
            # check physical damage from damage object
            # if there is physical damage
            # calculate the physical damage
            if(damage.physical > 0):
                damage = await self.get_physical_damage(attacker, target, damage)
                detail += f":punch:-{damage.physical:,}"
                total += damage.physical

                detail_cpt += 1

            # check ki damage
            # if there is ki damage
            # calculate ki damage
            if(damage.ki > 0):
                damage = await self.get_ki_damage(attacker, target, damage)
                
                if(detail_cpt > 0):
                    detail += ", "

                detail += f"{game_icon['ki_ability']}-{damage.ki:,}"
                total += damage.ki

            # check true damage
            # if there is true damage
            # add it to the final damage
            if(damage.true > 0):
                true = damage.true

                if(detail_cpt > 0):
                    detail += ", "

                detail += f":anger:{true:,}"
                total += true
            
            # get the display
            display = f"__Damage__ : **-{total:,}**"

            # display the detailed damage
            if(detail != ""):
                display += f" *({detail})*"

            # inflict damage
            gonna_die = False  # check if the damages are going to kill the target
            
            if(total >= target.health.current):  # the target is going to die from the damages
                gonna_die = true
            
            # inflict
            target.health.current -= total
            await target.health.health_limit()

            # trigger on_death() effects
            if(gonna_die):
                for death in target.on_death:
                    await asyncio.sleep(0)

                    death.apply()
        
        else:  # the target has dodged
            display += ":dash: **DODGED**"

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
        damage_reduction = 1
        amplifier = 1

        # increase the critical multiplier
        # in case of crit
        if(critical):
            multiplier_crit = 1.5 + (attacker.critical_bonus / 100)

        # get bonus value
        bonus = await self.get_bonus(attacker)

        # get the amplifier
        amplifier += (attacker.damage.amplifier_neutral + attacker.damage.amplifier_physical)

        # get defense value
        defense = await self.get_defense(target, damage, physical = True)

        # get damage reduction
        physical_reduction = 1 - (target.defense.damage_reduction_physical / 100)
        neutral_reduction = 1 - (target.defense.damage_reduction_neutral / 100)

        damage_reduction *= (physical_reduction * neutral_reduction)

        # get physical damage
        physical = int((
            ((damage.physical + bonus) * amplifier *
            defense * damage_reduction * type_advantage) * multiplier_crit
        ))

        # edit damage object
        damage.physical = physical

        return(damage)
    
    async def get_ki_damage(self, attacker, target, damage):
        """
        `coroutine`

        Calculate the Ki damage
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
        damage_reduction = 1
        amplifier = 1

        # increase the critical multiplier
        # in case of crit
        if(critical):
            multiplier_crit = 1.5 + (attacker.critical_bonus / 100)

        # get bonus value
        bonus = await self.get_bonus(attacker)

        # get the amplifier
        amplifier += (attacker.damage.amplifier_neutral + attacker.damage.amplifier_ki)

        # get defense value
        defense = await self.get_defense(target, damage, ki = True)

        # get damage reduction
        ki_reduction = 1 - (target.defense.damage_reduction_ki / 100)
        neutral_reduction = 1 - (target.defense.damage_reduction_neutral / 100)

        damage_reduction *= (ki_reduction * neutral_reduction)

        # get physical damage
        ki = int((
            ((damage.physical + bonus) * amplifier *
            defense * damage_reduction * type_advantage) * multiplier_crit
        ))

        # edit damage object
        damage.ki = ki

        return(damage)