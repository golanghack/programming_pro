from pprint import pprint
import random
import math

TIMESTAMPS_COUNT = 50000

PROBABILITY_SCORE_CHANGED = 0.0001

PROBABILITY_HOME_SCORE = 0.45

OFFSET_MAX_STEP = 3

INITIAL_STAMP = {
    "offset": 0,
    "score": {
        "home": 0,
        "away": 0
    }
}

def main():
    game_stamps = generate_game()
    pprint(game_stamps)
    

def generate_stamp(previous_value):
    score_changed = random.random() > 1 - PROBABILITY_SCORE_CHANGED
    home_score_change = 1 if score_changed and random.random() > 1 - \
                             PROBABILITY_HOME_SCORE else 0
    away_score_change = 1 if score_changed and not home_score_change else 0
    offset_change = math.floor(random.random() * OFFSET_MAX_STEP) + 1

    return {
        "offset": previous_value["offset"] + offset_change,
        "score": {
            "home": previous_value["score"]["home"] + home_score_change,
            "away": previous_value["score"]["away"] + away_score_change
        }
    }


def generate_game():
    stamps = [INITIAL_STAMP, ]
    current_stamp = INITIAL_STAMP
    for _ in range(TIMESTAMPS_COUNT):
        current_stamp = generate_stamp(current_stamp)
        stamps.append(current_stamp)

    return stamps


def get_score(game_stamps, offset):
    """
        Takes list of game's stamps and time offset for which returns the scores for t
        he home and away teams.
        Please pay attention to that for some offsets the game_stamps list 
        may not contain scores.
    """
    if game_stamps[-1].get("offset") < offset:
        score = game_stamps[-1].get("score")
        home = score.get("home") if score else None
        away = score.get("away") if score else None
        if type(home) == int and type(away) == int:
            return home, away

    while offset >= 0:
        for stamp in game_stamps:
            if stamp.get("offset") == offset:
                score = stamp.get("score")
                try:
                    home = score.get("home") if score else None
                    away = score.get("away") if score else None
                    return home, away
                except ValueError as err:
                    print(err)
                    
        offset = offset - 1
    return 0, 0


if __name__ == "__main__":
   main()