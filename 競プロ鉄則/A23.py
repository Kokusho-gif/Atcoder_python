'''
問題


URL 
https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_w

入出力例
input: 
3 4
0 0 1
0 1 0
1 0 0
1 1 0

output:
2

'''


def main():
    N, M = map(int, input().split())
    A = [[None]*N for _ in range(M)]
    for i in range(M):
        A[i] = map(int, input().split())
    
    



if __name__ == "__main__":
    main()