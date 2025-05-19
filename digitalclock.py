import tkinter as tk
from time import strftime

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Set window background and size
root.configure(bg='black')
root.geometry("400x150")

# Create and configure the time label
label = tk.Label(root, font=('calibri', 50, 'bold'), background='black', foreground='cyan')
label.pack(anchor='center', pady=20)

# Define the function to update time
def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

# Call the function to update the clock
time()

# Run the GUI loop
root.mainloop()
