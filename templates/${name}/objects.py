import game_objects
from .game import ${capitalize(name)}

% for model in models:
class ${model.name}(game_objects.GameObject):
    pass
% endfor
