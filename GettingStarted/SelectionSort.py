def selection_sort(A):
    minimium = 0
    for i in range(len(A)):
        minimum = i
        for j in range(i + 1, len(A)):
            if A[j] < A[minimium]:
                minimium = j
        A[i], A[minimium] = A[minimium], A[i]


A = [3, 7, 1, 2, 4, 5]
selection_sort(A)
print(A)
