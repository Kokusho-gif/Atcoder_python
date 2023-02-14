import numpy as np
import heapq

def dijkstra(s, G):
    n = len(G)
    cost = [float('inf')] * n
    prev = [-1] * n

    cost[s] = 0
    edgelist = []
    heapq.heappush(edgelist, (cost[s], s))

    while edgelist:
        minedge = heapq.heappop(edgelist)
        if cost[minedge[1]] < minedge[0]:
            continue
        v = minedge[1]
        for e in G[v]:
            if cost[e[1]] > cost[v] + e[0]:
                cost[e[1]] = cost[v] + e[0]
                prev[e[1]] = v
                heapq.heappush(edgelist, (cost[e[1]], e[1]))

    return cost, prev





def main():
    N, M = list(map(int, input().split()))
    G = heapq.heapify([[] for _ in range(N)])
    for i in range(M):
        A,B,C = list(map(int, input().split(' ')))
        A -=1; B -=1
        G[A].append((C, B))
        G[B].append((C, A))

    dist, prev = dijkstra(0,G)
    print(dist)

    return


if __name__ == '__main__':
    main()