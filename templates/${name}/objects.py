import game_objects
from .game import Game
from  util import command

% for model in models:
class ${model.name}(Game.Object):
    game_state_attributes = ${repr(
        [i.name for i in model.data]
        )}

%   for func in model.functions:
    @command
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
