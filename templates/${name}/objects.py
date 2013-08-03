import game_objects
from .game import Game

% for model in models:
class ${model.name}(Game.Object):
    game_state_attributes = ${repr(
        sorted([i.name for i in model.data])
        )}

%   for func in model.functions:
  def ${func.name}(self\
%     for arg in func.arguments:
, ${arg.name} = None\
%     endfor
):
    pass
%    endfor

% endfor
