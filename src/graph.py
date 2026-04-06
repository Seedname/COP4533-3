import matplotlib.pyplot as plt
import random
from string import ascii_lowercase as ALPHABET
from run import hvlcs_complete
import time
import pathlib
from tqdm import tqdm
import json


def random_input(alphabet_size: int, string_size: int, possible_values: list[int]) -> tuple[dict[str, int], str, str]:
    # get the letters used in the alphabet
    letters = random.sample(ALPHABET, alphabet_size)

    # generate their values
    character_map: dict[str, int] = {
        letter: random.choice(possible_values) # choose a random value from the possible values
        for letter in letters
    }

    # generate strings A and B
    A = ''.join(random.choice(letters) for _ in range(string_size))
    B = ''.join(random.choice(letters) for _ in range(string_size))

    return character_map, A, B



def run(string_lengths: list[int], alphabet_size: int, samples: int) -> list[int]:

    # character values from 1 to 10
    possible_values = list(range(1, 11))

    # runtime bins
    runtimes = [0] * len(string_lengths)

    for _ in tqdm(range(samples)):
        for i, string_length in enumerate(string_lengths):
            # get random values
            character_map, A, B = random_input(alphabet_size, string_length, possible_values)

            # time the program
            start_time = time.time_ns()

            result, value = hvlcs_complete(character_map, A, B)

            end_time = time.time_ns()

            # compute completion time
            total_time = end_time - start_time

            # add to the runtime for this string length
            runtimes[i] += total_time


    # average based off the number of samples
    runtimes = [runtime / samples for runtime in runtimes]

    return runtimes



if __name__ == "__main__":
    data_dir = pathlib.Path(__file__).parent.parent / "data"

    # make the data directory if it doesn't exist
    data_dir.mkdir(exist_ok=True)

    # string lengths to run it on
    string_lengths: list[int] = list(range(25, 2001, 100))

    # use all strings in the alphabet
    alphabet_size: int = 26

    # 10 samples per string length
    samples: int = 10        

    # compute the runtimes
    runtimes: list[int] = run(string_lengths, alphabet_size, samples)


    # save the data to a file
    with open(data_dir / "data.json", "w") as f:
        json.dump({
            "samples": samples,
            "alphabet_size": alphabet_size,
            "string_lengths": string_lengths,
            "runtimes": runtimes
        }, f, indent=2)


    # graph the runtimes
    plt.plot(string_lengths, runtimes, marker='o')
    plt.xlabel("String Length")
    plt.ylabel("Completion Time (ns)")
    plt.title("String Length vs. DP Completion Time")

    # save figure to file
    plt.savefig(data_dir / f"graph.png")

    # show the figure
    plt.show()
    # close it
    plt.close()
