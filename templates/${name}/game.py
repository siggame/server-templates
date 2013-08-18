import game_objects
import objects

<% locals = [i for i in globals if not isinstance(i.type, Model)] %>
<% relations = [i for i in globals if isinstance(i.type, Model)] %>

class Game(game_objects.Game):
    _name = ${repr(name)}
    _game_version = ${version}
    _server_version = 1
    _globals = ${repr(
        [i.name for i in locals] + [i.name  + '_id' for i in relations]
        )}
    _relations = ${repr(
        {i.name: i.type.name for i in relations}
        )}

    def before_start(self):
        #TODO: Initialize the game

        #Create any objects that should exist at the start (Tiles, for example)
        #Initialize any global values
        #At this point Player objects exist
        #(But any game-specific values will be uninitialized)
        config = self.load_config('defaults')
        self.game_length = config['globals']['game_length']

    def before_turn(self):
        #TODO: Initialize the turn
        #turn_number and current_player will be valued for the coming turn

        #Common operations include:
        #Setting current player's units to ready to move/attack
        #Start of turn income
        #Creating units whose construction began previously
        pass

    def after_turn(self):
        #TODO: Clean up any values at the end of a turn
        #turn_number and current_player will be valued for the past turn
        #This is called before check_winner, so this is a good place for any
        #Score calculation

        #Common operations include:
        #Setting all units to no moves_left/attacks_left
        #Any end of turn costs/damage
        pass

    def check_winner(self):
        #TODO: Calculate if anyone has won and return the winner and reason
        if self.turn_number >= self.game_length:
            return self.players[0], 'won due to tie'
        else:
            return None, 'the battle continues'
