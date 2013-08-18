import game_objects
from .game import Game
from  util import command
from game_utils import takes, success, failure

% for model in models:
class ${model.name}(Game.Object):
    _game_state_attributes = ${repr(
        [i.name for i in model.locals] + [i.name + '_id' for i in model.relations]
        )}
    _relations = ${repr(
        {i.name: i.type.name for i in model.relations}
        )}
    _remotes = ${repr(
        {i.name: i.through for i in model.remotes}
        )}

    def before_turn(self):
        #TODO: Fill in start of turn values
        #Common example would be giving units moves before their turn
        pass

    def after_turn(self):
        #TODO: Set post-turn values
        #Common example would be zeroing unit moves after the turn
        pass

%   for func in model.functions:
    @command
    @takes(\
%     for num, arg in enumerate(func.arguments):
${', ' if num else ''}${arg.name} = ${type_for(arg)}\
%     endfor
)
    def ${func.name}(self\
%     for arg in func.arguments:
, ${arg.name} = None\
%     endfor
):
%     if model.parent and func in model.parent.functions:
        ${model.parent.name}.${func.name}(self\
%       for arg in func.arguments:
, ${arg.name} = ${arg.name}\
%       endfor
)
%     else:
        pass
%     endif

%    endfor

% endfor
