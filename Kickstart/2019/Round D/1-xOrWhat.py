# def powSet(A, N):
#     power = []
#     for i in range(0, 1<<N):
#         subset = []
#         for j in range(0, N):
#             if (1<<j) & i:
#                 subset.append(A[j])
#         power.append(subset)
#     return power[1:]

def window(L, size):
    it = iter(L)
    win = [it.__next__() for cnt in range(size)]
    return win, it
def subsequentWindows(win, it):
    for e in it: # Subsequent windows
        win[:-1] = win[1:]
        win[-1] = e
        return win

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

T = int(input())
for testcase in range(1, T+1):
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    ans = ''
    for modification in range(0, Q):
        Pi, Vi = map(int, input().split())
        A[Pi] = Vi
        for length in range(N, 0, -1):
            print(length)
            for e in range(0, N-length):
                print(e)
                reqList, it = window(A, length)
                print(reqList, it)
                if countSetBitsAndReturnIfEven(xor_sum(reqList, len(reqList))) is not -1:
                    ans += "{} ".format(length)
                    continue
                else:
                    restOfList = []
                    for w in range(N-length-1):
                       reqList = subsequentWindows(A, it) 
                       if countSetBitsAndReturnIfEven(xor_sum(reqList, len(reqList))) is not -1:
                            ans += "{} ".format(length)
                            continue
                if len(ans) // 2 == modification + 1:
                    continue

            if len(ans) // 2 == modification + 1:
                continue
                    
            


        # powSetOfA = powSet(A, N)
        # # print(powSetOfA, len(powSetOfA))
        # # xor_sums = [[xor_sum(i, len(i)), i] for i in powSetOfA]
        # # print(xor_sums, len(xor_sums))
        # xor_even_max = 0
        # for i in powSetOfA:
        #     xorSum = xor_sum(i, len(i))
        #     print(xorSum, i)
        #     if countSetBitsAndReturnIfEven(xorSum) is not -1:
        #         if len(i) > xor_even_max:
        #             xor_even_max = len(i)
        #         else:
        #             continue
            
        # # xor_even_list = [countSetBitsAndReturnIfEven(i[0]) for i in xor_sums] # if countSetBitsAndReturnIfEven(i[0]) is not -1
        # # print(xor_even_list, len(xor_even_list))
        # ans += "{} ".format(xor_even_max)
    print("Case #{}: {}".format(testcase, ans[:len(ans)]))

