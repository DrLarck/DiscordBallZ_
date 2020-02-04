"""
Manages the battle phase.

-- 

Author : Zyorhist

Last update : 03/02/20 (DrLarck)
"""

"""
        The turn order should be processed as follows

        initiate battle
        - setup teams
        - get opponents
        - randomly assign team to "team a"
        - assign other team to "team b"

        Round order
        1) Display Current matchup
        - only needs to show each team's characters hp and type
        2) Team a turn (turn 1, 3, 5, ...)
        3) team b turn (turn 2, 4, 6, ...)


        Turn order
        1) Upkeep phase 
        - checks active players characters, updating buffs/debuffs 
        - double check stats for active characters
        2) Player action
        - player can use 1 combat item before selecting characters to use
        3) select fighter
        - pick which team member to use first
        4) select action
        - action is performed immediately
        - ki is gained after action is performed
        - return to "3) select fighter" until all team members have acted
        5) end of turn effects
        - "end of turn" abilities trigger
        - dot's apply
        6) timers reduce
        - buff/debuff timers reduce for active team only by 1
        7) pass to other player
        - new turn with next player in control.
        - if both players have acted this round, move to next round
        - turn number +1 (one player will always act on odd turns, the other will always act on even turns)

        during turn 1, only for first player not both players,
        team members can only choose between defend and charge (changed from defend and skip)

"""