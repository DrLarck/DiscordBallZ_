'''
Get the player's move.

Last update: 26/06/19
'''

# Dependancies

import asyncio
from time import strftime, gmtime

async def Wait_for_move(client, player, fighter, all_fighter):
    '''
    `coroutine`

    Wait for the player's choice.

    `client` : must be `discord.Client` object.

    `player` : must be `discord.Member` object.

    `fighter` : must be `Character` object.

    Return : bool, int (True if the choice has been registered successfully or False otherwise) (success, move)
    '''

    # Init

    fighter_ability_count = len(fighter.ability_list)
    success = False

    def Correct_move(message):
        if(message.author == player):
            choice = message.content
            choice = choice.split()

            if(len(choice) == 1):  # If there is only flee or ki charge
                if(choice[0].isdigit()):
                    choice[0] = int(choice[0])  # Choice has now the correct len, we check if the choice is correct now

                    if(choice[0] > 0 and choice[0] <= fighter_ability_count+3):  # If the choice is != 0 and that it's a number not too high for the amount of available moves
                        return(True)
                    
                    else:  # Not a correct move
                        return(False)
                
                else:  # Non digit
                    if(choice[0].upper() == 'FLEE'):  # if flee
                        return(True)
                    
                    else:  # if not flee or see
                        return(False)
            
            elif(len(choice) == 2):
                if(choice[0].upper() == 'CHECK'):  # if player want to check a character
                    if(choice[1].isdigit()):  # if he defined the target
                        choice[1] = int(choice[1])

                        if(choice[1] <= len(all_fighter)):  # if the target is ok
                            return(True)
                        
                        else:  # if target not ok
                            return(False)
                    
                    else:  # if not target
                        return(False)
                
                else:  # if not check
                    return(False)

        else:  # message author
            return(False)
    
    # Now we get the answer

    try:
        choice = await client.wait_for('message', timeout = 300, check = Correct_move)
    
    except asyncio.TimeoutError:
        success = False
        return(success, 'flee')
    
    except Exception as error:
        error_time = strftime('%d/%m/%y - %H:%M', gmtime())
        print('{} Error in cogs.utils.functions.commands.fight.wait_for.wait_for_move.Wait_for.move() : l.54 : {}'.format(error_time, error))
        success = False
        pass
    
    else:
        success = True
    
    # If everything is good we return the choice

    if(success):
        choice = choice.content
        choice = choice.split()

        if(len(choice) == 1):
            if(choice[0].isdigit()):  # if num
                choice[0] = int(choice[0])
                return(success, choice[0])
            
            else:  # if not digit
                if(choice[0].upper() == 'FLEE'):  # if flee
                    return(success, 'flee')

        elif(len(choice) == 2):
            if(choice[0].upper() == 'CHECK'):  # if check target
                if(choice[1].isdigit()):  # if correct
                    choice[1] = int(choice[1])

                    if(choice[1] <= len(all_fighter)):
                        choice[1] = int(choice[1])  
                        choice = ['CHECK', all_fighter[choice[1]-1], choice[1]]  # return ['CHECK', target.object, order]
                        return(success, choice)

        else:
            return(False)

    else:
        return(False)