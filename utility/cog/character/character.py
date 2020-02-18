"""
Every character classes inherit from the :class:`Character()` defined below.

--

Author : DrLarck

Last update : 17/02/20 (DrLarck)
"""

# dependancies
import asyncio
from random import randint, choice

# attribute
from utility.cog.character.attribute.info import Character_info
from utility.cog.character.attribute.image import Character_image
from utility.cog.character.attribute.type import Character_type
from utility.cog.character.attribute.rarity import Character_rarity

from utility.cog.character.attribute.posture import Character_posture
from utility.cog.character.attribute.health import Character_health
from utility.cog.character.attribute.ki import Character_ki
from utility.cog.character.attribute.damage import Character_damage

from utility.cog.character.attribute.defense import Character_defense
from utility.cog.character.attribute.regenation import Character_regen

# utils
from utility.cog.displayer.team import Team_displayer
from utility.cog.displayer.icon import Icon_displayer
from utility.cog.displayer.category import Category_displayer

# character class
class Character:
    """
    Every character classes inherit from this one.

    Defines what a character is and all the possible interaction you can have with it.

    - Attribute : 

    `info` : Represents the character's basic infos.

    `image` : Represents the character's images

    `type` : Represents the character's type.

    `rarity` : Represents the character's rarity.

    `is_init` : bool - Tells if the character has been init or not.

    `level` : Represents the character's level.

    `posture` : Represents the character's posture.

    `health` = Represents the character's health.

    `ki` : Represents the character's ki.

    `damage` : Represents the character's damage.

    `critical_chance` : Represents the character's crit chance.

    `critical_bonus` : Represents the character's crit bonus.

    `defense` : Represents the character's defense.

    `regeneration` : Represents the character's regen.

    `bonus` : Represents the character's bonus effect.

    `malus` Represents the character's malus effect.

    `ability` : Represents the character's abilities.

    `passive` : Represents the character's passive.

    `leader` : Represents the character's leader.

    `enhancement` : dict  {
        "star" : 0,
        "training" : dict {
            "defense" : dict {
                "health" : 0,
                "armor" : 0,
                "spirit" : 0
            },
            "damage" : dict {
                "physical" : 0,
                "ki" : 0
            }
        }
    }

    `ability_sorted` : bool - Tells if the ability list has been replaced

    - Method :

    :coro:`init()` : Translates strings and initializes the stats.

    :coro:`set_stat()` : Initializes the stats.

    :coro:`translate()` : Translates the names

    :coro:`receive_damage()` : Inflicts the damages to the character and triggers the effects based on the type of the attack and if the character dies or not.

    :coro:`use_ability()` : Uses the passed ability as parameter.

    :coro:`trigger_passive()` : Triggers the passive ability.

    :coro:`trigger_leader()` : Triggers the leader skill.

    :coro:`bot()` : Triggers the AI.
    """

    # attribute
    def __init__(self):
        # bot
        self.is_npc = False  # if true, the action will automatically be managed by the AI
        self.played = False  # if true, the character cannot be played this turn
        self.is_minion = False  # a minion is a character supporter such as Cell Jr.
        
        # basic info
        self.info = Character_info()
        self.image = Character_image()
        self.type = Character_type()
        self.rarity = Character_rarity()
        self.is_init = False

        # characteristics
        self.level = 0

        # represent the character's posture
        # if all the postures are set to False it means that the character is
        # attacking
        # default : "attacking" = True
        self.posture = Character_posture()

        # if the current health reaches 0, the character dies
        self.health = Character_health()

        # by default the maximum ki is 100
        self.ki = Character_ki()

        # 2 types of damage : Physical and Ki one
        self.damage = Character_damage()

        # the critical values are in %
        self.critical_chance = 0
        self.critical_bonus = 0

        # 2 types of defense : Physical and Ki, repectively "Armor" and "Spirit"
        # the "reduction" key value is in % as well as "parry" and "dodge"
        self.defense = Character_defense()

        # represents the stats that are generated by the character at each turn
        self.regeneration = Character_regen()

            # bonus stat
            # used for the stats calculation
            # each value represent an amount of item used
            # basically the player won't be able to use more than
            # 10 training items
        self.enhancement = {
            "star" : 0,
            "training" : {
                "defense" : {
                    "health" : 0,
                    "armor" : 0,
                    "spirit" : 0
                },
                "damage" : {
                    "physical" : 0,
                    "ki" : 0
                }
            }
        }

        # effect
        # list of effects
        self.bonus = []
        self.malus = []

        # ability
        # list of abilities
        self.ability_sorted = False
        self.ability = []

        self.passive_sorted = False
        self.passive_start = []  # Passive skill that must be triggered at the beginning of the turn
        self.passive_end = []  

        self.leader_sorted = False
        self.leader = []

        # on event
        self.on_death_sorted = False
        self.on_death_triggered = False
        self.on_death = []  # on dying effect
        
    #####################
    # method
        # init
    async def init(self):
        """
        `coroutine`

        Initializes the character by : 
        - Translating its name
        - Setting up its characteristics

        --

        Return : None
        """

        # init
        icon = Icon_displayer()
        category = Category_displayer()

        # set stat
        if(self.is_init == False):
            await self.set_stat()

            # set display
            self.rarity.icon = await icon.get_rarity_icon(self.rarity.value)
            self.type.icon = await icon.get_type_icon(self.type.value)
            self.info.expansion, self.image.expansion = await category.get_expansion(self.info.expansion)

            # icons
                # type
            self.type.icon = await icon.get_type_icon(self.type.value)
                # rarity
            self.rarity.icon = await icon.get_rarity_icon(self.rarity.value)

            # translation
            await self.translate()

            self.is_init = True
        
        else:
            pass

        return
    
    async def set_stat(self):
        """
        `coroutine`

        Initializes the character's stats.

        --

        Return : None
        """
        
        # get the level multiplier
        level_multiplier = self.level / 100

        level_multiplier = 1 + (level_multiplier + ((self.enhancement["star"] * 10) / 100))

        # setup health
        self.health.maximum = int((self.health.maximum * level_multiplier) * (1 + ((self.rarity.value * 20) / 100) + (250 * self.enhancement["training"]["defense"]["health"])))
        self.health.current = self.health.maximum

        # setup damage
        self.damage.physical_max = int((self.damage.physical_max * level_multiplier) * ((1 + ((self.rarity.value) * 20) / 100 + (50 * self.enhancement["training"]["damage"]["physical"]))))
        self.damage.physical_min = int(0.9 * self.damage.physical_max)

        self.damage.ki_max = int((self.damage.ki_max * level_multiplier) * ((1 + ((self.rarity.value) * 20) / 100 + (50 * self.enhancement["training"]["damage"]["ki"]))))
        self.damage.ki_min = int(0.9 * self.damage.ki_max)

        # setup defense
        self.defense.armor = int((self.defense.armor * level_multiplier) * ((1 + ((self.rarity.value) * 20) / 100 + (50 * self.enhancement["training"]["defense"]["armor"]))))
        self.defense.spirit = int((self.defense.spirit * level_multiplier) * ((1 +((self.rarity.value) * 20) / 100 + (50 * self.enhancement["training"]["defense"]["spirit"]))))

        return
    
    async def translate(self):
        return
    
    async def receive_damage(self, damage, attacker):
        """
        `coroutine`

        Applies the received damages.

        - Parameter :

        `damage` : Represents the damage received. (int)

        `attacker` (`Character()`)

        --

        Return : None
        """
        
        # only applies the effect if the character is alive
        if(self.health.current > 0):
            # check if the target is gonna die after this attack
            gonna_die = False

            if(damage >= self.health.current):  # the damages are going to kill it
                gonna_die = True

            # apply the damage
            self.health.current -= damage
            await self.health.health_limit()

            if(gonna_die):  # if the attack killed the character
                # trigger the dying effects.
                pass

        return
    
    # ability
    async def get_ability(self, client, ctx, caster, target, team_a, team_b, ability_index):
        """
        `coroutine`

        Uses the passed ability.

        - Parameter : 

        `client` : Represents the `discord.Client`.

        `ctx` : Represents the `commands.Context`.

        `target` : Represents a `Character()` instance.

        `team_a` | `team_b` : Represents a list of characters representing a team. Team a is the caster's team.

        `ability_index` : Represents the ability index in the `ability` list.

        --

        Return : `Ability()` instance.
        """
        
        # find the ability then create an instance of it
        ability = self.ability[ability_index]
        if(self.ability_sorted == False):
            ability = ability(
                client,
                ctx,
                caster,
                target,
                team_a,
                team_b
            )
        
        else:
            # pass the parameter to the ability instance
            ability.__init__(
                client,
                ctx,
                caster,
                target,
                team_a,
                team_b
            )

        return(ability)
        
        # triggers
    async def trigger_passive(self, start = False, end = False):
        """
        `coroutine`

        Triggers all the passive skills.

        --

        Return : None
        """

        # init
        passive = []

        if(start):  # add the passive that are triggered at the beginning of the turn
            passive += self.passive_start
        
        if(end):
            passive += self.passive_end

        if(len(passive) > 0):  # if there is some passive skills in it
            for _passive in passive:  # triggers the effects one by one
                await asyncio.sleep(0)

                await _passive.apply()
        
        else:  # if the passive list is empty we return
            return
        
        return
    
    async def trigger_leader(self):
        """
        `coroutine`

        Triggers all the leader skills.

        --

        Return : None
        """

        # init
        leader = self.leader

        if(len(leader) > 0):
            for _leader in leader:
                await asyncio.sleep(0)

                await _leader.apply()
        
        else:
            return
        
        return
    
        # artificial intelligence
    async def bot(self, client, ctx, player, team_a, team_b, turn):
        """
        `coroutine`

        Defines the character gameplay. The bot will play as defined in this method.

        - Parameter :

        `client` : Represents a `discord.Client`

        `ctx` : Represents the `commands.Context`

        `player` : Represents the player who called the command

        `team_a` : Allied team of the character

        `team_b` : Opponent team of the character

        `turn` : Represents the current turn number.

        --

        Return : None
        """

        # init
        ability_list = []
        usable_ability = []

        team_displayer = Team_displayer(
            client,
            ctx,
            player,
            team_a,
            team_b
        )

        move = {
            "move" : 3,
            "target" : None
        }  # init to defend

        # turn 1 manager
        if(turn == 1):
            possible_move = [0, 2]
            move["move"] = choice(possible_move)

            return(move)

        ############
        # set a list of abilities
        if(len(self.ability) > 0):
            for i in range(len(self.ability)):
                await asyncio.sleep(0)
                
                ability = await self.get_ability(client, ctx, self, None, team_a, team_b, i)
                ability_list.append(ability)

            # order the list
            # if the ability is less expansive then the targetted ability
            # replace it in the list
            for _ability in ability_list:
                await asyncio.sleep(0)

                for a in range(len(ability_list)):
                    await asyncio.sleep(0)

                    if(_ability.cost < ability_list[a].cost):
                        ability_list.remove(_ability)
                        ability_list.insert(a, _ability)
                        break
            
            # get a list of usable ability
            for __ability in ability_list:
                await asyncio.sleep(0)

                if(self.ki.current >= __ability.cost):
                    if(__ability.cooldown <= 0):
                        usable_ability.append(__ability)
                
                else:
                    break
        
        # decide if launch an ability or use an other move
        if(len(usable_ability) > 0):  # if the character has an ability
            random_move = randint(1, 4)
        
        else:  # else if the character doesn't have any ability
            random_move = randint(0, 2)

        if(random_move < 3):  # do not use an ability
            move["move"] = random_move

            if(move["move"] == 0):  # if sequence
                # find the targetable targets
                targetable_a, targetable_b = await team_displayer.get_targetable("sequence")
                targetable = targetable_a + targetable_b

                # pick a random target
                move["target"] = choice(targetable)
        
        else:  # wants to use an ability
            # if the character has enough ki to use any ability
            if(len(usable_ability) > 0):
                # pick a random ability in the usuable abilities list
                # pick a random ability
                ability_choice = 3  # init to 3, 3 is the ability 1 (index 0)
                random_ability = randint(0, len(usable_ability) - 1)

                # get the ability object with the random obtained index.
                ability = usable_ability[random_ability]

                ability_choice += random_ability  # add random choice to ability (4) to define which ability has been used

                # get targetable
                if(ability.need_target):
                    targetable_a, targetable_b = await team_displayer.get_targetable(
                        "ability",
                        ability = ability
                    )

                    targetable = targetable_a + targetable_b

                    move["target"] = choice(targetable)

                move["move"] = ability_choice
            
            else:  # do not have enough ki to use an ability
                move["move"] = 1

        return(move)