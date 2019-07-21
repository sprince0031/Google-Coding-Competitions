# from itertools import combinations

# def getCombinations(lst, n):
#     if n==0:
#         return [[]]
#     l=[]
#     for i in range(0,len(lst)):
#         m=lst[i]
#         remLst=lst[i+1:]
#         for p in getCombinations(remLst,n-1):
#             l.append([m]+p)
#     return l

T = int(input())
for testcase in range(1, T+1):
    N, P = [int(i) for i in input().split()]
    S = sorted([int(i) for i in input().split()], reverse=True)
    requiredTrainingHours = 0
    for i in range(1, P):
        requiredTrainingHours += S[0] - S[i]
    # # C = getCombinations(S, P)
    # optimalChoice = ()
    # lowestDiff = float('Inf')
    # for tup in C:
    #     currentDiff = max(tup) - min(tup)
    #     if currentDiff < lowestDiff:
    #         optimalChoice = tup
    #         lowestDiff = currentDiff
    # requiredTrainingHours = 0
    # optimalChoice = sorted(list(optimalChoice), reverse=True)
    # for i in range(1, len(optimalChoice)):
    #     requiredTrainingHours += optimalChoice[0] - optimalChoice[i]

    print("Case #{}: {}".format(testcase, requiredTrainingHours))