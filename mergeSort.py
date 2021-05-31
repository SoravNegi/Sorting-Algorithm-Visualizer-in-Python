def merge_Sort(data, drawData, timeTick, root, switch):
    root.update()
    if(switch == False):
        return
    merge_sort_alg(data,0, len(data)-1, drawData, timeTick, root, switch)


def merge_sort_alg(data, left, right, drawData, timeTick, root,switch):
    if left < right:
        root.update()
        if(switch == False):
            return
        middle = (left + right) // 2
        merge_sort_alg(data, left, middle, drawData, timeTick, root)
        merge_sort_alg(data, middle+1, right, drawData, timeTick, root)
        merge(data, left, middle, right, drawData, timeTick, root, switch)

def merge(data, left, middle, right, drawData, timeTick, root, switch):
    # drawData(data, getColorArray(len(data), left, middle, right))
    # time.sleep(timeTick)
    root.after(timeTick, drawData(data, getColorArray(len(data), left, middle, right)))

    leftPart = data[left:middle+1]
    rightPart = data[middle+1: right+1]

    leftIdx = rightIdx = 0

    for dataIdx in range(left, right+1):
        root.update()
        if(switch == False):
            return
        if leftIdx < len(leftPart) and rightIdx < len(rightPart):
            if leftPart[leftIdx] <= rightPart[rightIdx]:
                data[dataIdx] = leftPart[leftIdx]
                leftIdx += 1
            else:
                data[dataIdx] = rightPart[rightIdx]
                rightIdx += 1
        
        elif leftIdx < len(leftPart):
            data[dataIdx] = leftPart[leftIdx]
            leftIdx += 1
        else:
            data[dataIdx] = rightPart[rightIdx]
            rightIdx += 1
    
    # drawData(data, ["green" if x >= left and x <= right else "white" for x in range(len(data))])
    # time.sleep(timeTick)
    root.after(timeTick, drawData(data,['orange' if x >= left and x <= right else "white" for x in range(len(data))]))

def getColorArray(leght, left, middle, right):
    colorArray = []

    for i in range(leght):
        if i >= left and i <= right:
            if i >= left and i < middle:
                colorArray.append("SpringGreen")
            elif i==middle:
                colorArray.append("red")
            else:
                colorArray.append("Tomato")
        else:
            colorArray.append("#0CA8F6")

    return colorArray