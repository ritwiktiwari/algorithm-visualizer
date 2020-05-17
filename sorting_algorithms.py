from tkinter import *
from tkinter import ttk
import random

# Main Window
root = Tk()
root.title("Sorting Algorithm Visualizer")
root.maxsize(900,600)
root.config(bg='black')

# Variables
selected_algorithm = StringVar()
data = []



def draw_data(data):
    canvas.delete('all')
    canvas_height = 380
    canvas_width = 600
    x_width = canvas_width / (len(data) + 1)
    offset = 20
    spacing = 10
    normalized_values = [i/max(data) for i in data]
    for i, height in enumerate(normalized_values):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height-height*340
        x1 = (i+1) * x_width + offset
        y1 = canvas_height

        canvas.create_rectangle(x0,y0,x1,y1, fill='red')
        canvas.create_text((x0+x1)//2,y0,anchor=SW, text=str(data[i]))

def generate():
    global data
    data = []
    min_val = int(min_entry.get())
    max_val = int(max_entry.get())
    size = int(size_entry.get())
    for _ in range(size):
        data.append(random.randrange(min_val, max_val+1))
    draw_data(data)
    print("Algorithm "+ selected_algorithm.get())

def start():
    global data
    
    print("Start")
    

# Frame
UI_FRAME = Frame(root, height=200, width=600, bg='grey')
UI_FRAME.grid(row=0, column=0, padx=10, pady=5)

# Canvas
canvas = Canvas(root, width=600, height=380, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)

# UI Area
# ROW:0
Label(UI_FRAME, text='Algorithm: ', bg='grey').grid(row=0, column=0, padx=5, pady=5, sticky=W)
algorithm_menu = ttk.Combobox(UI_FRAME, textvariable=selected_algorithm, values=['Bubble Sort', 'Merge Sort'])
algorithm_menu.grid(row=0, column=1, padx=5, pady=5, sticky=W)
algorithm_menu.current(0)
speed_scale = Scale(UI_FRAME, from_=0.1, to=2.0, length=200, digits=2, resolution=0.2, orient=HORIZONTAL, label='Select speed (seconds)')
speed_scale.grid(row=0, column=2, padx=5, pady=5)
Button(UI_FRAME, text="Start", command=start).grid(row=0, column=3, padx=5, pady=5)

# ROW:1
Label(UI_FRAME, text='Size: ', bg='grey').grid(row=1, column=0, padx=5, pady=5, sticky=W)
size_entry = Entry(UI_FRAME)
size_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

Label(UI_FRAME, text='Min Value: ', bg='grey').grid(row=1, column=2, padx=5, pady=5, sticky=W)
min_entry = Entry(UI_FRAME)
min_entry.grid(row=1, column=3, padx=5, pady=5, sticky=W)

Label(UI_FRAME, text='Max Value: ', bg='grey').grid(row=1, column=4, padx=5, pady=5, sticky=W)
max_entry = Entry(UI_FRAME)
max_entry.grid(row=1, column=5, padx=5, pady=5, sticky=W)
Button(UI_FRAME, text="Generate", command=generate).grid(row=1, column=6, padx=5, pady=5)


root.mainloop()

