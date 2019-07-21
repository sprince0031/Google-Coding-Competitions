T = int(input())
for t in range(0, T):
    a, b = [int(i) for i in input().split(" ")]
    n = int(input())
    adup, bdup = a, b
    for turn in range(0, n):
        mid = (adup+bdup)//2
        if mid == a:
            print(a+1)
        else:
            print(mid)
        response = input()
        if response == "TOO_BIG":
            bdup = mid - 1
            continue
        elif response == "TOO_SMALL":
            adup = mid + 1
            continue
        elif response == "CORRECT":
            break
        else:
            exit(1)