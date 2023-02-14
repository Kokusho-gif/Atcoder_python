# 問題


# URL 
# https://atcoder.jp/contests/abc281/tasks/abc281_c

# 入出力例
# input: 


# output:

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


if __name__ == '__main__':
    main()