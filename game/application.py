
from game.game import Game


class Application:
    game_class: type(Game)

    def __init__(self):
        self.game = self.game_class()

    def run(self, *args, **kwargs):
        raise NotImplementedError()

    def parse_arguments(self, *args, **kwargs):
        pass
