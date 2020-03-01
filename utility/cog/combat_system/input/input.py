"""
Combat input object

--

Author : DrLarck

Last update : 15/02/20 (DrLarck)
"""

# dependancies
import asyncio

class Combat_input():
    """
    Manages the combat inputs

    - Method


    """

    def __init__(self, client):
        self.client = client
        self.timeout = 120
    
    async def get_possible(self, options, team_a, team_b, ability = False):
        """
        `coroutine`

        Generate a `list` of `str digits` for the possible choices the player can make from an `option` list

        - Parameter :

        `options` (`list`) : List of possible actions, inputs, etc.

        --

        Return : `list` of `str digits`
        """

        # init
        possible = []
        teams = team_a + team_b
        index = 1

        if(ability):  # defines the amount of abilities the player can use
            start = 1
            end = len(options) + 1
        
        else:
            start = 1
            end = len(options) + 1

        if(len(options) > 0):
            # get the index of the usable 
            for a in range(start, end):
                await asyncio.sleep(0)

                possible.append(str(a))
            
        for character in teams:
            await asyncio.sleep(0)

            possible.append(f"check {index}")

            index += 1

        return(possible)


    async def wait_for_input(self, possible_choice, player):
        """
        `coroutine`

        Wait for an input from the player that is in the possible choice list

        - Parameter :

        `possible_choice` (`list` or `str`) : List of possible inputs the player can make

        `player` (`Player()`) : The player input to listen

        --

        Return : `input` or `None` in case of `TimeOutError`
        """

        # init
        player_imput = None

        def predicate(message):
            """
            Check if the `message` content is in `possible_choice` and if the author is `player`

            --

            Return : `bool`
            """

            # init
            content = message.content
            content = content.lower()
            
            if(message.author.id == player.id):
                if(content in possible_choice):
                    return(True)
                
                else:
                    return(False)

        # get the imput
        try:
            player_imput = await self.client.wait_for(
                "message", timeout = self.timeout, check = predicate
            )
        
        except asyncio.TimeoutError:
            return(None)
        
        except Exception as error:
            print(f"(COMBAT INPUT : WAIT_FOR_INPUT) Error : {error}.")
            return(None)
        
        else:  # worked
            player_imput = (player_imput.content).lower()

        return(player_imput)