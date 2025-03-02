from tkinter import *
from tkinter import font

import time, tkinter.messagebox

gui = Tk()
gui.geometry("350x200")
gui.title("Stopwatch")
gui.config(background="gray97")
print(font.families())

hour = StringVar()
minute = StringVar()
second = StringVar()

hour.set("00")
minute.set("00")
second.set("00")

hour_entry = Entry(gui,bg="gray94", fg= "gray0", font=("Courier",18),width=5,textvariable=hour)
hour_entry.place(x=45 ,y=45)

minute_entry = Entry(gui,bg="gray94", fg= "gray0", font=("Courier",18),width=5,textvariable=minute)
minute_entry.place(x=145 ,y=45)

second_entry = Entry(gui,bg="gray94", fg= "gray0", font=("Courier",18),width=5,textvariable=second)
second_entry.place(x=245 ,y=45)

def start_timer():
    total= int(hour_entry.get()) * 3600 + int(minute_entry.get()) * 60 + int(second_entry.get())
    while total > -1:
        min,sec = divmod(total,60)
        hr= 00
        if min > 60:
            hr,min = divmod(min,60)
        hour.set("{:02d}".format(hr))
        minute.set("{:02d}".format(min))
        second.set("{:02d}".format(sec))
        gui.update()
        time.sleep(1)
        total -= 1
        #hour_entry.config(state='disabled')
        #minute_entry.config(state='disabled')
        #second_entry.config(state='disabled')
        b1.config(state='disabled')
        if total == 0:
            tkinter.messagebox.showinfo('Success!', 'Timer Complete')
            hour_entry.config(state='normal')
            minute_entry.config(state='normal')
            second_entry.config(state='normal')
            b1.config(state='normal')

b1 = Button(gui,highlightbackground="gray94",fg="gray0",text = "Start Timer",font=("Courier",20),width=10,command=start_timer)
b1.place(x=85 ,y=125)


gui.mainloop()