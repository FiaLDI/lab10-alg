#!usr/bin/env python3
# -*- coding: utf-8 -*-


import heapq

def linear_memory_sum(A, B):
    n = len(A)
    A.sort()
    B.sort()
    min_heap = []
    
    heapq.heappush(min_heap, (A[0] + B[0], 0, 0))
    result = []

    for _ in range(n*n - 1):
        a_sum, i, j = heapq.heappop(min_heap)
        result.append(a_sum)
        
        if j < n - 1:
            heapq.heappush(min_heap, (A[i] + B[j+1], i, j+1))
        if j == 0 and i < n - 1:
            heapq.heappush(min_heap, (A[i+1] + B[j], i+1, j))

    return result

def main():
    A = [3, 1, 2]
    B = [2, 4, 6]
    result = linear_memory_sum(A, B)
    print(result)


if __name__ == "__main__":
    main()