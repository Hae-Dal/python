def bubbleSort(A):
    for numElements in range(len(A), 0, -1):
        is_sorted = True
        for i in range(numElements - 1):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                is_sorted = False

        if is_sorted:
            break

    return A


nums = [0, 1, 5, 4, 7, 8, 2, 10, 17, 20, 95, 84]

print(nums)

bubbleSort(nums)

print(nums)
