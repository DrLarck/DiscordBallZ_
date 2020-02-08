"""
Combat object

--

Author : DrLarck

Last update : 08/02/20 (DrLarck)
"""

# dependancies
import asyncio
import random

# graphic
from utility.graphic.embed import Custom_embed
from utility.cog.displayer.move import Move_displayer

# util
from utility.cog.combat_system.input.input import Combat_input
from utility.cog.combat_system.attribute.move import Move
from utility.cog.fight_system.calculator.damage import Damage_calculator

class Combat():
    """
    Manages a combat

    - Parameter : 

    `client` (`discord.ext.commands.Bot`)

    `ctx` (`discord.ext.commands.context`)

    `teams` (`list` of `dict`) : {owner(str), team(list)}

    - Attribute :

    `player_a/b` (`Player()`) : Represents the play order, the player a plays before the player b

    - Method :

    :coro:`get_play_order()` : `None` - Defines the play order (player a and player b)

    :coro:`get_teams()` : `list`, `list` - Init the characters of both teams

    :coro:`display_teams()` : `None` - Display both teams as a single embed

    # combat
    :coro:`run()` : `Player()` - Run the fight
    """

    # attribute
    def __init__(self, client, ctx, teams):
        # bot
        self.client = client
        self.ctx = ctx
        self.teams = teams

        # players
        self.player_a, self.player_b = None, None
        self.team_a, self.team_b = None, None
        self.move = Move()

    # method
        # init
    async def get_play_order(self):
        """
        `coroutine`

        Defines the play order (player a and player b)

        --

        Return : `None`
        """

        # init 
        first = random.randint(0, 1)

        self.player_a = self.teams[first]["owner"]

        if(first == 0):
            self.player_b = self.teams[1]["owner"]
        
        else:
            self.player_b = self.teams[0]["owner"]

        return

    async def get_teams(self):
        """
        `coroutine`

        Init the characters of both teams

        --

        Return : `list` team a, `list` team b
        """

        # init
        team_a, team_b = [], []

        # get team a 
        team_a = await self.player_a.team.character()

        for char_a in team_a:
            await asyncio.sleep(0)

            await char_a.init()

        self.team_a = team_a

        # get team b 
        team_b = await self.player_b.team.character()

        for char_b in team_b:
            await asyncio.sleep(0)

            await char_b.init()
        
        self.team_b = team_b

        return(team_a, team_b)

    async def display_teams(self):
        """
        `coroutine`

        Display both teams as a single embed

        --

        Return : `None`
        """

        # init
        team_a_display, team_b_display = "", ""

        embed = await Custom_embed(
            self.client,
            title = "Teams"
        ).setup_embed()

        # displaying
        # team a
        for char_a in self.team_a:
            await asyncio.sleep(0)

            team_a_display += f"{char_a.image.icon}**{char_a.info.name}** - lv.**{char_a.level:,}**{char_a.type.icon} {char_a.rarity.icon}"

            team_a_display += "\n"
        
        for char_b in self.team_b:
            await asyncio.sleep(0)
        
            team_b_display += f"{char_b.image.icon}**{char_b.info.name}** - lv.**{char_b.level:,}**{char_b.type.icon} {char_b.rarity.icon}"

            team_b_display += "\n"

        # setting up the embed
        embed.add_field(
            name = f"🔵 **{self.player_a.name}**'s team",
            value = team_a_display,
            inline = False
        )

        embed.add_field(
            name = f"🔴 **{self.player_b.name}**'s team",
            value = team_b_display,
            inline = False
        )

        # sending the embed
        await self.ctx.send(embed = embed)

        return
    
    async def get_player_fighter(self, order):
        """
        `coroutine`

        Ask the player which character he wants to use this turn

        - Parameter : 

        `order` (`int`) : 0 for player A, 1 for player B
        
        --

        Return : `Character()`
        """

        # init
        team_display = ""
        index = 1

        team = None

        # if player a
        if(order == 0):
            team = self.team_a
            player = self.player_a
            circle = "🔵"
        
        else:
            team = self.team_b
            player = self.player_b
            circle = "🔴"
        
        # set embed
        embed = await Custom_embed(
            self.client,
            title = "Fighters",
            thumb = player.avatar
        ).setup_embed()
        
        # set player team display
        for char in team:
            await asyncio.sleep(0)

            posture, posture_icon = await char.posture.get_posture()
            team_display += f"`{index}`. {char.image.icon}**{char.info.name}** - **{char.health.current:,}**:hearts: *({int((char.health.current * 100) / char.health.maximum)} %)* {posture_icon}"

            team_display += "\n"
            index += 1
        
        embed.add_field(
            name = f"{circle}**{player.name}**'s team",
            value = team_display,
            inline = False
        )

        await self.ctx.send("Please select a fighter : Type its **index** number.")
        await self.ctx.send(embed = embed)
    
    async def get_target(self, player, team_a, team_b, target_ally = False, target_enemy = False, ignore_defenders = False):
        """
        `coroutine`

        Allows the player to get a target

        - Parameter :

        `player` (`Player()`)

        `team_a` (`list`) : The player's allied team

        `team_b` (`list`) : The player's enemy team

        `target_ally` (`bool`)

        `target_enemy` (`bool`)

        `ignore_defenders` (`bool`) : If it's set to `False` the defenders are ignored

        --

        Return : `Character()`
        """

        # init
        target = None
        targetable = []
        targetable_display = ""
        _input = Combat_input(self.client)

        # get the targetable characters
        if(target_ally):
            # add the allies 
            targetable += team_a
        
        if(target_enemy):
            # add the enemies
            if(ignore_defenders == False):  # ignore the defenders
                targetable += team_b
            
            else:  # get the defenders
                for enemy in team_b:
                    await asyncio.sleep(0)

                    if(enemy.posture.defending):
                        targetable.append(enemy)
        
        # set display
        target_index = 1

        for targetable_ in targetable:
            await asyncio.sleep(0)

            targetable_display += f"`{target_index}`. {targetable_.image.icon}**{targetable_.info.name}**{targetable_.type.icon} - **{targetable_.health.current:,}**:hearts: *({int((targetable_.health.current * 100) / targetable_.health.maximum)} %)*"

            targetable_display += "\n"

            target_index += 1
        
        embed = await Custom_embed(
            client = self.client,
            title = "Targets"
        ).setup_embed()

        embed.add_field(
            name = "Available targets",
            value = targetable_display,
            inline = False
        )

        await self.ctx.send("Please select a target among the following by typing its **index**")
        await self.ctx.send(embed = embed)

        # get the input
        possible_input = await _input.get_possible(targetable)
        player_input = int(await _input.wait_for_input(possible_input, player)) - 1
        
        target = targetable[player_input]

        return(target)
    
    async def battle(self, fighter, order):
        """
        `coroutine`

        Battle phase

        - Parameter 

        `fighter` (`Character()`)

        `order` (`int`)

        --

        Return : `None`
        """

        # init
        damager = Damage_calculator(fighter, self.move.target)
        display = ""
        move = Move_displayer()

        if(order == 0):
            player = self.player_a
            circle = ":blue_circle:"

            embed = await Custom_embed(
                self.client, title = "Battle phase", colour = 0x009dff
            ).setup_embed()
        
        else:
            player = self.player_b
            circle = ":red_circle"

            embed = await Custom_embed(
                self.client, title = "Battle phase", colour = 0xff0000
            ).setup_embed()

        # sequence move
        print(self.move.index)
        if(self.move.index == 0):
            damage = await damager.physical_damage(
                random.randint(fighter.damage.physical_min, fighter.damage.physical_max),
                dodgable = True,
                critable = True
            )

            move_info = {
                "name" : "Sequence",
                "icon" : "👊",
                "damage" : damage["calculated"],
                "critical" : damage["critical"],
                "dodge" : damage["dodge"],
                "physical" : True,
                "ki" : False
            }

            move = await move.offensive_move(move_info)
        
        # display
        embed.add_field(
            name = f"{circle}{fighter.image.icon}**{fighter.info.name}**{fighter.type.icon}'s move",
            value = move,
            inline = False
        )

        await self.ctx.send(embed = embed)

        return
    
    async def player_turn(self, player, order):
        """
        `coroutine`

        Gets thes input and throw the outputs for the current player

        - Parameter

        `player` (`Player()`)

        `order` (`int`) : Tells who's playing

        --

        Return : `None`
        """

        # init
        _input = Combat_input(self.client)
        fighter_action = "`1`. :punch:**Sequence**\n`2`. :fire:**Ki charge**\n`3`. :shield:**Defend**\n"
        possible_fighter = ["1", "2", "3"]

        # get the team order
        if(order == 0):
            team_a = self.team_a
            team_b = self.team_b
        
        else:
            team_a = self.team_b
            team_b = self.team_a

        # get the fighter
        await self.get_player_fighter(0)
        player_input = await _input.wait_for_input(possible_fighter, self.player_a)

        if(player_input != None):
            player_input = int(player_input) - 1

            player_fighter = self.team_a[player_input]
            
            # wait for an action
            action_index = 4

            for action in player_fighter.ability:
                await asyncio.sleep(0)

                ability = action(
                    self.client, self.ctx, player_fighter,
                    None, self.team_a, self.team_b
                )

                fighter_action += f"`{action_index}`. {ability.icon}**{ability.name}**"

                fighter_action += "\n"

                action_index += 1

            await self.ctx.send(
                f"Please select an action for {player_fighter.image.icon}**{player_fighter.info.name}** :\n{fighter_action}"
            )

            # get the move
            possible_move = await _input.get_possible(player_fighter.ability, ability = True)
            possible_move.append("1")
            possible_move.append("2")
            possible_move.append("3")
            possible_move.append("flee")

            player_move = await _input.wait_for_input(possible_move, self.player_a)
            
            if(player_move != "flee"):
                player_move = int(player_move) - 1

                if(player_move < 3):
                    # sequence
                    if(player_move == 0):
                        self.move.index = 0
                        self.move.target = await self.get_target(
                            player, team_a, team_b,
                            target_enemy = True
                        )
                    
                    else:
                        self.move.index = player_move

                else:
                    self.move.index = player_move

                    ability = await player_fighter.get_ability(
                        self.client, self.ctx, player_fighter, player_fighter, 
                        self.team_a, self.team_b, player_move - 3
                    )

                    if(ability.need_target):
                        self.move.target = await self.get_target(
                            player, team_a, team_b,
                            target_ally = ability.target_ally,
                            target_enemy = ability.target_enemy,
                            ignore_defenders = ability.ignore_defenders
                        )

            # execute the action
            await self.battle(player_fighter, order)
          
        return

    # combat
    async def run(self):
        """
        `coroutine`

        Run the combat

        --

        Return : `Player()`
        """ 

        # init
        await self.get_play_order()
        self.team_a, self.team_b = await self.get_teams()
        
        combat_end = False
        turn = 1

        # start the fight
        await self.ctx.send(f":blue_circle:**{self.player_a.name}** VS :red_circle:**{self.player_b.name}**")
        await asyncio.sleep(1)

        while not combat_end:
            if(turn == 1):
                await self.display_teams()
                await asyncio.sleep(1)
            
            # player a turn
            await self.player_turn(self.player_a, 0)
            
            # END OF THE TURN
            turn += 1

        return