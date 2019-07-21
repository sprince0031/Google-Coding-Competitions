def finalAnswer(group1, group2, fullGroupList, dictOfDonts):
    ans = ''
    for Name in fullGroupList:
        if Name not in group1 or Name not in group2:
            flag1, flag2 = 0, 0
            for name in group1:
                if Name not in dictOfDonts[name]:
                    continue
                else:
                    flag1 = 1
                    break
            if flag1 == 0:
                group1.append(Name)
            else:
                for name in group2:
                    if Name not in dictOfDonts[name]:
                        continue
                    else:
                        flag2 = 1
                        break
                if flag2 == 0:
                    group2.append(Name)
                else:
                    return 'No'
    return 'Yes'

fin = open('A-small-practice-1.in', 'r')
T = int(fin.readline())
for testcase in range(1, T+1):
    M = int(fin.readline())
    troublesomePairs = [fin.readline().split() for i in range(0, M)]
    fullGroupSet = set()
    [fullGroupSet.add(name) for troublesomePair in troublesomePairs for name in troublesomePair]
    fullGroupList = list(fullGroupSet)
    print(testcase, M)
    print(fullGroupList)
    dictOfDonts = dict()
    for name in fullGroupList:
        subGroupSet1, subGroupSet2 = set(), set()
        for troublesomePair in troublesomePairs:
            if name == troublesomePair[0]:
                subGroupSet1.add(troublesomePair[1])
            if name == troublesomePair[1]:
                subGroupSet2.add(troublesomePair[0])
        listOfDonts1, listOfDonts2 = list(subGroupSet1), list(subGroupSet2)
        dictOfDonts[name] = sorted(listOfDonts1 + listOfDonts2)
    print(dictOfDonts)
    group1, group2 = [troublesomePairs[0][0]], [troublesomePairs[0][1]]
    # print(group1)
    fout = open('A-small-practice-1.out', 'a')
    ans = finalAnswer(group1, group2, fullGroupList, dictOfDonts)
    fout.write("Case #{}: {} \n".format(testcase, ans))
    fout.close()
    