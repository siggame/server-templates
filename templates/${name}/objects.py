import game_objects
from .game import Game

% for model in models:
class ${model.name}(Game.Object):
    game_state_attributes = set([${', '.join([repr(i.name) for i in model.data])}])
% endfor
