# 問題


# URL 
# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cl

# 入出力例
# input: 
# 7 50
# 11 12 16 22 27 28 31

# output:
# 13


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    ans = 0
    for i in range(N):
        sum = 0
        r = i
        while (sum+A[r] <= K):
            sum += A[r]
            r += 1
            if(r==N):
                break
        ans += r-i
    
    print(ans)
        



if __name__ == "__main__":
    main()