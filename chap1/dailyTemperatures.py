from typing import List


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    res = [0] * len(temperatures)
    stack = []
    for i, t in enumerate(temperatures):
        while stack and stack[-1][0] < t:
            _, j = stack.pop()
            res[j] = i - j
        stack.append([t, i])
    return res


print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
print(dailyTemperatures([30, 40, 50, 60]))
print(dailyTemperatures([30, 60, 90]))
