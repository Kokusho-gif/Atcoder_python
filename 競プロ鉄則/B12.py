# 問題
# 正の整数 
# N が与えられます。
# x 
# 3
#  +x=N を満たす正の実数 
# x を出力してください。ただし、相対誤差または絶対誤差が 0.001 以下であれば正解とします。

# URL 
# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ck

# 入出力例
# input: 
# 2

# output:
# 1.000000

def binsearch(mid, N):
    if mid**3 + mid >= N:
        return True
    else:
        return False

def main():
    N = int(input())

    l = 1
    r = N/2

    while abs(r-l)>0.01: # 探索幅が0.01以下であれば相対誤差は0.01以下
        mid = (r+l)/2
        if binsearch(mid, N):
            r = mid
        else:
            l = mid
    
    print(r)






if __name__ == "__main__":
    main()