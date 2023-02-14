# 問題


# URL 
# https://atcoder.jp/contests/abc289/tasks/abc289_c


# 入出力例
# input: 
# 3 3
# 2
# 1 2
# 2
# 1 3
# 1
# 2

# output:
# 3


def main():
    N, M = list(map(int, input().split())) # 入力処理1
    a = [set() for i in range(M)]

    for i in range(M): # 入力処理2
        input()
        tmp = set(map(int, input().split()))
        a[i] = a[i].union(tmp)
    
    ans = 0

    for i in range(1, 1<<M): # 部分集合の全列挙
        tmp = set()
        for j in range(M):
            if i>>j & 1:
                tmp = tmp.union(a[j]) # j桁目が1ならa_jを集合に加える

        if len(tmp) == N:
            ans += 1
    
    print(ans)
            
        
            

    return



if __name__ == "__main__":
    main()