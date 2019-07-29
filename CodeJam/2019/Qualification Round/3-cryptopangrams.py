def getPrimes(N):
    primeList = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    for num in range(103, N+1):
        flag = 0
        for n in range(2, num//2):
            if num%n == 0:
                flag = 1
                break
        if flag == 0:
            primeList.append(num)
    return primeList

def getFactors(number, primeList):
    factors = []
    for prime in primeList:
        if len(factors) > 2:
            break
        if number%prime == 0:
            factors.append(prime)
            primeAlphaSet.add(prime)
    return factors

T = int(input())
for testcase in range(1, T+1):
    N, L = map(int, input().split())
    cipherText = list(map(int, input().split()))
    primeList = getPrimes(N)
    primeAlphaSet = set()
    factorPairList = [getFactors(num, primeList) for num in cipherText]
    finalFactorList = factorPairList[0]
    for factorPairIndex in range(1, L):
        for numIndex in range(0, 2):
            if factorPairList[factorPairIndex][numIndex] not in factorPairList[factorPairIndex-1]:
                finalFactorList.append(factorPairList[factorPairIndex][numIndex])
    alphaList = [chr(i) for i in range(ord('A'), ord('Z')+1)]
    alphaDict = dict(zip(sorted(list(primeAlphaSet)), alphaList))
    plainText = ''
    for prime in finalFactorList:
        plainText += alphaDict[prime]
    print("Case #{}: {}".format(testcase, plainText))