def sortarray(xs):
    arr = xs.copy()
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

data = [5, 2, 8, 1, 4]
t = sortarray(data)
print(t)