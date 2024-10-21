import random
from datetime import datetime


def waiting_game():
    """
    Implemenation of a waiting game, where the user is aked to guess when
    target time (seconds) has elapsed, which is a random value between 2 to 10
    seconds. Finally, the user is informed about the closeness of his answer.
    """
    target_seconds = random.randint(2, 10)
    print(f"Your target time is {target_seconds} seconds")
    input(f"---Press Enter to Begin---\n")
    start = datetime.now()
    input(f"...Press Enter again after {target_seconds} seconds...\n")
    stop = datetime.now()
    elapsed_time = (stop - start).total_seconds()
    print(f"Elapsed time: {elapsed_time :.3f} seconds")
    if target_seconds == elapsed_time:
        print("Right on target! Congratulations!")
    elif elapsed_time > target_seconds:
        print(f"{elapsed_time - target_seconds :.3f} seconds too slow!")
    else:
        print(f"{target_seconds - elapsed_time :.3f} seconds too fast!")


if __name__ == "__main__":
    waiting_game()
