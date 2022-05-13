def rotateLeft(d, arr):
    n = len(arr)
    if d < n:
        return arr[d:] + arr[:d]
    
    rem = d % n
    return arr[rem: ] + arr[:rem]

print(rotateLeft(7, [1,2,3,4,5]))
print(rotateLeft(2, [1,2,3,4,5]))
print(rotateLeft(5, [1,2,3,4,5]))
