def bubble_Sort(data, drawData, timeTick, root, switch, stop):
    root.update()
    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            root.update()
            if(switch == False):
                return
            if data[j] > data[j+1] :
                data[j], data[j+1] = data[j+1], data[j]
                #drawData(data, ['green' if x == j or x == j+1 else 'red' for x in range(len(data))])
                root.after(timeTick, drawData(data,['#0CA8F6' if x ==j or x==j+1 else 'orange' for x in range(len(data))]))
    drawData(data, ['blue' for x in range(len(data))])