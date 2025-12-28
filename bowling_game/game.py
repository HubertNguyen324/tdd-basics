class BowlingGame:
    def __init__(self) -> None:
        self._rolls: list[int] = []

    def _two_ball_in_frame_score(self, first_in_frame: int) -> int:
        return self._rolls[first_in_frame] + self._rolls[first_in_frame + 1]

    def _spare_score(self, first_in_frame: int) -> int:
        return 10 + self._rolls[first_in_frame + 2]

    def _stike_score(self, first_in_frame: int) -> int:
        return 10 + self._rolls[first_in_frame + 1] + self._rolls[first_in_frame + 2]

    def _is_strike(self, first_in_frame: int) -> bool:
        return self._rolls[first_in_frame] == 10

    def _is_spare(self, first_in_frame: int) -> bool:
        return self._rolls[first_in_frame] + self._rolls[first_in_frame + 1] == 10

    def roll(self, pins: int = 0) -> None:
        self._rolls.append(pins)

    def score(self) -> int:
        score = 0
        first_in_frame = 0
        for frame in range(10):
            if self._is_strike(first_in_frame):
                score += self._stike_score(first_in_frame)
                first_in_frame += 1
            elif self._is_spare(first_in_frame):
                score += self._spare_score(first_in_frame)
                first_in_frame += 2
            else:
                score += self._two_ball_in_frame_score(first_in_frame)
                first_in_frame += 2

        return score
