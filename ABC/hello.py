from sys import setrecursionlimit

def main():
    N, T = map(int, input().split())
    G = [[] for _ in range(N)]
    visited = [False] *N
    rank = [0] *N

    setrecursionlimit(10**6) # これ入れないとREになった
    for _ in range(N-1):
        A, B = map(int, input().split())
        A -=1
        B -=1
        G[A].append(B)
        G[B].append(A)
    
    def seek_subordinate(s):
        visited[s] = True
        for e in G[s]:
            if visited[e]:
                continue
            rank[s] = max(rank[s], seek_subordinate(e)+1)

        return rank[s]
    
    seek_subordinate(T-1)
    print(*rank)


if __name__ == '__main__':
    main()