# 問題
# ケーキのピースの数 N と,N 個のピースの大きさの情報が与えられたとき,
# JOI くんが取れるピースの大きさの合計の最大値を求めるプログラムを作成せよ．

# URL 
# https://atcoder.jp/contests/joi2015ho/tasks/joi2015ho_b

# 入出力例
# input: 
# 5
# 2
# 8
# 1
# 10
# 9

# output:
# 18


def main():
    N,T = list(map(int, input().split()))

    A = list(map(int, input().split()))
    sum = list(A)
    
    for i in range(1, N):
        sum[i] += sum[i-1]
    
    T %= sum[-1]

    for i in range(N-1,-1, -1):
        if(i==0):
            print('1', (T))
            break
        
        if(T>=sum[i]):
            print((i+2),(T-sum[i]))
            break

        
    



if __name__ == "__main__":
    main()