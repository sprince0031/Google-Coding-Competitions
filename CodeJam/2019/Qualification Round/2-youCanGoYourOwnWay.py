T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    Lydia = input()
    ansPath = ''
    for step in Lydia:
        if step == 'E':
            ansPath += 'S'
        else:
            ansPath += 'E'
    print("Case #{}: {}".format(testcase, ansPath))