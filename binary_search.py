
def binSearch(A, e):
    L, R = [], []
    if len(A) == 1:
        if A[1] == e: return True
        else: return False
    else: 
        if (len(A) // 2) == 0: return False
        print(len(A) // 2)
        if A[len(A) // 2] == e: return True
        elif A[len(A) // 2] > e:
            return binSearch(L, e)
        else:
            return binSearch(R, e)


example = [1, 2, 3, 4, 5]

print(binSearch(example, 5))





squaresList = [1, 4, 9, 16, 25, 36]

