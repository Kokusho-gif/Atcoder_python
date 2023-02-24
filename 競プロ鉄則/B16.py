# 問題


# URL 
# https://atcoder.jp/contests/tessoku-book/tasks/dp_a

# 入出力例
# input: 
# 4
# 10 30 40 20

# output:
# 30


def main():
    N = int(input())
    h = list(map(int, input().split()))

    INF = 1 << (4*5)

    dp = [INF for _ in range(N)]

    dp[0] = 0

    for i in range(1,N):
        if i>=2:
            dp[i] = min(dp[i-1]+abs(h[i-1]-h[i]), dp[i-2]+abs(h[i-2]-h[i]))
        else:
            dp[i] = dp[i-1]+abs(h[i-1]-h[i])
    
    print(dp[N-1])


if __name__ == "__main__":
    main()