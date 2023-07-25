import tkinter as tk
from time import strftime
def digiClock(): 
    current_time = strftime('%H:%M:%S %p')
    current_date = strftime('%d %B, %Y')
    time_var.set(current_time)
    date_var.set(current_date)
    root.after(1000, digiClock)
root = tk.Tk()
root.title('digiClock')
root.configure(bg='black', border='10')
clock_font = ('Courier', 30, 'bold')
date_font = ('Courier', 20, 'italic', 'bold')
time_var = tk.StringVar()
date_var = tk.StringVar()
label_time = tk.Label(root, font=clock_font, bg='black', fg='cyan', textvariable=time_var)
label_time.pack(anchor='center')
label_date = tk.Label(root, font=date_font, bg='black', fg='lightgreen', textvariable=date_var)
label_date.pack()
digiClock()
root.mainloop() 