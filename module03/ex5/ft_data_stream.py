import random
from typing import Generator


def gen_event() -> Generator[tuple, None, None]:
    names: list = ['alice', 'bob', 'charlie', 'dylan']
    actions: list = ['run', 'eat', 'sleep', 'grab', 'move',
                     'climb', 'swim', 'use', 'release']

    while True:
        name: str = random.choice(names)
        action: str = random.choice(actions)
        yield (name, action)


def consume_event(event_list: list) -> Generator[tuple, None, None]:
    while len(event_list) > 0:
        max_idx: int = len(event_list) - 1
        random_idx: int = random.randint(0, max_idx)

        event: tuple = event_list.pop(random_idx)

        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")

    stream: Generator[tuple, None, None] = gen_event()

    i: int = 0
    while i < 1000:
        event: tuple = next(stream)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
        i += 1

    event_list: list = []
    j: int = 0
    while j < 10:
        event_list += [next(stream)]
        j += 1

    print(f"Built list of 10 events: {event_list}")

    for consumed_event in consume_event(event_list):
        print(f"Got event from list: {consumed_event}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    main()
