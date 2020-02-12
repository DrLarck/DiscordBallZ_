"""
Manages the damage calculator.

--

Author : Zyorhist

Last update : 03/02/20 (DrLarck)
"""
"""
        Order of events to follow

        1) Check for dodge first.  If the ability or attack is dodged, do nothing effects dont apply.

        2) get all of the set variables
        find dodge
        find type advantage
        get ki_damage
        get physical_damage
        get true_damage
        get variance
        get momentum

        3) get bonuses
        get ki_bonus (from buff effects)
        get physical_bonus (from buff effects)
        add bonuses to damage

        4) get amplifiers
        get multipliers from buff effects
        multiply variance, type advantage, crit, and multipliers

        5) get defense 
        get defense values
        multiply by defense formula

        6) get damage reduction
        get damage reduction from buffs
        multiply by damage reduction

        7) return total

        full formula

        ki_damage = 
        ([ki damage from abilty] + [bonus from buffs]) * ([type advantage] * [ki amplifiers from buffs] * [neutral amplifiers from buffs] * [crit] * [variance]) * {next line}
        ((2500 + ([momentum from ability] + [momentum from buffs])) / (2500 + [spirit])) * ([ki damage reduction] * [neutral damage reduction])

        physical_damage = 
        ([physical damage from abilty] + [bonus from buffs]) * ([type advantage] * [physical amplifiers from buffs] * [neutral amplifiers from buffs] * [crit] * [variance]) * {next line}
        ((2500 + ([momentum from ability] + [momentum from buffs])) / (2500 + [armor])) * ([physical damage reduction] * [neutral damage reduction])

        true_damage = 
        true damage value from ability

        total_damage = 
        ki damage + physical damage + true damage

"""