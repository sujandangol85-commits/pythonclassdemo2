import tkinter as tk
import random
import time

# Setup
root = tk.Tk()
root.title("Catch the Dot")
root.geometry("600x600")
root.config(bg="#121212")

score = 0
start_time = time.time()
game_duration = 30  # seconds

canvas = tk.Canvas(root, width=600, height=500, bg="#1e1e1e", highlightthickness=0)
canvas.pack(pady=20)

score_label = tk.Label(root, text="Score: 0", font=("Helvetica", 16), bg="#121212", fg="#00ff88")
score_label.pack()

timer_label = tk.Label(root, text="Time: 30", font=("Helvetica", 16), bg="#121212", fg="#ffcc00")
timer_label.pack(pady=5)

dot = None

# Create new dot at random position
def create_dot():
    global dot
    if time.time() - start_time >= game_duration:
        canvas.delete("all")
        timer_label.config(text="Time: 0")
        score_label.config(text=f"Final Score: {score}")
        return
    canvas.delete("all")
    x = random.randint(50, 550)
    y = random.randint(50, 450)
    dot = canvas.create_oval(x, y, x+30, y+30, fill="#00ff00", outline="")  # green dot
    canvas.tag_bind(dot, "<Button-1>", dot_clicked)

# When dot is clicked
def dot_clicked(event):
    global score
    score += 1
    score_label.config(text=f"Score: {score}")
    create_dot()

# Update timer every second
def update_timer():
    elapsed = int(time.time() - start_time)
    remaining = max(0, game_duration - elapsed)
    timer_label.config(text=f"Time: {remaining}")
    if remaining > 0:
        root.after(1000, update_timer)

# Start game
create_dot()
update_timer()

# Start GUI loop
root.mainloop()
