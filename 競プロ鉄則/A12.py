# 問題

# URL 
# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_l

# 入出力例
# input: 
# 4 10
# 1 2 3 4

# output:
# 6

def binsearch(mid, K, N, A): # 二分探索
    ans = 0
    for i in range(N):
        ans += mid//A[i]
    if ans>=K:
        return True
    else:
        return False

def main():
    N, K = map(int, input().split())

    A = list(map(int, input().split()))

    l = 1
    r = 10**9

    while l<r:
        mid = (l+r)//2
        if binsearch(mid, K, N, A):
            r = mid # mid時点で印刷数はans以上なので, 探索範囲の右端はmidに設定
        else:
            l = mid+1 # mid時点で印刷数はansより小さいので, 探索範囲の左端はmid+1に設定
    
    print(l)


if __name__ == "__main__":
    main()