from tkinter import *
from tkinter import ttk
import random
from sorting_algorithms import bubble_sort, insertion_sort, selection_sort, merge_sort, quick_sort

root = Tk()
root.title('DSA PROJECT Sorting Algorithm Visualiser')
root.geometry("800x700")
root.config(bg='orange')

select_algorithm = StringVar()
arr = []
stop_sorting_flag = False

def stop_sorting():
    global stop_sorting_flag
    stop_sorting_flag = True

def check_stop():
    return stop_sorting_flag

def Generate_array():
    global arr, stop_sorting_flag
    stop_sorting_flag = True
    lowest = int(lowest_Entry.get())
    highest = int(highest_Entry.get())
    size = int(arrsize_Entry.get())
    arr = [random.randrange(lowest, highest+1) for _ in range(size)]
    drawrectangle(arr, ['red' for _ in range(len(arr))]) 

def drawrectangle(arr, colorArray):
    canvas.delete("all")
    canvas_height = 380
    canvas_width = 700
    bar_width = max(canvas_width / (len(arr) + 1), 1)
    border_offset = 30
    spacing = max(1, int(bar_width * 0.1))
    normalized_array = [i / max(arr) for i in arr]

    for i, height in enumerate(normalized_array):
        x0 = i * bar_width + border_offset + spacing
        y0 = canvas_height - height * 340
        x1 = (i + 1) * bar_width + border_offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        if len(arr) <= 50:
            canvas.create_text(x0+2, y0, anchor=SW, text=str(arr[i]), font=("Arial", 8))

    root.update_idletasks()

def sorting():
    global stop_sorting_flag
    stop_sorting_flag = False
    speed = sortingspeed.get()
    algo = select_algorithm.get()
    if algo == 'Bubble Sort':
        bubble_sort(arr, drawrectangle, speed, check_stop)
    elif algo == 'Insertion Sort':
        insertion_sort(arr, drawrectangle, speed, check_stop)
    elif algo == 'Selection Sort':
        selection_sort(arr, drawrectangle, speed, check_stop)
    elif algo == 'Merge Sort':
        merge_sort(arr, drawrectangle, speed, check_stop)
    elif algo == 'Quick Sort':
        quick_sort(arr, drawrectangle, speed, check_stop)

# Centering grid setup
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

options_frame = Frame(root, width=700, height=300, bg='green')
options_frame.grid(row=0, column=0, padx=10, pady=10, sticky="n")

canvas = Canvas(root, width=700, height=350, bg='grey')
canvas.grid(row=1, column=0, padx=10, pady=5, sticky="n")

Label(options_frame, text="Algorithm Choice: ").grid(row=0, column=0, padx=10, pady=10)
algomenu = ttk.Combobox(options_frame, textvariable=select_algorithm, 
                        values=['Bubble Sort', 'Insertion Sort', 'Selection Sort', 'Merge Sort', 'Quick Sort'], width=15)
algomenu.grid(row=0, column=1, padx=5, pady=5)
algomenu.current(0)

sortingspeed = Scale(options_frame, from_=0.01, to=5.0, length=150, digits=3, resolution=0.01,
                     orient=HORIZONTAL, label="Sorting Speed (seconds)")
sortingspeed.grid(row=0, column=2, padx=10, pady=10)

Button(options_frame, text="Start Sorting", command=sorting, bg='red', height=5).grid(row=0, column=3, padx=5, pady=5)
Button(options_frame, text="Stop Sorting", command=stop_sorting, bg='yellow', height=5).grid(row=0, column=4, padx=5, pady=5)

lowest_Entry = Scale(options_frame, from_=1, to=500, resolution=1, orient=HORIZONTAL, label="Lower Limit")
lowest_Entry.grid(row=1, column=0, padx=5, pady=5)

highest_Entry = Scale(options_frame, from_=50, to=1000, resolution=1, orient=HORIZONTAL, label="Upper Limit")
highest_Entry.grid(row=1, column=1, padx=5, pady=5)

arrsize_Entry = Scale(options_frame, from_=3, to=200, resolution=1, orient=HORIZONTAL, label="Array size")
arrsize_Entry.grid(row=1, column=2, padx=5, pady=5)

Button(options_frame, text="Current Array", command=Generate_array, bg='blue', height=5).grid(row=1, column=3, padx=10, pady=10)

root.mainloop()
