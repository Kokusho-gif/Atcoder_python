# 問題


# URL 
# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_r

# 入出力例
# input: 
# 3 7
# 2 2 3

# output:
# Yes


def main():
    N, S = list(map(int, input().split()))
    A = list(map(int, input().split()))

    dp = [[0 for _ in range(S+1)] for _ in range(N+1)]

    dp[0][0] = 1

    for i in range(1,N+1):
        for j in range(S+1):
            if dp[i-1][j]==1:
                dp[i][j] = 1
                if j+A[i-1] <= S:
                    dp[i][j+A[i-1]] = 1
    
    if dp[N][S]==1:
        print('Yes')
    else:
        print("No")


if __name__ == "__main__":
    main()