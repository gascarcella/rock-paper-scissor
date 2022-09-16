from logging import getLogger

from ..game import Game, RPS

logger = getLogger(__name__)


class ConsoleGame(Game):
    def update(self):
        print(f"Player: {self.status.player_points}")
        print(f"Computer: {self.status.computer_points}")
        print(f"Tie: {self.status.tie_points}")

    @staticmethod
    def get_user_input():
        return input("Pick [R]ock,[P]apper,[S]cissor. Write R,P or S: ").lower()

    def process_user_input(self, user_input) -> RPS:
        input_map = {
            'r': RPS.ROCK,
            'p': RPS.PAPER,
            's': RPS.SCISSOR
        }
        return input_map[user_input]

    def get_user_choice(self) -> RPS:
        def get_choice() -> RPS | None:
            try:
                # We need to explicitly pass ConsoleGame class and self because we are outside scope
                _choice = super(ConsoleGame, self).get_user_choice()
                return _choice
            except KeyError:
                return None

        choice = None
        while not choice:
            choice = get_choice()
            if not choice:
                logger.error("Invalid User Input")
                print("Please pick a valid choice")
                continue
            return choice
