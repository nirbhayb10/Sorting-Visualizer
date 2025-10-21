from tkinter import *
from tkinter import ttk
import random
from sorting_algorithms import bubble_sort, insertion_sort, selection_sort, merge_sort

root = Tk()
root.title('✨ DSA Project: Sorting Algorithm Visualizer ✨')
root.geometry("900x700")
root.config(bg='#1e1e2f')

select_algorithm = StringVar()
arr = []

def Generate_array():
    global arr
    lowest = int(lowest_Entry.get())
    highest = int(highest_Entry.get())
    size = int(arrsize_Entry.get())
    arr = [random.randrange(lowest, highest + 1) for _ in range(size)]
    drawrectangle(arr, ['#ff4b5c' for _ in range(len(arr))])

def drawrectangle(arr, colorArray):
    canvas.delete("all")
    canvas_height = 400
    canvas_width = 800
    bar_width = max(canvas_width / (len(arr) + 1), 1)
    border_offset = 30
    spacing = max(1, int(bar_width * 0.1))
    normalized_array = [i / max(arr) for i in arr]

    for i, height in enumerate(normalized_array):
        x0 = i * bar_width + border_offset + spacing
        y0 = canvas_height - height * 340
        x1 = (i + 1) * bar_width + border_offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i], outline="")
        if len(arr) <= 40:
            canvas.create_text(x0 + 2, y0, anchor=SW, text=str(arr[i]), font=("Segoe UI", 8), fill="#ffffff")

    root.update_idletasks()

def sorting():
    speed = sortingspeed.get()
    algo = select_algorithm.get()
    if algo == 'Bubble Sort':
        bubble_sort(arr, drawrectangle, speed, lambda: False)
    elif algo == 'Insertion Sort':
        insertion_sort(arr, drawrectangle, speed, lambda: False)
    elif algo == 'Selection Sort':
        selection_sort(arr, drawrectangle, speed, lambda: False)
    elif algo == 'Merge Sort':
        merge_sort(arr, drawrectangle, speed, lambda: False)

style = ttk.Style()
style.theme_use("clam")

style.configure("TFrame", background="#2d2d44")
style.configure("TLabel", background="#2d2d44", foreground="#ffffff", font=("Segoe UI", 10, "bold"))
style.configure("TButton", font=("Segoe UI", 10, "bold"), padding=6)
style.map("TButton",
          background=[("active", "#ff4b5c"), ("!disabled", "#ff6f61")],
          foreground=[("active", "white"), ("!disabled", "white")])

style.configure("TCombobox", fieldbackground="#3b3b58", background="#3b3b58", foreground="white")
style.map("TCombobox", fieldbackground=[("readonly", "#3b3b58")])

options_frame = ttk.Frame(root, padding=15)
options_frame.pack(pady=20)

canvas_frame = Frame(root, bg="#1e1e2f")
canvas_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

canvas = Canvas(canvas_frame, width=850, height=400, bg="#252542", highlightthickness=0)
canvas.pack(pady=20)

Label(options_frame, text="Choose Algorithm:").grid(row=0, column=0, padx=10, pady=10)
algomenu = ttk.Combobox(options_frame, textvariable=select_algorithm,
                        values=['Bubble Sort', 'Insertion Sort', 'Selection Sort', 'Merge Sort'], width=18, state="readonly")
algomenu.grid(row=0, column=1, padx=5, pady=5)
algomenu.current(0)

sortingspeed = Scale(options_frame, from_=0.01, to=2.0, length=150, digits=3, resolution=0.01,
                     orient=HORIZONTAL, label="Sorting Speed (seconds)", fg="white", bg="#2d2d44",
                     highlightthickness=0, troughcolor="#3b3b58", font=("Segoe UI", 9, "bold"))
sortingspeed.grid(row=0, column=2, padx=10, pady=10)

ttk.Button(options_frame, text="Start Sorting ▶", command=sorting).grid(row=0, column=3, padx=10, pady=5)
ttk.Button(options_frame, text="Generate Array 🔁", command=Generate_array).grid(row=0, column=4, padx=10, pady=5)

lowest_Entry = Scale(options_frame, from_=1, to=500, resolution=1, orient=HORIZONTAL, label="Lower Limit",
                     fg="white", bg="#2d2d44", highlightthickness=0, troughcolor="#3b3b58", font=("Segoe UI", 9, "bold"))
lowest_Entry.grid(row=1, column=0, padx=5, pady=5)

highest_Entry = Scale(options_frame, from_=50, to=1000, resolution=1, orient=HORIZONTAL, label="Upper Limit",
                      fg="white", bg="#2d2d44", highlightthickness=0, troughcolor="#3b3b58", font=("Segoe UI", 9, "bold"))
highest_Entry.grid(row=1, column=1, padx=5, pady=5)

arrsize_Entry = Scale(options_frame, from_=3, to=20, resolution=1, orient=HORIZONTAL, label="Array Size",
                      fg="white", bg="#2d2d44", highlightthickness=0, troughcolor="#3b3b58", font=("Segoe UI", 9, "bold"))
arrsize_Entry.grid(row=1, column=2, padx=5, pady=5)

root.mainloop()
