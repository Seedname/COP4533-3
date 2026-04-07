from parse import read_input

def hvlcs(character_map, A, B) -> list[list[int]]:
    # create the 2D dp table of size len(A) + 1 by len(B) + 1, initialized to 0
    dp = [[0 for i in range(len(B) + 1)] for j in range(len(A) + 1)]

    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            # if the two characters match, add the value of the character to the previous dp value
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + character_map[A[i - 1]]
            # else, take the maximum of skipping the character in A or skipping the character in B
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp


if __name__ == "__main__":
    _, character_map, A, B = read_input("file1")
    
    # get the dp table
    dp = hvlcs(character_map, A, B)

    print(f"{dp[len(A)][len(B)]}")