import game_objects
from .game import Game
from  util import command
from game_utils import takes, success, failure

% for model in models:
class ${model.name}(Game.Object):
    game_state_attributes = ${repr(
        [i.name for i in model.data]
        )}

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
