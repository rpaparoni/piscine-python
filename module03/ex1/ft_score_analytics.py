import sys


def ft_score_analytics(scores: list) -> None:
    i: int = 0
    valid_scores: list = []
    while i < len(scores):
        try:
            valid_score: int = int(scores[i])
            valid_scores += [valid_score]
        except ValueError:
            print(f"Invalid parameter: '{scores[i]}'")
        i += 1
    if len(valid_scores) == 0:
        error: str = "No scores provided. Usage: python3 "
        error = error + "ft_score_analytics.py <score1> <score2> ..."
        raise ValueError(error)
    score_list: list = []
    k: int = 0
    while k < len(valid_scores):
        score_list.append(str(valid_scores[k]))
        k += 1
    scores_processed: str = (", ".join(score_list))
    print(f"Scores processed: [{scores_processed}]")

    total_players: int = len(score_list)
    print(f"Total players: {total_players}")

    total_score: int = 0
    j: int = 0

    while j < total_players:
        current_score: int = int(score_list[j])
        total_score += current_score
        j += 1
    print(f"Total score: {total_score}")

    average_score = total_score / total_players
    print(f"Average score: {average_score}")

    max_score: int = int(max(score_list))
    print(f"High score: {max_score}")

    min_score: int = int(min(score_list))
    print(f"Low score: {min_score}")

    score_range = max_score - min_score
    print(f"Score range: {score_range}")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")

    try:
        if len(sys.argv) > 1:
            scores: list = sys.argv[1:]
            ft_score_analytics(scores)
        else:
            error: str = "No scores provided. Usage: python3 "
            error = error + "ft_score_analytics.py <score1> <score2> ..."
            raise ValueError(error)

    except Exception as error:
        print(f"{error}")
