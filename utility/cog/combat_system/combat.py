"""
Combat object

--

Author : DrLarck

Last update : 03/03/20 (DrLarck)
"""

# dependancies
import asyncio
import random

# graphic
from utility.graphic.embed import Custom_embed
from utility.cog.displayer.move import Move_displayer
from configuration.icon import game_icon

# util
from utility.cog.combat_system.input.input import Combat_input
from utility.cog.combat_system.attribute.move import Move
from utility.cog.combat_system.damage.calculator import Damage_calculator
from utility.cog.character.getter import Character_getter

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
        self.team_a, self.team_b = [], []
        self.team_a_, self.team_b_ = [], []  # copies of the team a and b to allow the player to target the removed fighters
        self.leader_a, self.leader_b = [], []
        self.removed_a, self.removed_b = [], []
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
        # 0 = team[0]
        # 1 = team[1]
        first = random.randint(0, 1)

        # get the player_a instance
        self.player_a = self.teams[first]["owner"]

        # if the first player is the team[0]
        # the second player is the other team
        if(first == 0):
            self.player_b = self.teams[1]["owner"]
        
        # vice versa
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

        # init the characters
        for char_a in team_a:
            await asyncio.sleep(0)

            await char_a.init()

        self.team_a = team_a

        # get team b 
        team_b = await self.player_b.team.character()

        # init the characters
        for char_b in team_b:
            await asyncio.sleep(0)

            await char_b.init()
        
        self.team_b = team_b

        # set the copies
        for character_a in self.team_a:
            await asyncio.sleep(0)

            self.team_a_.append(character_a)

        for character_b in self.team_b:
            await asyncio.sleep(0)

            self.team_b_.append(character_b)
        
        # set leader
        leader_a = self.team_a[0]
        leader_b = self.team_b[0]

        self.leader_a = leader_a
        self.leader_b = leader_b

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

        Return : `list`
        """

        # init
        team_display = ""
        index = 1

        playable = []

        # if player a
        if(order == 0):
            team = self.team_a
            player = self.player_a
            removed = self.removed_a
            color = 0x009dff
            circle = "🔵"
        
        else:
            team = self.team_b
            player = self.player_b
            removed = self.removed_b
            color = 0xff0000
            circle = "🔴"
    
        # set embed
        embed = await Custom_embed(
            self.client,
            title = "Fighters",
            thumb = player.avatar,
            colour = color
        ).setup_embed()
    
        # set player team display
        for char in team:
            await asyncio.sleep(0)

            if not char.played and char.health.current > 0 and char.posture.stunned == False:
                posture, posture_icon = await char.posture.get_posture()
                team_display += f"`{index}`. {char.image.icon}**{char.info.name}**{char.type.icon} - **{char.health.current:,}**:hearts: *({int((char.health.current * 100) / char.health.maximum)} %)* {posture_icon}"

                team_display += "\n"
                index += 1
                playable.append(char)
        
        embed.add_field(
            name = f"{circle}**{player.name}**'s team",
            value = team_display,
            inline = False
        )

        if not player.is_cpu:
            await self.ctx.send(embed = embed)

        return(playable)
    
    async def get_target(self, player, team_a, team_b, order, target_ally = False, target_enemy = False, ignore_defenders = False):
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

        `order` (`int`) : Turn order

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
            if(ignore_defenders == True):  # ignore the defenders
                targetable += team_b
            
            else:  # get the defenders
                for enemy in team_b:
                    await asyncio.sleep(0)

                    if(enemy.posture.defending and enemy.health.current > 0):
                        targetable.append(enemy)
                
                if(len(targetable) <= 0):  # if there is no defenders
                    targetable += team_b
        
        # set display
        target_index = 1
        dead = []

        for targetable_ in targetable:
            await asyncio.sleep(0)
            
            if(targetable_.health.current > 0):
                targetable_display += f"`{target_index}`. {targetable_.image.icon}**{targetable_.info.name}**{targetable_.type.icon} - **{targetable_.health.current:,}**:hearts: *({int((targetable_.health.current * 100) / targetable_.health.maximum)} %)*"

                targetable_display += "\n"

                target_index += 1
            
            else:  
                dead.append(targetable_)
        
        # remove the dead characters
        for char in dead:
            await asyncio.sleep(0)

            targetable.remove(char)
            team_b.remove(char)

        # define the color of the embed
        if(order == 0):
            color = 0x009dff
            circle = "🔵"
        
        else:
            color = 0xff0000
            circle = "🔴"

        # if the displaying is empty
        if(targetable_display == ""):
            targetable_display = "None target available"

        embed = await Custom_embed(
            client = self.client,
            title = "Targets",
            colour = color
        ).setup_embed()

        embed.add_field(
            name = "Available targets",
            value = targetable_display,
            inline = False
        )

        await self.ctx.send(embed = embed)
        await self.ctx.send(f"Please {circle}**{player.name}** select a target among the following by typing its **index**")

        # get the input
        possible_input = await _input.get_possible(targetable, team_a, team_b)
        player_input = int(await _input.wait_for_input(possible_input, player)) - 1
        
        target = targetable[player_input]

        return(target)
    
    async def battle(self, fighter, order, turn):
        """
        `coroutine`

        Battle phase

        - Parameter 

        `fighter` (`Character()`)

        `order` (`int`)

        `turn` (`int`)

        --

        Return : `None`
        """

        # init
        display = ""
        move = Move_displayer()

        if(order == 0):
            player = self.player_a
            circle = ":blue_circle:"
            _circle = ":red_circle:"

            embed = await Custom_embed(
                self.client, title = "Battle phase", colour = 0x009dff, thumb = player.avatar
            ).setup_embed()

            team_a = self.team_a_
            team_b = self.team_b_
        
        else:
            player = self.player_b
            circle = ":red_circle:"
            _circle = ":blue_circle:"

            embed = await Custom_embed(
                self.client, title = "Battle phase", colour = 0xff0000, thumb = player.avatar
            ).setup_embed()

            team_a = self.team_b_
            team_b = self.team_a_

        if(turn == 1):
            if(self.move.index == 0):
                display = await move.skip_move()
            
            elif(self.move.index == 2):
                display = await move.defense_move()

                await fighter.posture.change_posture("defending")

        else:
            # Ability
            await fighter.posture.change_posture("attacking")

            ability = await fighter.get_ability(
                self.client,
                self.ctx,
                fighter,
                self.move.target,
                team_a,
                team_b,
                self.move.index
            )

            display = await ability.use()

            fighter.ki.current -= ability.cost
            await fighter.ki.ki_limit()
            
        # display
        if(self.move.target == None):
            field_name = f"{circle}{fighter.image.icon}**{fighter.info.name}**{fighter.type.icon}'s move to **Himself** :"
        
        else:
            field_name = f"{circle}{fighter.image.icon}**{fighter.info.name}**{fighter.type.icon}'s move to {_circle}{self.move.target.image.icon}**{self.move.target.info.name}**{self.move.target.type.icon} :"

        embed.add_field(
            name = field_name,
            value = display,
            inline = False
        )

        await self.ctx.send(embed = embed)

        return
    
    async def effects(self, team, leader, start = False, end = False):
        """
        `coroutine`
        
        Triggers all the effects of passed `team`

        - Parameter 

        `team` (`list` of `Character()`)

        `leader` (`Character()`) : Leader of the team

        `start/end` (`bool`) : Tells if the effect are on turn starts or on turn ends

        --

        Return : `None`
        """

        # trigger all the malus and bonus effects
        # at the end of the turn and trigger on end
        # passive skills
        if(end):  
            for character in team:
                await asyncio.sleep(0)

                # bonus
                for bonus in character.bonus:
                    await asyncio.sleep(0)

                    if(bonus.duration > 0):  # check if the bonus is still available
                        await bonus.apply()

                        if not bonus.is_permanent:  # if it's not infinite
                            bonus.duration -= 1
                    
                    else:
                        character.bonus.remove(bonus)
                        await bonus.on_remove()  # triggers the on_remove effect
                
                # malus
                for malus in character.malus:
                    await asyncio.sleep(0)

                    if(malus.duration > 0):
                        await malus.apply()

                        if not malus.is_permanent:
                            malus.duration -= 1

                    else:
                        character.malus.remove(malus)
                        await malus.on_remove()

                # ki gain
                character.ki.current += character.regeneration.ki
                await character.ki.ki_limit()

        for char in team:
            await asyncio.sleep(0)

            # Make start passive callable 
            # if they're not callable yet
            new_passive_start_list, new_passive_end_list = [], []
            new_leader_list = []
            
            # get the passive effect
            if not char.passive_sorted:
                for passive in char.passive_start:
                    await asyncio.sleep(0)

                    passive = passive(
                        self.client,
                        self.ctx,
                        char,
                        self.team_a,
                        self.team_b
                    )

                    new_passive_start_list.append(passive)
                
                # replace the objects to make them callable
                char.passive_start = new_passive_start_list
                
                # make the passive end callable
                for passive_ in char.passive_end:
                    await asyncio

                    passive_ = passive_(
                        self.client,
                        self.ctx,
                        char,
                        self.team_a,
                        self.team_b
                    )

                    new_passive_end_list.append(passive_)
                
                # replace
                char.passive_end = new_passive_end_list
                char.passive_sorted = True
            
            # get callable leader
            if not char.leader_sorted:
                for lead in char.leader:
                    await asyncio.sleep(0)

                    lead = lead(
                        self.client,
                        self.ctx,
                        char,
                        self.team_a,
                        self.team_b
                    )

                    new_leader_list.append(lead)
                
                # replace the non callable list
                # by the callable one
                char.leader = new_leader_list
                char.leader_sorted = True
        
            await char.trigger_passive(start = start, end = end)

        if(leader.health.current > 0):
            await leader.trigger_leader()
            
        return
    
    async def trigger_leader(self, client, ctx, character_leader):
        """
        `coroutine`

        Trigger the leader skill of the passed character.

        --

        Return : None
        """

        # first sort the leader
        if(character_leader.health.current > 0):
            new_leader = []
            if(character_leader.leader_sorted == False):
                for leader in character_leader.leader:
                    await asyncio.sleep(0)

                    leader = leader(
                        client,
                        ctx,
                        character_leader,
                        self.team_a,
                        self.team_b
                    )

                    new_leader.append(leader)
                
                character_leader.leader = new_leader
                character_leader.leader_sorted = True

            # trigger all the leader if they've not been triggered 
            for _leader in character_leader.leader:
                await asyncio.sleep(0)

                if not _leader.triggered :
                    await _leader.apply()

        return
    
    async def reset_stat(self, team):
        """
        `coroutine`

        Reset the stats of the team

        --

        Return : `None`
        """

        character_getter = Character_getter()

        for char_a in team:
            await asyncio.sleep(0)

            # get the reference
            char_a_ref = await character_getter.get_character(char_a.info.id)

            # set the same stat as the char_a
            char_a_ref.level = char_a.level
            char_a_ref.rarity.value = char_a.rarity.value
            char_a_ref.enhancement = char_a.enhancement
            await char_a_ref.init()

                # health
            char_a.health.maximum = char_a_ref.health.maximum

                # damage
            char_a.damage.physical_max = char_a_ref.damage.physical_max
            char_a.damage.physical_min = char_a_ref.damage.physical_min

            char_a.damage.ki_max = char_a_ref.damage.ki_max
            char_a.damage.ki_min = char_a_ref.damage.ki_min

                # defense
            char_a.defense.armor = char_a_ref.defense.armor
            char_a.defense.spirit = char_a_ref.defense.spirit
            char_a.defense.dodge = char_a_ref.defense.dodge

                # bonus
            char_a.critical_chance = char_a_ref.critical_chance
            char_a.critical_bonus = char_a_ref.critical_bonus
            char_a.regeneration.health = char_a_ref.regeneration.health
            char_a.regeneration.ki = char_a_ref.regeneration.ki

        return
        
    async def player_turn(self, player, order, turn):
        """
        `coroutine`

        Gets thes input and throw the outputs for the current player

        - Parameter

        `player` (`Player()`)

        `order` (`int`) : Tells who's playing

        `turn` (`int`)

        --

        Return : `Character()`
        """

        # init
        _input = Combat_input(self.client)

        # set the first turn actions
        if(turn == 1):
            fighter_action = "`1.` :arrow_right: **Skip**\n`3.` :shield: **Defend**\n"
        
        else:
            fighter_action = ""

        # get the fighter
        playable = await self.get_player_fighter(order)  # get a list of playable character this turn
        possible_fighter = await _input.get_possible(playable, self.team_a_, self.team_b_)  # get possible inputs

        # add the flee input
        possible_fighter.append("flee")

        fighter_ok = False

        while not fighter_ok:
            await asyncio.sleep(0)

            # get the team order
            if(order == 0):
                player = self.player_a
                team_a = self.team_a
                team_a_ = self.team_a_
                team_b = self.team_b
                team_b_ = self.team_b_
                circle = ":blue_circle:"
            
            else:
                player = self.player_b
                team_a = self.team_b
                team_a_ = self.team_b_
                team_b = self.team_a
                team_b_ = self.team_a_
                circle = ":red_circle:"

            # if the player is a real player
            if not player.is_cpu:
                await self.ctx.send(f"Please {circle}**{player.name}** select a fighter : Type its **index** number.\nYou can type, for example : `2` | `flee` | `check 3`")
                player_input = await _input.wait_for_input(possible_fighter, player)  # get the player choice
                player_input = player_input.split()
            
            else:  # the player is played by a CPU, get an automatic selection
                player_input = await player.pick_fighter()

                fighter_ok = True

            # special input
            if(player_input[0].lower() == "flee"):
                return(0)
            
            elif(player_input[0].lower() == "check"):
                if(len(player_input) > 1):
                    await self.check_character(int(player_input[1]), order)

            # normal input
            elif(player_input != None):
                player_input = int(player_input[0]) - 1

                player_fighter = playable[player_input]  # get the selected fighter

                if(player_fighter.health.current > 0 and player_fighter.posture.stunned == False):
                    fighter_ok = True
                
                else:
                    await self.ctx.send("Please select a fighter that is not :skull:**K.O** or **Stunned**")
            
        # wait for an action
        if(turn > 1):
            action_index = 1
            ability_index = 0

            # abilities
            # set the display
            for action in player_fighter.ability:
                await asyncio.sleep(0)

                # get each ability for the display
                ability = await player_fighter.get_ability(
                    self.client, self.ctx, player_fighter, player_fighter, 
                    team_a, team_b, ability_index
                )

                await ability.set_tooltip()

                # if the ability is available
                if(ability.cooldown <= 0 and player_fighter.ki.current >= ability.cost):
                    fighter_action += f"`{action_index}`. {ability.icon}**{ability.name}** - ({player_fighter.ki.current} / {ability.cost}:fire:) : {ability.tooltip}"
                
                else:  # if the ability is on cooldown or not enough ki
                    if(ability.cooldown > 0):
                        # add the hourglass to the display
                        cooldown = f"**Cooldown :** {ability.cooldown:,}:hourglass: - "
                        fighter_action += cooldown

                    # show the ability as unavailable
                    # don't show the tooltip
                    fighter_action += f"~~`{action_index}`. {ability.icon}**{ability.name}** - ({player_fighter.ki.current} / {ability.cost}:fire:)~~"

                fighter_action += "\n"

                action_index += 1
                ability_index += 1
        
        if not player.is_cpu:
            await self.ctx.send(
                f"Please select an action for {player_fighter.image.icon}**{player_fighter.info.name}** *({player_fighter.ki.current}:fire:)* :\n{fighter_action}"
            )

        # get the move
        possible_move = []
        fighter_ability = []

        # get the possible ability
        for i in range(len(player_fighter.ability)):
            await asyncio.sleep(0)

            ability = await player_fighter.get_ability(
                self.client, self.ctx, player_fighter, player_fighter, 
                team_a, team_b, i
            )

            if(ability.cooldown <= 0):  # not on cooldown
                if(ability.cost <= player_fighter.ki.current):
                    fighter_ability.append(ability)

        # normal turn
        if(turn > 1):
            # get the possible move for the player
            possible_move = await _input.get_possible(fighter_ability, self.team_a_, self.team_b_, ability = True)

        else:  # setup turn
            possible_move.append("1")
            possible_move.append("3")
        
        possible_move.append("flee")

        action_ok = False

        while not action_ok:
            await asyncio.sleep(0)

            # get the player's choice
            if not player.is_cpu:
                player_move = await _input.wait_for_input(possible_move, player)
                player_move = player_move.split()

            else:
                player_move = "cpu"

            # special move
            if(player_move[0].lower() == "flee"):
                return(0)

            elif(player_move[0].lower() == "check"):
                if(len(player_move) > 1):
                    await self.check_character(int(player_move[1]), order)
            
            elif(player_move[0] != "flee"):
                if not player.is_cpu:
                    player_move = int(player_move[0]) - 1

                    # initial move
                    if(turn == 1):
                        # skip
                        if(player_move == 0):
                            self.move.index = 0

                            action_ok = True
                        
                        # defend
                        elif(player_move == 2):
                            self.move.index = 2

                            action_ok = True

                    # normal move
                    else:
                        self.move.index = player_move

                        ability = await player_fighter.get_ability(
                            self.client, self.ctx, player_fighter, player_fighter, 
                            team_a, team_b, player_move
                        )
                        
                        # check the cost
                        if(player_fighter.ki.current >= ability.cost):
                            if(ability.need_target):
                                self.move.target = await self.get_target(
                                    player, team_a_, team_b_, order,
                                    target_ally = ability.target_ally,
                                    target_enemy = ability.target_enemy,
                                    ignore_defenders = ability.ignore_defenders
                                ) 

                                action_ok = True
                            
                            else:  # if don't need target just pass
                                action_ok = True
                        
                        else:
                            await self.ctx.send("You do not have enough **Ki** to use this ability")
                        
                else:  # cpu
                    self.move = await player.make_move(
                    player_fighter, self.move, self.client, self.ctx,
                    team_a_, team_b_, turn
                    )

                    action_ok = True
                        
        # execute the action
        await self.battle(player_fighter, order, turn)
          
        return(player_fighter)
    
    async def get_winner(self):
        """
        `coroutine`

        Check the win condition and return the player who won the game

        --

        Return : `Player()` or `None` if not found and `0` in case of draw
        """

        # init
        winner, loser = None, None
        draw = False
        circle, _circle = "", ""

        health_a, health_b = 0, 0

        # check the healf of the team_a
        # we iterate the copy
        for char_a in self.team_a_:  
            await asyncio.sleep(0)

            health_a += char_a.health.current
        
        # check the health of the team_b
        for char_b in self.team_b_:
            await asyncio.sleep(0)

            health_b += char_b.health.current
        
        # check the winner
        if(health_a <= 0):
            winner = self.player_b
            loser = self.player_a
            circle = ":red_circle:"
            _circle = ":blue_circle:"
        
        if(health_b <= 0):
            winner = self.player_a
            loser = self.player_b
            circle = ":blue_circle:"
            _circle = ":red_circle:"
        
        if(loser != None):
            # check draw
            if(health_a <= 0 and health_b <= 0):
                winner = 0

                await self.ctx.send(f":blue_circle:{self.player_a.name} VS :red_circle:{self.player_b.name} : **DRAW** !")
            
            # winner
            if not draw:
                await self.ctx.send(f"{circle}**{winner.name}** has won the fight against {_circle}**{loser.name}** !")

        return(winner)
    
    async def turn(self, order, _turn):
        """
        `coroutine`

        Run the player's turn

        - Parameter

        `order` (`int`)

        `_turn` (`int`)

        --

        Return : `Player()` if there is a winner, else `None`
        """

        # init
        self.move.target = None

        if(order == 0):
            player = self.player_a
            removed = self.removed_a
            team = self.team_a
        
        else:
            player = self.player_b
            removed = self.removed_b
            team = self.team_b

        # player turn
        character_used = await self.player_turn(player, order, _turn)

        if(character_used == 0):
            return(0)

        character_used.played = True

        removed.append(character_used)
        team.remove(character_used)

        winner = await self.get_winner()

        if(winner != None):
            return(winner)

        return
    
    async def get_play_time(self, order):
        """
        `coroutine`

        Update the teams to know how many times the player has to play
        
        - Parameter

        `order` (`int`)

        --

        Return : `int`
        """

        # init
        play_time = 0
        unplayable = []

        if(order == 0):
            team = self.team_a
        
        else:
            team = self.team_b

        for char in team:
            await asyncio.sleep(0)

            if(char.health.current <= 0 or char.posture.stunned):
                unplayable.append(char)
        
        for char_ in unplayable:
            await asyncio.sleep(0)

            team.remove(char_)
        
        play_time = len(team)

        return(play_time)
    
    async def check_character(self, index, order):
        """
        `coroutine`

        Displays informations about a character in the combat

        --

        Return : `None`
        """

        # init
        characters = self.team_a_ + self.team_b_
        posture_icon = [":crossed_swords:", ":fire:", ":shield:", ":confused:"]
        getter = Character_getter()

        if(index > len(characters)):
            return

        if(order == 0):
            color = 0x009dff
        
        else:
            color = 0xff0000
        
        character = characters[index - 1]
        reference = await getter.get_character(character.info.id)

        # init ref character
        reference.level = character.level
        reference.rarity.value = character.rarity.value

        await reference.init()

        # comparison
        comparison_hp = character.health.maximum - reference.health.maximum

        comparison_phy = character.damage.physical_max - reference.damage.physical_max
        comparison_ki = character.damage.ki_max - reference.damage.ki_max

        comparison_armor = character.defense.armor - reference.defense.armor
        comparison_spirit = character.defense.spirit - reference.defense.spirit

        # posture
        posture = None

        if(character.posture.attacking == True):
            posture = posture_icon[0]
        
        if(character.posture.charging == True):
            posture = posture_icon[1]

        if(character.posture.defending == True):
            posture = posture_icon[2]
        
        if(character.posture.stunned == True):
            posture = posture_icon[3]
        
        # formatting the embed
        combat_format = f"__Health__ : **{character.health.current:,}** / **{character.health.maximum:,}**:hearts:"
        if(comparison_hp != 0): 
            if(comparison_hp > 0):
                combat_format += f" *(+ {comparison_hp:,})*"
            
            else:
                combat_format += f" *({comparison_hp:,})*"

        combat_format += f"\n__Posture__ : {posture}"
        combat_format += f"\n__Damage__ :\n:punch: **{character.damage.physical_min:,}** - **{character.damage.physical_max:,}**"
        if(comparison_phy != 0):
            if(comparison_phy > 0):
                combat_format += f" *(+{comparison_phy:,})*"
            
            else:
                combat_format += f" *({comparison_phy:,})*"

        combat_format += f"\n{game_icon['ki_ability']} **{character.damage.ki_min:,}** - **{character.damage.ki_max:,}**"
        if(comparison_ki != 0):
            if(comparison_ki > 0):
                combat_format += f" *(+{comparison_ki:,})*"
            
            else:
                combat_format += f" *({comparison_ki:,})*"

        combat_format += f"\n__Defense__ :\n:shield: **{character.defense.armor:,}**"
        if(comparison_armor != 0):
            if(comparison_armor > 0):
                combat_format += f" *(+{comparison_armor:,})*"

            else:
                combat_format += f" *({comparison_armor:,})*"
        
        combat_format += f"\n:rosette: **{character.defense.spirit:,}**"
        if(comparison_spirit != 0):
            if(comparison_spirit > 0):
                combat_format += f" *(+{comparison_spirit:,})*"
            
            else:
                combat_format += f" *({comparison_spirit:,})*"

        combat_format += f"\n__Ki__ : **{character.ki.current}** :fire:"

        # now the effects
            # buff
        if(len(character.bonus) > 0):  # if the character has a buff
            combat_format += f"\n__Bonus__ : "

            for buff in character.bonus:
                await asyncio.sleep(0)

                if(buff.is_permanent):
                    combat_format += f"{buff.icon}[{buff.stack}|*∞*]"    
                
                else:
                    combat_format += f"{buff.icon}[{buff.stack}|{buff.duration}]"
        
        if(len(character.malus) > 0):
            combat_format += f"\n__Malus__ : "
            
            for debuff in character.malus:
                await asyncio.sleep(0)

                combat_format += f"{debuff.icon}[{debuff.stack}|{debuff.duration}]"

        embed = await Custom_embed(
            self.client, title = "Character infos", colour = color, thumb = character.image.thumb
        ).setup_embed()

        embed.add_field(
            name = f"{character.image.icon}{character.info.name} {character.type.icon}{character.rarity.icon}'s infos :",
            value = combat_format
        )

        await self.ctx.send(embed = embed)

        return

    # combat
    async def run(self):
        """
        `coroutine`

        Run the combat

        --

        Return : `Player()` or `None` if one of the players has fled
        """ 

        # init
        await self.get_play_order()  # defines which player plays first
        self.team_a, self.team_b = await self.get_teams()  # set the players team
        
        winner = None  # store the Player() who won the fight
        combat_end = False
        turn = 1

        # start the fight
        await self.ctx.send(f":blue_circle:**{self.player_a.name}** VS :red_circle:**{self.player_b.name}**")
        await asyncio.sleep(1)

        # get the team leader of each player 
        leader_a = self.team_a[0]  
        leader_b = self.team_b[0]

        while not combat_end:
            await asyncio.sleep(0)

            turn_end = False

            await self.ctx.send(f"📣 Round {turn} 📣")
            await asyncio.sleep(1)

            # if it's the first turn, displays differently
            if(turn == 1):
                await self.display_teams()
                await asyncio.sleep(1)
            
            while not turn_end:
                await asyncio.sleep(0)

                # trigger the on_turn_start effects
                await self.effects(self.team_a, self.leader_a, start = True)
                await self.effects(self.team_b, self.leader_b, start = True)
                
                winner = await self.get_winner()

                if(winner != None):
                    return(winner)

                # get the number of time a player will play this turn
                play_time = await self.get_play_time(0)

                for a in range(play_time):
                    # if there is only one char left
                    # check if the char can play
                    winner = await self.turn(0, turn)

                    if(winner == 0):
                        await self.ctx.send(f":blue_circle:**{self.player_a.name}** has fled the combat")
                        return

                    if(winner != None):
                        return(winner)

                play_time = await self.get_play_time(1)
   
                for b in range(play_time):
                    # if there is only one char left
                    # check if the char can play
                    winner = await self.turn(1, turn)

                    if(winner == 0):
                        await self.ctx.send(f":red_circle:**{self.player_a.name}** has fled the combat")
                        return

                    if(winner != None):
                        return(winner)    

                # END OF TURN
                if(len(self.team_a) <= 0 and len(self.team_b) <= 0):
                    for char_a in self.team_a_:
                        await asyncio.sleep(0)

                        char_a.played = False

                        self.team_a.append(char_a)
                    
                    for char_b in self.team_b_:
                        await asyncio.sleep(0)

                        char_b.played = False

                        self.team_b.append(char_b)
                        
                    self.removed_a = []
                    self.removed_b = []
                    
                    # reset stats before applying effects
                    await self.reset_stat(self.team_a)
                    await self.reset_stat(self.team_b)
                    
                    # effect
                    await self.trigger_leader(self.client, self.ctx, leader_a)
                    await self.trigger_leader(self.client, self.ctx, leader_b)

                    await self.effects(self.team_a, self.leader_a, end = True)
                    await self.effects(self.team_b, self.leader_b, end = True)

                    winner = await self.get_winner()

                    if(winner != None):
                        return(winner)

                    turn_end = True
            
            turn += 1

        return