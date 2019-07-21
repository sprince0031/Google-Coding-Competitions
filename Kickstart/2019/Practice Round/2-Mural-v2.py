T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    Sections = [int(i) for i in input()]
    ans = 0
    Sum = 0
    half = 0
    if N % 2 == 0:
        half = (N//2)
    else:
        half = N//2 + 1
    for i in range(0, N//2):
        # for j in range(N):
        # if i+j <= N-1:
        #     Sum += Sections[i+j]
        # else:
        #     break
        Sum = sum(Sections[i:i+half])
        ans = max(ans, Sum)
    print("Case #{}: {}".format(testcase, ans))

# def solve(N, A):
#     B = [0] * (N + 1)
#     for i in range(1, N + 1):
#         B[i] = B[i - 1] + A[i - 1]
#     res = 0
#     half = (N + 1) // 2
#     for i in range(N):
#         if i + half <= N:
#             res = max(res, B[i + half] - B[i])
#     return res




# T = int(input())
# for testcase in range(1, T+1):
#     N = int(input())
#     Sections = [int(i) for i in input()]
#     res = solve(N, Sections)
#     print("Case #{}: {}".format(testcase, res))