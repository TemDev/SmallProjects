from tkinter import *

w, h = 1000, 800  # map(int, input("Enter width height").split())
list_of_widgets = []
list_of_all = []
Selected = None
raised_frame = None
Selected_shape = None
list_of_shapes = []


class AdvancedEntry(Entry):
    def __init__(self, container, info, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.bind('<Return>', self._add_config)
        self.info = info

    def _add_config(self, e):
        if raised_frame == label_frame:
            if Selected:
                raised_frame.final_label.config(text="")
                if self.info == "text":
                    Selected.config(text=self.get())
                elif self.info == "colour":
                    try:
                        Selected.config(bg=self.get())
                    except TclError:
                        raised_frame.final_label.config(text="The colour config is wrong :(")
                elif self.info == "bd":
                    try:
                        Selected.config(bd=self.get())
                    except TclError:
                        raised_frame.final_label.config(text="Numbers please ;) at border")
                elif self.info == "tc":
                    try:
                        Selected.config(fg=self.get())
                    except TclError:
                        raised_frame.final_label.config(text="Dumb input")
                elif self.info == "wl":
                    try:
                        Selected.config(wraplength=self.get())
                    except TclError:
                        raised_frame.final_label.config(text="Dumb input")
                elif self.info == "ul":
                    try:
                        Selected.config(underline=self.get())
                    except TclError:
                        raised_frame.final_label.config(text="Dumb input")
        elif raised_frame == button_frame:
            if Selected:
                raised_frame.final_label.config(text="")
                if self.info == "colour":
                    try:
                        Selected.config(bg=self.get())
                        raised_frame.final_label.config(text="Unfortunately, macOS does not support button colours")
                    except TclError:
                        raised_frame.final_label.config(text="The colour config is wrong :(")
                elif self.info == "bd":
                    try:
                        Selected.config(bd=self.get())
                        raised_frame.final_label.config(text="Neither does it support border widths :(")
                    except TclError:
                        raised_frame.final_label.config(text="Numbers please ;)")
        elif raised_frame == canvas_frame:
            if self.info == "colour":
                try:
                    Selected.config(bg=self.get())
                except TclError:
                    raised_frame.final_label.config(text="The colour config is wrong :(")
            elif self.info == "bd":
                try:
                    Selected.config(bd=self.get())
                except TclError:
                    raised_frame.final_label.config(text="Numbers please ;)")
            elif self.info == "draw":
                x1, y1, x2, y2 = map(int, self.get().split())
                if Selected_shape == "line":
                    line = Selected.create_line(x1, y1, x2, y2, fill="black")
                    list_of_shapes.append(line)


class Labelpage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='#D3DEED')
        #  self.pack(side=TOP, fill=BOTH, expand=1)
        self.grid(row=0, column=0, sticky="NESW")
        self.controller = controller
        label1 = Label(self, text="Text:")
        label1.pack(side="top", pady=10)
        entry1 = AdvancedEntry(self, "text")
        entry1.pack(side="top", pady=10)
        label2 = Label(self, text="Colour")
        label2.pack(side="top", pady=10)
        entry2 = AdvancedEntry(self, "colour")
        entry2.pack(side="top", pady=10)
        label3 = Label(self, text="Border")
        label3.pack(side="top", pady=10)
        entry3 = AdvancedEntry(self, "bd")
        entry3.pack(side="top", pady=10)
        label4 = Label(self, text="Text-Color")
        label4.pack(side="top", pady=10)
        entry4 = AdvancedEntry(self, "tc")
        entry4.pack(side="top", pady=10)
        label5 = Label(self, text="WrapLength")
        label5.pack(side="top", pady=10)
        entry5 = AdvancedEntry(self, "wl")
        entry5.pack(side="top", pady=10)
        label6 = Label(self, text="UnderLine")
        label6.pack(side="top", pady=10)
        entry6 = AdvancedEntry(self, "ul")
        entry6.pack(side="top", pady=10)
        self.final_label = Label(self)
        self.final_label.pack(side="top", pady=20)


class Buttonpage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='#C0B3F7')
        #  self.pack(fill=BOTH, expand=1)
        self.grid(row=0, column=0, sticky="NESW")
        self.controller = controller
        label1 = Label(self, text="Colour")
        label1.pack(side="top", pady=10)
        entry1 = AdvancedEntry(self, "colour")
        entry1.pack(side="top", pady=10)
        label2 = Label(self, text="Border")
        label2.pack(side="top", pady=10)
        entry2 = AdvancedEntry(self, "bd")
        entry2.pack(side="top", pady=10)
        self.final_label = Label(self)
        self.final_label.pack(side="top", pady=20)


def line_action():
    global Selected_shape
    Selected_shape = "line"


def circle_action():
    global Selected_shape
    Selected_shape = "circle"


def arc_action():
    global Selected_shape
    Selected_shape = "arc"


def polygon_action():
    global Selected_shape
    Selected_shape = "polygon"


class Canvaspage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='#DF8BA5', width=300, height=1000)
        #  self.pack(fill=BOTH, expand=1)
        self.grid(row=0, column=0, sticky="NESW")
        self.controller = controller
        label1 = Label(self, text="Colour")
        label1.pack(side="top", pady=10)
        entry1 = AdvancedEntry(self, "colour")
        entry1.pack(side="top", pady=10)
        label2 = Label(self, text="Border")
        label2.pack(side="top", pady=10)
        entry2 = AdvancedEntry(self, "bd")
        entry2.pack(side="top", pady=10)
        radiobutton_variable = IntVar()
        Radiobutton(self, text="Line      ", variable=radiobutton_variable, value=1, bg="black",
                    command=line_action).pack(side="top")
        Radiobutton(self, text="Circle   ", variable=radiobutton_variable, value=2, bg="black",
                    command=circle_action).pack(side="top")
        Radiobutton(self, text="Arc        ", variable=radiobutton_variable, value=3, bg="black",
                    command=arc_action).pack(side="top")
        Radiobutton(self, text="Polygon", variable=radiobutton_variable, value=4, bg="black",
                    command=polygon_action).pack(side="top")
        label3v1 = Label(self, text="x0 y0 x2 y2 x3 y3...")
        label3v1.pack(side="top", pady=10)
        entry3v1 = AdvancedEntry(self, "draw")
        entry3v1.pack(side="top", pady=10)
        self.final_label = Label(self)
        self.final_label.pack(side="top", pady=20)


class Startingwidgets:

    def __init__(self, widget):
        self.widget = widget
        self.widget.bind('<Button-1>', self.on_press)
        self.widget.pack(padx=20, pady=30, side=TOP)
        self.dict_of_types = {label: Label, button: Button, canvas: Canvas}
        list_of_widgets.append(self.widget)

    def on_press(self, event):
        new_widget = self.dict_of_types[self.widget](parent)
        DraggableWidgets(new_widget)
        list_of_all.append(new_widget)


class DraggableWidgets:
    def __init__(self, widget):
        self.widget = widget
        self.constant = [w // 2, h // 2]
        self.widget.place(x=w // 2, y=h // 2)
        self.widget.bind('<Button-1>', self.on_press)
        self.widget.bind('<B1-Motion>', self.on_motion)
        self.widget.bind('<ButtonRelease-1>', self.on_release)

    def on_press(self, event):
        self.color = self.widget["bg"]
        self.widget.configure(bg='#E796B3')
        global Selected, raised_frame
        Selected = self.widget
        frame = stack_list[self.widget.__class__.__name__]
        raised_frame = frame
        frame.tkraise()
        pass

    def on_motion(self, event):
        pass

    def on_release(self, event):
        self.widget.configure(bg=self.color)
        self.constant[0] += event.x
        self.constant[1] += event.y
        self.widget.place(x=self.constant[0], y=self.constant[1])
        pass


class SelectableFrames:
    def __init__(self, widget):
        self.constant = None
        self.widget = widget
        self.widget.bind('<Button-1>', self.on_press)
        self.widget.bind('<B1-Motion>', self.on_motion)
        self.widget.bind('<ButtonRelease-1>', self.on_release)

    def on_press(self, event):
        self.color = self.widget["bg"]
        self.widget.configure(bg='#E796B3')
        global parent, raised_frame
        parent = self.widget
        frame = stack_list[self.widget.__class__.__name__]
        raised_frame = frame
        frame.tkraise()
        pass

    def on_motion(self, event):
        pass

    def on_release(self, event):
        if parent != gui_frame:
            self.widget.configure(bg=self.color)
            self.constant[0] += event.x
            self.constant[1] += event.y
            self.widget.place(x=self.constant[0], y=self.constant[1])
            pass


root = Tk()
root.title("Simpleton")
root.wm_attributes('-fullscreen', 'true')
# Good colours: 5E7703, 29bdc1
root.configure(background='#29bdc1')

# WIDGET FRAME, LEFTMOST
widget_frame = Frame(root, bg='darkblue', width=300, height=1000)
widget_frame.pack(padx=10, pady=20, side=LEFT)
widget_frame.pack_propagate(0)

# GUI FRAME, CENTRE
gui_frame = Frame(root, bg='darkblue', width=w, height=h)
gui_frame.pack(side=LEFT, expand=True)
gui_frame.pack_propagate(0)

# OPTIONS FRAME, RIGHTMOST
options_frame = Frame(root, bg='darkblue', width=300, height=1000)
options_frame.pack(padx=10, pady=20, side=LEFT)
options_frame.grid_rowconfigure(0, weight=1)
options_frame.grid_columnconfigure(0, weight=1)
#  options_frame.pack_propagate(0)
options_frame.grid_propagate(0)
parent = gui_frame

# Currently, available widgets
label = Label(widget_frame, text="Press to create a label")
button = Label(widget_frame, text="Press to create a button")
canvas = Label(widget_frame, text="Press to create a canvas")

widget1 = Startingwidgets(label)
widget2 = Startingwidgets(button)
widget3 = Startingwidgets(canvas)

# Stack of Frames
label_frame = Labelpage(options_frame, controller=root)
button_frame = Buttonpage(options_frame, controller=root)
canvas_frame = Canvaspage(options_frame, controller=root)

stack_list = {'Label': label_frame, 'Button': button_frame, 'Canvas': canvas_frame}

root.mainloop()
