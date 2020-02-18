"""
Manages the character getter.

--

Author : DrLarck

Last update : 16/02/20 (DrLarck)
"""

# dependancies
import asyncio

# database
from utility.database.database_manager import Database

# getter
class Character_getter:
    """
    Manages the character getters.

    - Attribute :

    `character_list` : List of all the characters existing in the game.

    `special_character` : List of non-summonable characters.

    - Method : 

    :coro:`get_character(character_id)` : Returns an instance of a character. The character id must be type int. Return None if not found.

    :coro:`get_summonable()` : Returns the list of summonable characters (id).

    :coro:`get_from_unique(unique_id)` : Get a character instance from its unique id
    """

    # attribute
    def __init__(self):
        # non-summonable characters
        self.special_character = []

        # list of all the characters in the game
        self.character_list = [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            11, 12, 13, 14, 15, 16 ,17, 18, 19, 20,
            21, 22, 23, 24 , 25, 26, 27, 28, 29, 30,
            31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
            41, 42, 43, 44, 45, 46
        ]

    # method
    async def get_character(self, character_id):
        """
        `coroutine`

        Get a character instance according to the passed id.

        --

        Return : Character instance, otherwise : None
        """

        # init
        character = None

        # Green Saibaiman
        if(character_id == 1):
            from utility.cog.character.list.c001_sabimen import Character_001

            character = Character_001()
        
        # Blue Saibaiman
        if(character_id == 2):
            from utility.cog.character.list.c002_sabimen import Character_002

            character = Character_002()
        
        # Red Saibaiman
        if(character_id == 3):
            from utility.cog.character.list.c003_sabimen import Character_003

            character = Character_003()
        
        # Pilaf Machine
        if(character_id == 4):
            from utility.cog.character.list.c004_pilafmachine import Character_004

            character = Character_004()
        
        # Piccolo
        if(character_id == 5):
            from utility.cog.character.list.c005_piccolo import Character_005

            character = Character_005()

        # Bardock
        if(character_id == 6):
            from utility.cog.character.list.c006_broly import Character_006

            character = Character_006()
        
        if(character_id == 7):
            from utility.cog.character.list.c007_superbuu import Character_007

            character = Character_007()
        
        if(character_id == 8):
            from utility.cog.character.list.c008_goten import Character_008

            character = Character_008()
        
        if(character_id == 9):
            from utility.cog.character.list.c009_turles import Character_009

            character = Character_009()
        
        if(character_id == 10):
            from utility.cog.character.list.c010_launch import Character_010

            character = Character_010()

        if(character_id == 11):
            from utility.cog.character.list.c011_redribbonsoldier import Character_011

            character = Character_011()

        if(character_id == 12):
            from utility.cog.character.list.c012_zarbon import Character_012
                    
            character = Character_012()

        if(character_id == 13):
            from utility.cog.character.list.c013_hercule import Character_013
                    
            character = Character_013()

        if(character_id == 14):
            from utility.cog.character.list.c014_chiaotzu import Character_014
                    
            character = Character_014()

        if(character_id == 15):
            from utility.cog.character.list.c015_killa import Character_015
                    
            character = Character_015()
            
        if(character_id == 16):
            from utility.cog.character.list.c016_yamcha import Character_016
                    
            character = Character_016()
            
        if(character_id == 17):
            from utility.cog.character.list.c017_tien import Character_017
                    
            character = Character_017()
            
        if(character_id == 18):
            from utility.cog.character.list.c018_hit import Character_018
                    
            character = Character_018()
            
        if(character_id == 19):
            from utility.cog.character.list.c019_cumber import Character_019
                    
            character = Character_019()
            
        if(character_id == 20):
            from utility.cog.character.list.c020_dende import Character_020
                    
            character = Character_020()
                        
        if(character_id == 21):
            from utility.cog.character.list.c021_jiren import Character_021
                    
            character = Character_021()
                        
        if(character_id == 22):
            from utility.cog.character.list.c022_android16 import Character_022
                    
            character = Character_022()
                        
        if(character_id == 23):
            from utility.cog.character.list.c023_android17 import Character_023
                    
            character = Character_023()
                        
        if(character_id == 24):
            from utility.cog.character.list.c024_android18 import Character_024
                    
            character = Character_024()
                        
        if(character_id == 25):
            from utility.cog.character.list.c025_android19 import Character_025
                    
            character = Character_025()
                        
        if(character_id == 26):
            from utility.cog.character.list.c026_bardock import Character_026
                    
            character = Character_026()
                        
        if(character_id == 27):
            from utility.cog.character.list.c027_fasha import Character_027
                    
            character = Character_027()
                        
        if(character_id == 28):
            from utility.cog.character.list.c028_shugesh import Character_028
                    
            character = Character_028()
                        
        if(character_id == 29):
            from utility.cog.character.list.c029_borgos import Character_029
                    
            character = Character_029()
                        
        if(character_id == 30):
            from utility.cog.character.list.c030_tora import Character_030
                    
            character = Character_030()
                                    
        if(character_id == 31):
            from utility.cog.character.list.c031_guldo import Character_031
                    
            character = Character_031()
                                    
        if(character_id == 32):
            from utility.cog.character.list.c032_burter import Character_032
                    
            character = Character_032()
                                    
        if(character_id == 33):
            from utility.cog.character.list.c033_jeice import Character_033
                    
            character = Character_033()
                                    
        if(character_id == 34):
            from utility.cog.character.list.c034_recoome import Character_034
                    
            character = Character_034()
                                    
        if(character_id == 35):
            from utility.cog.character.list.c035_ginyu import Character_035
                    
            character = Character_035()
                                    
        if(character_id == 36):
            from utility.cog.character.list.c036_frieza import Character_036
                    
            character = Character_036()
                                    
        if(character_id == 37):
            from utility.cog.character.list.c037_yemma import Character_037
                
            character = Character_037()
                                    
        if(character_id == 38):
            from utility.cog.character.list.c038_cell import Character_038
                    
            character = Character_038()
                                    
        if(character_id == 39):
            from utility.cog.character.list.c039_goku import Character_039
                    
            character = Character_039()
                                    
        if(character_id == 40):
            from utility.cog.character.list.c040_gohan import Character_040
                    
            character = Character_040()
                                    
        if(character_id == 41):
            from utility.cog.character.list.c041_pan import Character_041
                    
            character = Character_041()
                                    
        if(character_id == 42):
            from utility.cog.character.list.c042_janemba import Character_042
                    
            character = Character_042()
                                    
        if(character_id == 43):
            from utility.cog.character.list.c043_krillin import Character_043
                    
            character = Character_043()
                                    
        if(character_id == 44):
            from utility.cog.character.list.c044_vegeta import Character_044
                    
            character = Character_044()
                                    
        if(character_id == 45):
            from utility.cog.character.list.c045_trunks import Character_045
                    
            character = Character_045()
        
        if(character_id == 46):
            from utility.cog.character.list.c046_bardockSsj import Character_046

            character = Character_046()
                                    
        return(character)
    
    async def get_summonable(self):
        """
        `coroutine`

        Get the list of summonable characters. Remove the special characters.

        --

        Return : list of summonable characters
        """

        # init
        summonable = self.character_list

        for character in summonable:
            await asyncio.sleep(0)

            if character in self.special_character:  # if the character is a special one
                summonable.remove(character)
            
            else:
                pass

        return(summonable)
    
    async def get_from_unique(self, client, unique_id):
        """
        `coroutine`

        Get a character instance from its unique id.

        - Parameter : 

        `client` : Represents a `discord.Client`. The client must contain a connection pool to the database.

        `unique_id` : str - Represents the character's unique id to look for.

        --

        Return : character instance. None if not found.
        """

        # init
        db = Database(client.db)
        character = None
        char_father = await db.fetch(
            f"SELECT * FROM character_unique WHERE character_unique_id = '{unique_id}';"
        )

        if(len(char_father) > 0):
            # sort the data
            char_id = char_father[0][4]
            char_type = char_father[0][5]
            char_rarity = char_father[0][6]
            char_level = char_father[0][7]
            char_star = char_father[0][9]
            char_training = {
                "health" : char_father[0][10],
                "armor" : char_father[0][11],
                "spirit" : char_father[0][12],
                "physical" : char_father[0][13],
                "ki" : char_father[0][14]
            }

            # get the character instance
            character = await self.get_character(char_id)

            # set the character's stats
            character.type.value = char_type
            character.rarity.value = char_rarity
            character.level = char_level
            
                # training items
            character.enhancement["star"] = char_star
            character.enhancement["training"]["defense"]["health"] = char_training["health"]
            character.enhancement["training"]["defense"]["armor"] = char_training["armor"]
            character.enhancement["training"]["defense"]["armor"] = char_training["spirit"]
            character.enhancement["training"]["damage"]["physical"] = char_training["physical"]
            character.enhancement["training"]["damage"]["ki"] = char_training["ki"]

            # init the object
            await character.init()

        return(character)