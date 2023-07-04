from tkinter import  *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
# Number of reps(work, breaks are together in reps)
reps = 10
# Checkmarks
checkmark = ""
# Timer
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
# Function for reset in pomodoro
def reset_timer():
    # Cancel timer
    window.after_cancel(timer)

    # Set default text for timer label
    timer_label.config(text="Timer")

    # Set default text for checkmarks
    checkmark_label.config(text="")

    # Set default value for timer
    canvas.itemconfig(timer_text, text="00:00")

    # Set default value for reps(10)
    global reps
    reps = 10


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    # Calculate seconds from minute for current session
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # Set up seconds for session(work, short break, long break) and change title
    if reps == 8:
        count_down(long_break_sec)
        timer_label.config(text="Long break", fg=PINK)

    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Short break", fg=RED)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global checkmark

    # Set up seconds and minutes
    count_min = math.floor(count / 60)
    count_sec = math.floor(count % 60)

    # Adding 0 if seconds or minutes are smaller than 10
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    # Draw it(minutes, seconds) on canvas
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    # The main idea of counting down
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        # Start again
        start_timer()
        # Adding checkmark after complated work
        if reps % 2 == 0:
            checkmark += "✔"
            checkmark_label.config(text=f"{checkmark}", fg=GREEN)


# ---------------------------- UI SETUP ------------------------------- #
# The main window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Green text Timer
timer_label = Label(text="Timer", font=("Arial", 45, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
timer_label.grid(column=1, row=0)

# Picture of tomato
# highlightthickness=0 without border
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_picture = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_picture)
timer_text =canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Start button
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

# Reset button
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

# Green text checkmark
checkmark_label = Label(text="", font=("Arial", 15, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
checkmark_label.grid(column=1, row=3)

window.mainloop()