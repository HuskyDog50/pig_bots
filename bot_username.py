def choice(round_score, my_score, opponent_score):
    if my_score + round_score >= 100:
        return False
    if my_score <= 20:
        if opponent_score >= my_score + round_score:
            return False
        return True
    if return scores[0] > scores[1] + score or score < 20:
        return False
