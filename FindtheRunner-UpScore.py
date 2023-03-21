if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    mx = max(arr)
    score = None

    for num in arr:
        if num == mx:
            pass
        elif score is None or num > score:
            score = num

    print(score)
