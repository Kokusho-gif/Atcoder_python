# 問題


# URL 
# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cm

# 入出力例
# input: 
# 6 30
# 5 1 18 7 2 9

# output:
# Yes

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    Q1 = []
    Q2 = []

    for i in range(1<<int(N/2)):
        sum = 0
        print(i)
        for j in range(int(N/2)):
            if (i>>j & 1):
                sum += A[j]
                print(f'{j}: {A[j]}')
        Q1.append(sum)
    print(Q1)


if __name__ == "__main__":
    main()