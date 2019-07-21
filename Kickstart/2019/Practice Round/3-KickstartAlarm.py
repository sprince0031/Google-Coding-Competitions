
T = int(input())
for testcase in range(1, T+1):
    N, K, x1, y1, C, D, E1, E2, F = [int(i) for i in input().split()]
    requiredList = []
    mod = 1000000007
    for i in range(0, N):
        xi, yi = ( C * x1 + D * y1 + E1 ) % F, ( C * x1 + D * y1 + E2 ) % F
        requiredList.append((xi + yi) % F)
        x1, y1 = xi, yi
    contiguousSubLists = [requiredList[i:i+j] for i in range(0, N) for j in range(1, N-i+1)]
    powerSum = 0
    for k in range(1, K+1):
        power = 0
        for subList in contiguousSubLists:
            for i in range(1, len(subList)+1):
                power += subList[i-1] * (i**k)
        #         print("subList[i-1]: {} * (i: {} ** k: {}) = {}, power: {}".format(subList[i-1], i, k, subList[i-1] * (i**k), power))
        #     print("End of sublist: {}".format(subList))
        # print(power)
        powerSum += power % mod
    # print(powerSum)
    # result = 0
    # GP_Sum = K
    # mod = 1000000007
    # for i in range(1,N+1):
    #     if i != 1:
    #         GP_Sum += (pow(i, K+1)-1) * pow(i-1, mod-2)
    #         print(GP_Sum)
    #         GP_Sum %= mod
    #     result += GP_Sum * requiredList[i-1]
    #     result %= mod
    print("Case #{}: {}".format(testcase, powerSum%mod))
