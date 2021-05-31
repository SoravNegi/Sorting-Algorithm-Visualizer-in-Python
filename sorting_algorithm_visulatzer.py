from tkinter import *
from tkinter import ttk
import random
# from bubbleSort import bubble_Sort
# from quickSort import quick_Sort
# from mergeSort import merge_Sort


root = Tk()
root.title('Sorting Algorithm Visualisation')
root.maxsize(1000, 700)
root.config(bg='orange')

#Variable
selected_alg = StringVar()
speed_Type = StringVar()
data = []


# misc buttons functions
# switch = True
def switchon():
    global switch
    switch = True
    StartAlgorithm()

def stop():
    global switch
    switch = False

def exit():
    root.destroy()

#functions

def setspeed():
    if speedMenu.get() == 'Slowest':
        return 1000
    elif speedMenu.get() == 'Slow':
        return 500
    elif speedMenu.get() == 'Medium':
        return 100
    elif speedMenu.get() == 'Fast':
        return 10
    else:
        return 0

def drawData(data, colorArray):
    canvas.delete("all")
    c_height = 400
    c_width = 800
    x_width = c_width / (len(data)+1)
    offset = 4
    spacing = 2
    normalizationData = [i / max(data) for i in data]
    for i, height in enumerate(normalizationData):
        #top left
        x0 = i*x_width+offset+spacing
        y0 = c_height-height*370
        #buttom right
        x1 = (i+1)*x_width+offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        #canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))

    root.update_idletasks()

def Generate():

    global data
    #minVal = int(minEntry.get())
    #maxVal = int(maxEntry.get())
    #size = int(sizeEntry.get())
 
    data = []
    for _ in range(0,51):
        data.append(random.randrange(1,100))

    drawData(data, ['orange' for x in range(len(data))])

def StartAlgorithm():
    global data, switch

    if not data: return

    if algMenu.get() == 'Quick Sort':
        quick_Sort(data, 0, len(data)-1, drawData, setspeed())
    elif algMenu.get() == 'Bubble Sort':
        bubble_Sort(data, drawData, setspeed())
    elif algMenu.get() == 'Merge Sort':
        merge_Sort(data, drawData, setspeed())
        
    drawData(data, ['orange' for x in range(len(data))])

#Sorting Algorithms

#  1.Bubble Sort
def bubble_Sort(data, drawData, timeTick):
    global switch
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

#  2.MergeSort
def merge_Sort(data, drawData, timeTick):
    global switch
    root.update()
    if(switch == False):
        return
    merge_sort_alg(data,0, len(data)-1, drawData, timeTick)


def merge_sort_alg(data, left, right, drawData, timeTick):
    global switch
    if left < right:
        root.update()
        if(switch == False):
            return
        middle = (left + right) // 2
        merge_sort_alg(data, left, middle, drawData, timeTick)
        merge_sort_alg(data, middle+1, right, drawData, timeTick)
        merge(data, left, middle, right, drawData, timeTick)

def merge(data, left, middle, right, drawData, timeTick):
    global switch
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

#  3.QuickSort
def partition(data, head, tail, drawData, timeTick):
    global switch
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
  
def quick_Sort(data, head, tail, drawData, timeTick):
    global switch
    if head < tail:
        root.update()
        if(switch == False):
            return
        partitionIdx = partition(data, head, tail, drawData, timeTick)
        quick_Sort(data, head, partitionIdx-1, drawData, timeTick)
        quick_Sort(data, partitionIdx+1, tail, drawData, timeTick)

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

#frame/base Layout

frame1 = Frame(root, width=900, height=300, bg='AliceBlue')
frame1.grid(row=0, column=0, padx=5, pady=5)

UI_frame = Frame(frame1, width=900, height=300, bg='BurlyWood')
UI_frame.grid(row=0, column=0, padx=5, pady=5)

canvas = Canvas(root, width=800, height=400, bg='AntiqueWhite')
canvas.grid(row=1, column=0, padx=5, pady=5, sticky=NSEW)

#User Interface Area
#Row[0]
Label(UI_frame, text="Algorithm: ", bg='AliceBlue').grid(row=0, column=0, padx=5, pady=5)
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Bubble Sort','Merge Sort','Quick Sort'], background='AliceBlue')
algMenu.grid(row=0, column=2, padx=5, pady=5)
algMenu.current(0)

# Label(UI_frame, text="Speed: ", bg='AliceBlue').grid(row=1, column=0, padx=5, pady=5)
# speedScale = Scale(UI_frame, from_=0, to=0.5, length=100, digits=1, resolution=0.1, orient=HORIZONTAL, bg='AliceBlue')
# speedScale.grid(row=1, column=1, padx=5, pady=5, sticky=W)

#Row[1]

# sizeEntry = Scale(UI_frame, from_=3, to=25, resolution=1, orient=HORIZONTAL, label="Data Size")
# sizeEntry.grid(row=1, column=0, padx=5, pady=5)

# minEntry = Scale(UI_frame, from_=0, to=10, resolution=1, orient=HORIZONTAL, label="Min Value")
# minEntry.grid(row=1, column=1, padx=5, pady=5)

# maxEntry = Scale(UI_frame, from_=10, to=100, resolution=1, orient=HORIZONTAL, label="Max Value")
# maxEntry.grid(row=1, column=2, padx=5, pady=5)

Label(UI_frame, text="Speed: ", bg='AliceBlue').grid(row=1,column=0,padx=5,pady=5,sticky=W)
speedMenu = ttk.Combobox(UI_frame,textvariable=speed_Type,values=["Real-Time",'Fast','Medium','Slow','Slowest'], background='AliceBlue')
speedMenu.grid(row=1,column=2,padx=5,pady=5,sticky=W)
speedMenu.current(1)

#buttons

Button(UI_frame, text="Generate", command=Generate, bg='AliceBlue').grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)
Button(UI_frame, text="Start", command=switchon, bg='AliceBlue').grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)
Button(UI_frame,text='Stop',command=stop,bg='WHITE').grid(row=2,column=2,padx=5,pady=5, sticky=NSEW)
Button(UI_frame,text='Exit',command=exit,bg='WHITE',background='RED',fg='WHITE').grid(row=2,column=3,padx=5,pady=5, sticky=NSEW)


root.mainloop()