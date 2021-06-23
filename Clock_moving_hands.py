import tkinter as tk
import math
import datetime


class Clock:
    def __init__(self, root, timezone=0):
        self.root = root
        self.my_canvas = tk.Canvas(self.root, bg="blue", height=340, width=340)
        oval = self.my_canvas.create_oval(10, 10, 330, 330, fill='darkblue')
        self.label_cords = []
        self.label_cords2 = []
        self.label_cords3 = []
        now = datetime.datetime.now()
        self.counter_seconds = now.second * 100
        self.counter_minutes = now.minute * 100 * 60 + now.second * 100
        self.counter_hours = (now.hour + timezone) * 3600 * 100 + now.minute * 100 * 60 + now.second * 100
        self.seconds_arrow = None
        self.minutes_arrow = None
        self.hours_arrow = None
        for i in range(12):
            x = 170 + 160 * math.cos((2 * math.pi * i - 6 * math.pi) / 12)
            y = 170 + 160 * math.sin((2 * math.pi * i - 6 * math.pi) / 12)
            self.label_cords.append((x, y))
        for i in range(72):
            x2 = 170 + 120 * math.cos((2 * math.pi * i - 18 * math.pi) / 36)
            y2 = 170 + 120 * math.sin((2 * math.pi * i - 18 * math.pi) / 36)
            x3 = 170 + 160 * math.cos((2 * math.pi * i - 18 * math.pi) / 36)
            y3 = 170 + 160 * math.sin((2 * math.pi * i - 18 * math.pi) / 36)
            self.label_cords2.append((x2, y2))
            self.label_cords3.append((x3, y3))
        for i in range(len(self.label_cords)):
            label = tk.Label(self.my_canvas, text=i)
            line = self.my_canvas.create_line(170, 170, self.label_cords[i][0], self.label_cords[i][1])
            label.place(x=self.label_cords[i][0]-5, y=self.label_cords[i][1]-5)
        self.my_canvas.pack(side=tk.LEFT)
        self.my_canvas.after(1000, self.time_pass)
        self.lines = []
        self.animate = False
        self.rainbow = ['red', 'orange', 'yellow', 'green', 'blue', '#3333FF', 'violet']

        for i in range(len(self.label_cords2)):
            line2 = self.my_canvas.create_line(self.label_cords2[i][0], self.label_cords2[i][1], self.label_cords3[i][0],
                                               self.label_cords3[i][1], fill='white')
            self.lines.append(line2)

    def time_pass(self):
        if self.seconds_arrow:
            self.my_canvas.delete(self.seconds_arrow)
            self.my_canvas.delete(self.minutes_arrow)
            self.my_canvas.delete(self.hours_arrow)
        self.counter_seconds += 1
        self.counter_minutes += 1
        self.counter_hours += 1
        if self.counter_seconds % 6000 == 0:
            self.counter = 0
            self.animation()
            self.counter_seconds %= 6000

        self.counter_minutes %= 360000
        self.counter_hours %= 4320000

        x1 = 170 + 160 * math.cos((2 * math.pi * self.counter_seconds - 3000 * math.pi) / 6000)
        y1 = 170 + 160 * math.sin((2 * math.pi * self.counter_seconds - 3000 * math.pi) / 6000)
        x2 = 170 + 130 * math.cos((2 * math.pi * self.counter_minutes - 180000 * math.pi) / 360000)
        y2 = 170 + 130 * math.sin((2 * math.pi * self.counter_minutes - 180000 * math.pi) / 360000)
        x3 = 170 + 80 * math.cos((2 * math.pi * self.counter_hours - 2160000 * math.pi) / 4320000)
        y3 = 170 + 80 * math.sin((2 * math.pi * self.counter_hours - 2160000 * math.pi) / 4320000)
        self.seconds_arrow = self.my_canvas.create_line(170, 170, x1, y1, fill='red', arrow='last', arrowshape=(20, 40, 10))
        self.minutes_arrow = self.my_canvas.create_line(170, 170, x2, y2, fill='green', arrow='last', arrowshape=(16, 30, 8))
        self.hours_arrow = self.my_canvas.create_line(170, 170, x3, y3, fill='purple', arrow='last', arrowshape=(10, 18, 5))
        self.my_canvas.after(10, self.time_pass)

    def animation(self):
        for i in self.lines:
            self.my_canvas.delete(i)
        for i in range(72):
            x2 = 170 + (120 - self.counter) * math.cos((2 * math.pi * i - 18 * math.pi) / 36)
            y2 = 170 + (120 - self.counter) * math.sin((2 * math.pi * i - 18 * math.pi) / 36)
            x3 = 170 + (160 - self.counter) * math.cos((2 * math.pi * i - 18 * math.pi) / 36)
            y3 = 170 + (160 - self.counter) * math.sin((2 * math.pi * i - 18 * math.pi) / 36)
            line2 = self.my_canvas.create_line(x2, y2, x3, y3, fill=self.rainbow[self.counter % 7])
            self.lines.append(line2)
        self.counter += 1
        if self.counter == 120:
            for i in self.lines:
                self.my_canvas.delete(i)
            for i in range(len(self.label_cords2)):
                line2 = self.my_canvas.create_line(self.label_cords2[i][0], self.label_cords2[i][1],
                                                       self.label_cords3[i][0],
                                                       self.label_cords3[i][1], fill='white')
                self.lines.append(line2)
        else:
            self.my_canvas.after(20, self.animation)

    def animation2(self):
        pass



root = tk.Tk()
my_gui = Clock(root)
my_gui2 = Clock(root, 6)
tk.mainloop()
