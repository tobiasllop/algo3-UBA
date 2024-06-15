import numpy as np

def dantzig(dist, n):
    energia = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
        energia += np.sum(dist[:k+1, :k+1])
    return energia

def main():
    tests = int(input())
    for t in range(tests):
        n = int(input())
        L = np.zeros((n, n))
        for i in range(n):
            L[i] = list(map(int, input().split()))

        orden = list(map(int, input().split()))[::-1]
        L = L[np.ix_(orden, orden)]      
        print(dantzig(L, n)) 

if __name__ == "__main__":
    main()
