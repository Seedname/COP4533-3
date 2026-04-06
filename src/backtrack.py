from parse import read_input
from hvlcs import hvlcs

def backtrack(dp, A, B, character_map) -> str:
    i = len(dp) - 1
    j = len(dp[0]) - 1
    res = []

    while i > 0 and j > 0:
        # if the characters are equal and the values match, we used the character and should add it to the result string
        if A[i - 1] == B[j - 1] and dp[i][j] == dp[i - 1][j - 1] + character_map[A[i - 1]]:
            res.append(A[i - 1])
            i -= 1
            j -= 1
        # otherwise, we check which previous value is optimal and move accordingly
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(res))


if __name__ == "__main__":
    _, character_map, A, B = read_input("file1")
    
    # get the dp table
    dp = hvlcs(character_map, A, B)

    # get the hvlcs string
    res = backtrack(dp, A, B, character_map)

    print(res)