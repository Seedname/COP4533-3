from parse import read_input
from hvlcs import hvlcs


def backtrack(dp, A) -> str:
    i = len(dp) - 1
    j = len(dp[0]) - 1
    res = []

    while i > 0 and j > 0:
        # if the value is equal to the previous value, then this character must not be used
        if dp[i][j] == dp[i - 1][j]:
            i -= 1
        elif dp[i][j] == dp[i][j - 1]:
            j -= 1
        # otherwise, we use the character and add it to the result string
        else:
            res.append(A[i - 1])
            i -= 1
            j -= 1

    return ''.join(reversed(res))


if __name__ == "__main__":
    _, character_map, A, B = read_input("file1")
    
    # get the dp table
    dp = hvlcs(character_map, A, B)

    # get the hvlcs string
    res = backtrack(dp, A)

    print(res)