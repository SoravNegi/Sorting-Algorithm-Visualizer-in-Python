def partition(data, head, tail, drawData, timeTick, root, switch):
    border = head         
    pivot = data[tail]  

    # drawData(data, getColordarray(len(data), head, tail, border, border))
    # time.sleep(timeTick)
    root.after(timeTick, drawData(data,getColordarray(len(data), head, tail, border, border)))

    for j in range(head, tail):
        root.update()
        if(switch == False):
            return
        if data[j] < pivot:

            # drawData(data, getColordarray(len(data), head, tail, border, j, True))
            # time.sleep(timeTick)
            root.after(timeTick, drawData(data,getColordarray(len(data), head, tail, border, j, True)))

            data[border], data[j] = data[j], data[border]
            border += 1

        # drawData(data, getColordarray(len(data), head, tail, border, j))
        # time.sleep(timeTick)
        root.after(timeTick, drawData(data,getColordarray(len(data), head, tail, border, j)))

    # drawData(data, getColordarray(len(data), head, tail, border, j, True))
    # time.sleep(timeTick)
    root.after(timeTick, drawData(data,getColordarray(len(data), head, tail, border, j, True)))

    data[border], data[tail] = data[tail], data[border]
    return border 
  
def quick_Sort(data, head, tail, drawData, timeTick, root, switch):
    if head < tail:
        root.update()
        if(switch == False):
            return
        partitionIdx = partition(data, head, tail, drawData, timeTick, root, switch)
        quick_Sort(data, head, partitionIdx-1, drawData, timeTick, root, switch)
        quick_Sort(data, partitionIdx+1, tail, drawData, timeTick, root, switch)

def getColordarray(datalen, head, tail, border,currIdx, isSwaping = False):
    colorArray = []
    for i in range(datalen):
        #base coloring
        if i>= head and i <= tail:
           colorArray.append('grey')
        else:
            colorArray.append('white')
        
        if i == tail:
            colorArray[i] = 'blue'
        elif i == border:
            colorArray[i] = 'red'
        elif i == currIdx:
            colorArray[i] = 'yellow'

        if isSwaping:
            if i == border or i == currIdx:
                colorArray[i] == 'green'
    return colorArray