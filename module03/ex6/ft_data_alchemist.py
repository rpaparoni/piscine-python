import random


def main() -> None:
    print("=== Game Data Alchemist ===")

    initial_players: list = ['Alice', 'bob', 'Charlie',
                             'dylan', 'Emma', 'Gregory',
                             'john', 'kevin', 'Liam']
    print(f"\nInitial list of players: {initial_players}")

    capitalized_players: list = [name.capitalize() for name in initial_players]
    print(f"\nNew list with all names capitalized: {capitalized_players}")

    only_capitalized: list = [name for name in initial_players
                              if name[0].isupper()]
    print(f"\nNew list of capitalized names only: {only_capitalized}")

    score_dict: dict = {name: random.randint(10, 999)
                        for name in capitalized_players}
    print(f"\nScore dict: {score_dict}")

    total_score: int = sum(score_dict.values())
    score_average: float = round(total_score / len(score_dict), 2)
    print(f"\nScore average is {score_average}")

    high_scores: dict = {name: score for name, score in score_dict.items()
                         if score > score_average}
    print(f"\nHigh scores: {high_scores}")


if __name__ == "__main__":
    main()
