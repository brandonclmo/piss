import math 
import sys 
import tkinter as tk 

root = tk.Tk()
root.title("piss")
root.geometry("400x300")

canvas = tk.Canvas(root, width=200, height=200, bg="white")
canvas.pack(pady=20)

canvas.create_text(100, 10, text="Cock", font=("Papyrus", 16))

# Draw stickman
canvas.create_oval(80, 30, 120, 70, outline="black", width=2)
canvas.create_line(100, 70, 100, 130, fill="black", width=2)
canvas.create_line(100, 90, 70, 110, fill="black", width=2)
canvas.create_line(100, 90, 130, 110, fill="black", width=2)
canvas.create_line(100, 130, 80, 170, fill="black", width=2)
canvas.create_line(100, 130, 120, 170, fill="black", width=2)
penar = canvas.create_line(100, 130, 103, 170, fill="black", width=4)
parabola = None
frame = 0

def draw_parabola(angle_rad):
    pee_x, pee_y = 103, 105
    points = []
    for x in range(0, 101, 2):
        y = 0.02 * x ** 2 + 30
        xr = x * math.cos(angle_rad) - y * math.sin(angle_rad)
        yr = x * math.sin(angle_rad) + y * math.cos(angle_rad)
        points.append((pee_x + xr, pee_y + yr))
    return points

# def animate():
    global parabola, frame
    amplitude = 0.5
    angle = math.cos(frame * 0.04) * amplitude
    if parabola:
        canvas.delete(parabola)
    pts = draw_parabola(angle)
    parabola = canvas.create_line(pts, fill="yellow", width=2, smooth=True)
    frame += 1
    root.after(30, animate)
def draw_penar():
    global penar, frame
    base_x, base_y = 100, 130 #Penar centre 
    length = 40
    angle = frame * 0.07
    # Calculate tip position
    tip_x = base_x + length * math.cos(angle)
    tip_y = base_y + length * math.sin(angle)
    # Remove old penar
    canvas.delete(penar)
    # Adds newer(and better) penar! 
    penar_new = canvas.create_line(base_x, base_y, tip_x, tip_y, fill="black", width=4)
    # Update reference
    globals()['penar'] = penar_new
    frame += 1
    root.after(30, draw_penar)

draw_penar()
root.mainloop()

