import random

# Lecture version of QuickSort
# the commented-out versions of partition and quicksort are my attempts to follow
# the lecture pseudocode but afterwards I gave up out of frustration :/

#def partition(A, p):
    # n = len(A)
    # Al = []
    # Ar = []
    
    # for i in range(1, n):
    #     if i != p:
    #         if A[i] < A[p]:
    #             Al.append(A[i])
    #         else:
    #             Ar.append(A[i])
    # A = Al + [A[p]] + Ar
    # print(A, ' ', len(Al) + 1)
    # return A, (len(Al) + 1)

def partition1(A):
    p = A[random.randrange(0, len(A))]
    Al = [i for i in A if i < p]
    Ap = [i for i in A if i == p]
    Ar = [i for i in A if i > p]
    return Al, Ap, Ar

# def QuickSort(A):
#     n = len(A)
#     if n <= 1:
#         return A
#     p = random.randrange(1, n)
#     A, r = partition(A, p)
#     return QuickSort(A[:r]) + QuickSort(A[r:])

def QuickSort1(A):
    n = len(A)
    if n <= 1:
        return A
    Al, Ap, Ar = partition1(A)
    return QuickSort1(Al) + Ap + QuickSort1(Ar)

# exampleList1 = [5, 4, 3, 2, 1]

# print('Before: ', exampleList1)
# exampleList1 = QuickSort1(exampleList1)
# print('After: ', exampleList1)