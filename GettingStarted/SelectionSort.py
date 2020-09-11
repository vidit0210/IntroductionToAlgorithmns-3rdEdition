def selection_sort(A):
    for i in range(len(A)):
        minimum = i
        for j in range(i + 1, len(A)):
            if A[j] < A[minimum]:
                minimum = j
        A[i], A[minimum] = A[minimum], A[i]


A = [3, 7, 1, 2, 4, 5]
selection_sort(A)
print(A)
