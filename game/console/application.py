from logging import getLogger

from ..application import Application
from ..game import Player

from .game import ConsoleGame


logger = getLogger(__name__)


class ConsoleApplication(Application):
    game_class = ConsoleGame

    def run(self, *args, **kwargs):
        logger.info("Starting Console Application")
        try:
            while True:
                self.loop()
                input("Press any key to play again. Ctrl + C to exit")
        except KeyboardInterrupt:
            logger.info("Interrupted by Keyboard")
        print("Hope you enjoyed your match!")

    def loop(self):
        result = self.game.game_loop()
        if result.winner == Player.TIE:
            logger.info("Result is TIE")
            print(f"We have a TIE with {result.tie_points} points")
        else:
            logger.info(f"Winner is {result.winner}")
            print(f"Winner is {result.winner.value} with {result.winner_points} points")
            print(f"{result.looser.value} loose with {result.looser_points} points")

