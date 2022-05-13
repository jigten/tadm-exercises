def hackerlandRadioTransmitters(x, k):
    sorted_land, i, count = sorted(x), 0, 0
    n = len(sorted_land)
    while i < n:
        count += 1;
        next_house = sorted_land[i] + k;
        while i < n and sorted_land[i] <= next_house:
            i += 1
        next_house = sorted_land[i - 1] + k;
        while i < n and sorted_land[i] <= next_house:
            i += 1

    return count
    

print(hackerlandRadioTransmitters([1, 2, 3, 4, 5], 1))
print(hackerlandRadioTransmitters([7, 2, 4, 6, 5, 9, 12, 11], 2))
