'''
問題


URL 
https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cs

入出力例
input: 
tokyo
kyoto

output:
4

'''


def main():
    S = input()
    T = input()

    dp = [[0 for _ in range(len(T)+1)] for _ in range(len(S)+1)]
    dp[0][0] = 0
    for i in range(len(S)+1):
        for j in range(len(T)+1):
            if S[i-1]==T[j-1] and i>=1 and j>=1:
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1])
            elif i>=1 and j>=1:
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1)
            elif i>=1:
                dp[i][j] = dp[i-1][j] + 1
            elif j>=1:
                dp[i][j] = dp[i][j-1] + 1
    
    print(dp[len(S)][len(T)])



if __name__ == "__main__":
    main()