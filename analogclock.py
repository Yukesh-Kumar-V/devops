import tkinter as tk
import time
import math

# Create main window
root = tk.Tk()
root.title("Analog Clock")
root.resizable(False, False)

# Create a canvas
canvas_size = 400
canvas = tk.Canvas(root, width=canvas_size, height=canvas_size, bg='white')
canvas.pack()

# Clock center and radius
center_x = canvas_size // 2
center_y = canvas_size // 2
clock_radius = 180

# Draw clock face
def draw_clock_face():
    canvas.create_oval(center_x - clock_radius, center_y - clock_radius,
                       center_x + clock_radius, center_y + clock_radius,
                       width=4)
    
    for i in range(12):
        angle = math.radians(i * 30)
        x_inner = center_x + (clock_radius - 20) * math.sin(angle)
        y_inner = center_y - (clock_radius - 20) * math.cos(angle)
        x_outer = center_x + clock_radius * math.sin(angle)
        y_outer = center_y - clock_radius * math.cos(angle)
        canvas.create_line(x_inner, y_inner, x_outer, y_outer, width=2)

# Update hands every second
def update_clock():
    canvas.delete("hands")

    now = time.localtime()
    sec = now.tm_sec
    min = now.tm_min
    hr = now.tm_hour % 12

    # Angles in radians
    sec_angle = math.radians(sec * 6)
    min_angle = math.radians(min * 6 + sec * 0.1)
    hr_angle = math.radians((hr * 30) + (min * 0.5))

    # Hand lengths
    sec_len = clock_radius - 30
    min_len = clock_radius - 50
    hr_len = clock_radius - 80

    # Calculate end points for each hand
    def draw_hand(length, angle, width, color):
        x = center_x + length * math.sin(angle)
        y = center_y - length * math.cos(angle)
        canvas.create_line(center_x, center_y, x, y, width=width, fill=color, tags="hands")

    draw_hand(hr_len, hr_angle, 6, 'black')     # hour hand
    draw_hand(min_len, min_angle, 4, 'blue')    # minute hand
    draw_hand(sec_len, sec_angle, 2, 'red')     # second hand

    # Schedule next update
    root.after(1000, update_clock)

draw_clock_face()
update_clock()
root.mainloop()
