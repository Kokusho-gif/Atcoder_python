# 問題


# URL 
# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_p

# 入出力例
# input: 
# 5
# 2 4 1 3
# 5 3 7


# output:
# 8



def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    INF = 1 << (5*2)
    dp = [INF for _ in range(N)]
    dp[0] = 0

    for i in range(1,N):
        if i>=2:
            dp[i] = min(dp[i-1] + A[i-1], dp[i-2] + B[i-2])
        else:
            dp[i] = dp[i-1] + A[i-1]
    
    print(dp[N-1])




if __name__ == "__main__":
    main()