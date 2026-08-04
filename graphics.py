from tkinter import *
from tkinter import ttk
from grid import Grid

class TkinterWindow:
    def __init__(self, root):
#start the tkinter window
        root.title("Conway's Game of Life")

    def grid_size_entry_window(self):
#open the initial frame to get users desired x and y grid size
        grid_size_entry_frame = ttk.Frame(root)
        grid_size_entry_frame.grid(column=0, row=0, sticky=(NSEW))

#create entry fields for x and y size
        self.size_x = StringVar()
        size_x_entry = ttk.Entry(grid_size_entry_frame, width=7, textvariable=self.size_x)
        size_x_entry.grid(column=1, row=2, sticky=(W, E))

        self.size_y = StringVar()
        size_y_entry = ttk.Entry(grid_size_entry_frame, width=7, textvariable=self.size_y)
        size_y_entry.grid(column=3, row=2, sticky=(W, E))

#label the entry fields
        ttk.Label(grid_size_entry_frame, text="Enter size X").grid(column=1, row=1, sticky=W)
        ttk.Label(grid_size_entry_frame, text="Enter size Y").grid(column=3, row=1, sticky=E)

#create the start button
        ttk.Button(grid_size_entry_frame, text="Open Grid", command=self.create_grid).grid(column=2, row=3, sticky=(NSEW))

        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        grid_size_entry_frame.columnconfigure(2, weight=1)

        for child in grid_size_entry_frame.winfo_children():
            child.grid_configure(padx=5, pady=5)

        size_x_entry.focus()
        root.bind("<Return>", self.create_grid)

    def create_grid(self):
        self.cell_grid = Grid(self.size_x, self.size_y)

root = Tk()
TkinterWindow(root)
root.mainloop()
