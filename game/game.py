from enum import Enum
from logging import getLogger
from random import choice as random_choice


# Logger
logger = getLogger(__name__)

# Default number of round to play if not provided
_DEFAULT_MAX_ROUNDS = 5


# Rock, Paper, Scissor
class RPS(Enum):
    ROCK = 'rock'
    PAPER = 'paper'
    SCISSOR = 'scissor'


# RPS Values as List of String to use with `random.choice`
CHOICES = [v.value for v in RPS]

# Values Weights to determine Winner
WEIGHTS = {
    RPS.ROCK: 1,
    RPS.PAPER: 2,
    RPS.SCISSOR: 3,
}


# Winner
class Player(Enum):
    USER = 'user'
    COMPUTER = 'computer'
    TIE = 'tie'


class Status:
    player_points: int  # Points Scored by Player
    computer_points: int  # Points Scored by Computer
    tie_points: int  # Ties

    def __init__(self):
        self.player_points = 0
        self.computer_points = 0
        self.tie_points = 0

    @property
    def winner(self) -> Player:
        if self.player_points > self.computer_points:
            return Player.USER
        elif self.player_points < self.computer_points:
            return Player.COMPUTER
        else:
            return Player.TIE

    @property
    def winner_points(self) -> int:
        if self.winner == Player.USER:
            return self.player_points
        elif self.winner == Player.COMPUTER:
            return self.computer_points
        else:
            return self.tie_points

    @property
    def looser(self) -> Player:
        if self.winner == Player.USER:
            return Player.COMPUTER
        elif self.winner == Player.COMPUTER:
            return Player.USER
        else:
            return Player.TIE

    @property
    def looser_points(self) -> int:
        if self.looser == Player.USER:
            return self.player_points
        elif self.looser == Player.COMPUTER:
            return self.computer_points
        else:
            return self.tie_points


class Game:
    status: Status

    max_rounds: int  # Best of N rounds
    actual_round: int  # Running round

    def __init__(self, max_rounds: int = None):
        if not max_rounds:
            max_rounds = _DEFAULT_MAX_ROUNDS
        self.max_rounds = max_rounds
        self.actual_round = 0

        self.status = Status()

    @property
    def finished(self):
        return self.actual_round >= self.max_rounds

    def game_loop(self) -> Status:
        logger.info("Game Started")
        while not self.finished:
            self.start_round()
            self.update()
        logger.info("Game Finish")
        return self.status

    def update(self):
        raise NotImplementedError()

    def start_round(self) -> None:
        logger.info("New Round Started")
        self.actual_round += 1
        logger.debug("Getting Player Input")
        player_choice = self.get_user_choice()
        logger.debug("Getting Actual Round Winner")
        winner = self.get_winner(player_choice)
        logger.debug("Checking Winner")
        if winner == Player.USER:
            logger.info("Player won this round")
            self.status.player_points += 1
        elif winner == Player.COMPUTER:
            logger.info("Computer won this round")
            self.status.computer_points += 1
        else:
            logger.info("Tie Round")
            self.status.tie_points += 1

    def get_winner(self, player_choice: RPS, computer_choice: RPS = None) -> Player:
        if not computer_choice:
            computer_choice = self.get_random_choice()
        if WEIGHTS[player_choice] == WEIGHTS[computer_choice] + 1 or \
                (WEIGHTS[player_choice] == 3 and WEIGHTS[computer_choice] == 1):
            return Player.USER
        elif WEIGHTS[player_choice] == WEIGHTS[computer_choice]:
            return Player.TIE
        else:
            return Player.COMPUTER

    @staticmethod
    def get_random_choice() -> RPS:
        logger.debug("Getting a Random Computer Choice")
        choice = random_choice(CHOICES)
        return RPS(choice)

    def get_user_choice(self) -> RPS:
        player_input = self.get_user_input()
        player_choice = self.process_user_input(player_input)
        return player_choice

    @staticmethod
    def get_user_input():
        raise NotImplementedError()

    def process_user_input(self, user_input) -> RPS:
        raise NotImplementedError()

