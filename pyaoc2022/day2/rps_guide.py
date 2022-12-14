from pathlib import Path
from typing import Callable



def read_guide(path: Path) -> list[tuple[str, str]]:
    with open(path, "r") as f:
        return [tuple(line.strip().split()) for line in f.readlines()]


def compute_move_score(move: tuple[str, str]) -> int:
    """
    Score function that treats the move pair values as the move being played by the opponent and by the player.
    First value in the tuple is the opponent's move: A - rock; B - paper; C - scissors
    Second value in the tuple is the player's move: X - rock; Y - paper; Z - scissors

    Player's score is calculated based on the value of the move (1 for rock; 2 for paper; 3 for scissors).
    In addition to the move value we add 0 for a loss, 3 for a draw, 6 for a win.
    """
    score = 0

    match move:
        case ("A", x):
            match x:
                case "X":
                    score += 1 + 3
                case "Y":
                    score += 2 + 6
                case "Z":
                    score += 3 + 0
                case _:
                    print(f"Invalid move: {move}")
        case ("B", x):
            match x:
                case "X":
                    score += 1 + 0
                case "Y":
                    score += 2 + 3
                case "Z":
                    score += 3 + 6
                case _:
                    print(f"Invalid move: {move}")
        case ("C", x):
            match x:
                case "X":
                    score += 1 + 6
                case "Y":
                    score += 2 + 0
                case "Z":
                    score += 3 + 3
                case _:
                    print(f"Invalid move: {move}")
        case _:
            print(f"Invalid move: {move}")

    return score


def compute_prediction_score(move: tuple[str, str]) -> int:
    """
    Score function that treats the move pair values as the move being played by the opponent and the outcome for the player.
    First value in the tuple is the opponent's move: A - rock; B - paper; C - scissors
    Second value in the tuple is the player's outcome: X - loss; Y - draw; Z - win

    Player's score is calculated based on the value of the move (1 for rock; 2 for paper; 3 for scissors).
    Player's move needs to be inferred based on the opponent's move and the player's desired outcome.
    In addition to the move value we add 0 for a loss, 3 for a draw, 6 for a win.
    """
    score = 0

    match move:
        case ("A", x):
            match x:
                case "X":
                    score += 3 + 0
                case "Y":
                    score += 1 + 3
                case "Z":
                    score += 2 + 6
                case _:
                    print(f"Invalid move: {move}")
        case ("B", x):
            match x:
                case "X":
                    score += 1 + 0
                case "Y":
                    score += 2 + 3
                case "Z":
                    score += 3 + 6
                case _:
                    print(f"Invalid move: {move}")
        case ("C", x):
            match x:
                case "X":
                    score += 2 + 0
                case "Y":
                    score += 3 + 3
                case "Z":
                    score += 1 + 6
                case _:
                    print(f"Invalid move: {move}")
        case _:
            print(f"Invalid move: {move}")

    return score


def compute_guide_score(raw_guide: list[list[str]], move_score_fn: Callable[[tuple[str, str]], int]) -> int:
    return sum([move_score_fn(move) for move in raw_guide])


if __name__ == "__main__":
    raw_guide = read_guide("guide.txt")

    # Challenge 1: Compute the total score for the given guide
    # Inputs represent the moves played by the opponent and the player
    challenge_1_score = compute_guide_score(raw_guide, move_score_fn=compute_move_score)
    print(f"Challenge 1 score for the given guide is: {challenge_1_score}")

    # Challenge 2: Compute the total score for the given guide
    # Inputs represent the moves played by the opponent and the outcome for the player
    challenge_2_score = compute_guide_score(raw_guide, move_score_fn=compute_prediction_score)
    print(f"Challenge 2 score for the given guide is: {challenge_2_score}")
