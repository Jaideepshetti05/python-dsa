def merge_intervals(intervals):
    intervals.sort()
    result = []

    for start, end in intervals:
        if not result or result[-1][1] < start:
            result.append([start, end])
        else:
            result[-1][1] = max(result[-1][1], end)

    return result


data = [[1, 3], [2, 6], [8, 10], [9, 12]]

print(merge_intervals(data))