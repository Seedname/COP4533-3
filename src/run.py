from hvlcs import hvlcs
from backtrack import backtrack
from parse import read_input, write_output


def hvlcs_complete(character_map: dict[str, int], A: str, B: str) -> tuple[str, int]:
    # get the dp table
    dp: list[list[int]] = hvlcs(character_map, A, B)

    # get the hvlcs string
    result: str = backtrack(dp, A)

    # get the value of the string
    value: int = dp[len(A)][len(B)]

    return result, value


if __name__ == "__main__":
    file_name = "file1"

    # read the input
    _, character_map, A, B = read_input(file_name)

    # get the reuslt and value    
    result, value = hvlcs_complete(character_map, A, B)

    # write the output to a file
    output: str = write_output(file_name, value, result)

    print(output)
