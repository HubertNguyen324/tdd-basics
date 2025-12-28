import pytest

from .game import BowlingGame


@pytest.fixture
def game() -> BowlingGame:
    return BowlingGame()


def _roll_many(game: BowlingGame, pins: int, rolls: int) -> None:
    for _ in range(rolls):
        game.roll(pins)


def _roll_spare(game: BowlingGame):
    game.roll(5)
    game.roll(5)


def _roll_strike(game: BowlingGame):
    game.roll(10)


def test_instantiation(game: BowlingGame):
    assert game is not None
    assert isinstance(game, BowlingGame)


def test_guttergame_score(game: BowlingGame):
    _roll_many(game=game, pins=0, rolls=20)
    assert game.score() == 0


def test_all_onesgame_score(game: BowlingGame):
    _roll_many(game=game, pins=1, rolls=20)
    assert game.score() == 20


def test_one_spare(game: BowlingGame):
    _roll_spare(game)
    game.roll(3)
    _roll_many(game=game, pins=0, rolls=17)
    assert game.score() == 16


def test_one_strike(game: BowlingGame):
    _roll_strike(game)
    game.roll(3)
    game.roll(4)
    _roll_many(game=game, pins=0, rolls=16)
    assert game.score() == 24


def test_perfect_game(game: BowlingGame):
    _roll_many(game, 10, 12)
    assert game.score() == 300
