"""
Load the cogs.

--

Author : DrLarck

Last update : 15/02/2020 (DrLarck)
"""

# dependancies
from discord.ext import commands

class Cog_loader:
    """
    Load the cogs and throw an error in the console if a cog cannot be loaded properly.

    - Parameter : 

    `client` : Represents the `Client`.

    - Attribute :

    `cog` : List of cogs to load.

    `client` : Represents the `Client`.

    - Method :
    
    `load_cog()` : Loads all the cogs stored in the `cog` attribute.
    """

    # attribute
    def __init__(self, client):
        self.client = client
        self.cog = [
            # command
            "cog.command.help",
            "cog.command.train", "cog.command.summon", "cog.command.box",
            "cog.command.start", "cog.command.team", "cog.command.show",
            "cog.command.profile", "cog.command.cancel", "cog.command.mission",
            "cog.command.pvp",
            # other
            "cog.event.on_event",
            # BETA
            "cog.command.beta"
        ]
    
    # method

    def load_cog(self):
        """
        Loads all the cogs stored in the `cog` attribute.
        """

        for cog in self.cog:
            try:
                self.client.load_extension(cog)
            
            except commands.ExtensionNotFound as error:
                print(f"(LOADING COG : NOT FOUND) - Error while loading {cog} : {error}\n")
                pass
            
            except commands.ExtensionAlreadyLoaded as error:
                print(f"(LOADING COG : ALREADY LOADED) - Error while loading {cog} : {error}\n")
                pass

            except commands.ExtensionFailed as error:
                print(f"(LOADING COG : FAILED) - Error while loading {cog} : {error}\n")
                pass
            
            except commands.NoEntryPointError as error:
                print(f"(LOADING COG : ENTRY POINT ERROR) - Error while loading {cog} : {error}\n")
                pass

            except Exception as error:
                print(f"(LOADING COG) - Error while loading {cog} : {error}\n")
                pass
        
        return