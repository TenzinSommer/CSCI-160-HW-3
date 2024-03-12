# textbook version
import random


def swap(A, a, b):
    A[a], A[b] = A[b], A[a]

def partition2(A, p):
    n = len(A)
    swap(A, p, n - 1)
    l = 0
    for i in range(0, n - 1):
        if A[i] < A[n - 1]:
            swap(A, l, i)
            l += 1  
    swap(A, l, n - 1)
    return l

def QuickSort2(A):
    if len(A) <= 1:
        return A
    p = random.randrange(0, len(A))
    r = partition2(A, p)
    # print(A, ' ', r)
    return QuickSort2(A[:r]) + [A[r]] + QuickSort2(A[r + 1:])


# x = [5, 4, 3, 2, 1]
# print(x, ' ', len(x))
# print(QuickSort2(x))  