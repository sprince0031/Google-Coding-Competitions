def xor_sum(A, N):
    if N > 1:
        # print(A)
        xorSum = A[0] ^ A[1]
        for i in range(2, N):
            xorSum ^= A[i]
        return xorSum
    else:
        # print(A)
        return A[0]
    
def  countSetBitsAndReturnIfEven(n): 
    count = 0
    while (n): 
        count += n & 1
        n >>= 1
    if count%2 == 0:
        return count
    else:
        return -1

# T = int(input())
# for testcase in range(1, T+1):
#     N, Q = map(int, input().split())
#     A = list(map(int, input().split()))
#     ans = ''
#     for modification in range(0, Q):
#         Pi, Vi = map(int, input().split())
#         A[Pi] = Vi
#         for length in range(N, 0, -1):
#             print(length)
#             for e in range(0, N-length):
#                 print(e)
#                 reqList, it = window(A, length)
#                 print(reqList, it)
#                 if countSetBitsAndReturnIfEven(xor_sum(reqList, len(reqList))) is not -1:
#                     ans += "{} ".format(length)
#                     continue
#                 else:
#                     restOfList = []
#                     for w in range(N-length-1):
#                        reqList = subsequentWindows(A, it) 
#                        if countSetBitsAndReturnIfEven(xor_sum(reqList, len(reqList))) is not -1:
#                             ans += "{} ".format(length)
#                             continue
#                 if len(ans) // 2 == modification + 1:
#                     continue

#             if len(ans) // 2 == modification + 1:
#                 continue
                    
            


#         # powSetOfA = powSet(A, N)
#         # # print(powSetOfA, len(powSetOfA))
#         # # xor_sums = [[xor_sum(i, len(i)), i] for i in powSetOfA]
#         # # print(xor_sums, len(xor_sums))
#         # xor_even_max = 0
#         # for i in powSetOfA:
#         #     xorSum = xor_sum(i, len(i))
#         #     print(xorSum, i)
#         #     if countSetBitsAndReturnIfEven(xorSum) is not -1:
#         #         if len(i) > xor_even_max:
#         #             xor_even_max = len(i)
#         #         else:
#         #             continue
            
#         # # xor_even_list = [countSetBitsAndReturnIfEven(i[0]) for i in xor_sums] # if countSetBitsAndReturnIfEven(i[0]) is not -1
#         # # print(xor_even_list, len(xor_even_list))
#         # ans += "{} ".format(xor_even_max)
#     print("Case #{}: {}".format(testcase, ans[:len(ans)]))

def generatePascalTriangleRow(n):
    pascalRow = [1]
    element = 1
    # if n%2 == 0:
    rangeToCalculate = n//2
    # else:

    for i in range(0, rangeToCalculate):
        element *= (n-i)/(i+1)
        pascalRow.append(int(element))
    if n % 2 != 0:
        return pascalRow + pascalRow[:-(len(pascalRow)):-1]
    else:
        toBeReversed = pascalRow[-len(pascalRow)+1:-1]
        return pascalRow + toBeReversed[::-1]

T = int(input())
for testcase in range(1, T+1):
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    ans = ''
    pascalRow = generatePascalTriangleRow(N)
    # print(pascalRow)
    for modfication in range(0, Q):
        Pi, Vi = map(int, input().split())
        A[Pi] = Vi
        tempN = N
        breakFlag = 0
        for numsToTakeOut in range(len(pascalRow)):
            if numsToTakeOut == 0:
                evenOrNot = countSetBitsAndReturnIfEven(xor_sum(A, N))
                if evenOrNot is not -1:
                    ans = "{} ".format(N)
                    # breakFlag = 1
                    break
                else:
                    tempN -= 1
            else:
                for possibility in range(0, pascalRow[numsToTakeOut]):
                    

            if breakFlag == 1:
                break
        # numberOfWindows, flag = 1, 0
        # for windowSize in range(N, 0, -1):
        #     for window in range(0, numberOfWindows):
        #         if countSetBitsAndReturnIfEven(xor_sum(A[window:windowSize+window], windowSize)) is not -1:
        #             ans += "{} ".format(windowSize)
        #             flag = 1
        #             break
        #     if flag == 0:
        #         numberOfWindows += 1
        #     else:
        #         break
    print("Case #{}: {}".format(testcase, ans[:len(ans)]))