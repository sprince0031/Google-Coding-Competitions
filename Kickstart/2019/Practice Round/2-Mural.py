T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    Sections = [int(i) for i in input()]
    paintedOrNot = [0 for i in range(0, len(Sections))]
    currentPaintedSectionIndex = Sections.index(max(Sections))
    maxBeautyScore = Sections[currentPaintedSectionIndex]
    paintedOrNot[currentPaintedSectionIndex] = 1
    if paintedOrNot[0] != 1:
        Sections.pop(0)
        paintedOrNot.pop(0)
    else:
        Sections.pop()
        paintedOrNot.pop()
    flag = 0
    while True:
        leftFreeValIndex = paintedOrNot.index(1)-1
        rightFreeValIndex = len(paintedOrNot) - paintedOrNot[::-1].index(1)
        if leftFreeValIndex == -1 and rightFreeValIndex != len(paintedOrNot):
            currentPaintedSectionIndex = rightFreeValIndex
            maxBeautyScore += Sections[currentPaintedSectionIndex]
            paintedOrNot[currentPaintedSectionIndex] = 1
            flag = 1
            # print("1", Sections)
            # print("1", paintedOrNot)
            # print("1", maxBeautyScore, currentPaintedSectionIndex)
        elif rightFreeValIndex == len(paintedOrNot) and leftFreeValIndex != -1:
            currentPaintedSectionIndex = leftFreeValIndex
            maxBeautyScore += Sections[currentPaintedSectionIndex]
            paintedOrNot[currentPaintedSectionIndex] = 1
            flag = 0
            # print("2", Sections)
            # print("2", paintedOrNot)
            # print("2", maxBeautyScore, currentPaintedSectionIndex)
        elif leftFreeValIndex != -1 and rightFreeValIndex != len(paintedOrNot):
            if Sections[leftFreeValIndex] > Sections[rightFreeValIndex]:
                currentPaintedSectionIndex = leftFreeValIndex
                maxBeautyScore += Sections[currentPaintedSectionIndex]
                paintedOrNot[currentPaintedSectionIndex] = 1
                # print("3.1", Sections)
                # print("3.1", paintedOrNot)
                # print("3.1", maxBeautyScore, currentPaintedSectionIndex)
            else:
                currentPaintedSectionIndex = rightFreeValIndex
                maxBeautyScore += Sections[currentPaintedSectionIndex]
                paintedOrNot[currentPaintedSectionIndex] = 1
                # print("3.2", Sections)
                # print("3.2", paintedOrNot)
                # print("3.2", maxBeautyScore, currentPaintedSectionIndex)
        else:
            # print("4", Sections)
            # print("4", paintedOrNot)
            # print("4", maxBeautyScore, currentPaintedSectionIndex)
            break
        if paintedOrNot[0] == 0 and flag == 0:
            Sections.pop(0)
            paintedOrNot.pop(0)
            currentPaintedSectionIndex -= 1
            # print("pop if", Sections)
            # print("pop if", paintedOrNot)
            flag = 1
        elif paintedOrNot[len(Sections)-1] == 0 and flag == 1:
            Sections.pop()
            paintedOrNot.pop()
            # print("pop elif", Sections)
            # print("pop elif", paintedOrNot)
            flag = 0
        else:
            break
    print("Case #{}: {}".format(testcase, maxBeautyScore))