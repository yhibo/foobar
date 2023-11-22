def solution(l, t):
    start = 0
    current_sum = 0

    for end in range(len(l)):
        current_sum += l[end]

        while current_sum > t and start <= end:
            current_sum -= l[start]
            start += 1

        if current_sum == t:
            return [start, end]

    return [-1, -1]