T = int(input())
for testcase in range(1, T+1):
    number = input()
    otherNumber = '0'*len(number)
    for i in range(0, len(number)):
        if number[i] == '4':
            number = number[:i] + '3' + number[i+1:]
            otherNumber = otherNumber[:i] + '1' + otherNumber[i+1:]
    print("Case #{}: {} {}".format(testcase, int(number), int(otherNumber)))