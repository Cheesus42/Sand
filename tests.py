import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    root.after(1000, update_time)  # Schedule the function to be called again after 1 second

root = tk.Tk()
root.title("Clock")

label = tk.Label(root, font=("Arial", 30))
label.pack()

update_time()  # Start the update loop

root.mainloop()
