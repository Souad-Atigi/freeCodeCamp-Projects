from typing import Literal
from random import choice
from collections import Counter

Hand = Literal["R", "P", "S", ""]

def player(prev_play: Hand, opponent_history: list[Hand] = [], player_history: list[Hand] = []) -> Hand:
    if not prev_play:
        opponent_history.clear()
        player_history.clear()

    opponent_history.append(prev_play)

    if len(opponent_history) <= 1:
        guess = choice(["R", "P", "S"])
    else:
        # Analyze patterns of length 1 to 5
        pattern_length = min(5, len(opponent_history) - 1)
        while pattern_length > 0:
            pattern = "".join(opponent_history[-pattern_length:])
            if pattern in "".join(opponent_history[:-pattern_length]):
                next_move_index = "".join(opponent_history[:-pattern_length]).rindex(pattern) + pattern_length
                if next_move_index < len(opponent_history):
                    prediction = opponent_history[next_move_index]
                    guess = oppose(prediction)
                    break
            pattern_length -= 1
        else:
            # If no pattern found, use frequency analysis
            freq = Counter(opponent_history[-10:])
            most_common = freq.most_common(1)[0][0] if freq else ""
            guess = oppose(most_common)

    player_history.append(guess)
    return guess

def oppose(hand: Hand) -> Hand:
    if hand == "P":
        return "S"
    elif hand == "R":
        return "P"
    elif hand == "S":
        return "R"
    return choice(["R", "P", "S"])