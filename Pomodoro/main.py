from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_reset = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_all() :
    window.after_cancel(timer_reset)
    timer_label.config(text='Timer',fg=GREEN)
    check_label.config(text='')
    canvas.itemconfig(timer_text,text='00:00')
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer():
    global reps
    reps  += 1
    work_seconds = WORK_MIN*60
    short_break_seconds = SHORT_BREAK_MIN*60
    long_break_seconds = LONG_BREAK_MIN*60
    if reps % 8 == 0 :
        timer_label.config(text='Break', fg='GREEN')
        countdown(long_break_seconds)
    elif reps % 2 == 0 :
        timer_label.config(text='Break', fg='PINK')
        countdown(short_break_seconds)
    else :
        timer_label.config(text='Time', fg='RED')
        countdown(work_seconds)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count) :
    minutes = int(count/60)
    seconds = count%60
    if seconds < 10 :
        seconds = '0' + str(seconds)
    if minutes < 10 :
        minutes = '0' + str(minutes)
    canvas.itemconfig(timer_text,text=f'{minutes}:{seconds}')
    if count > 0 :
       global timer_reset
       timer_reset = window.after(1000,countdown,count-1)
    else :
        timer()
        marks = ""
        sessions = int(reps/2)
        for _ in range(sessions) :
            marks += "✔"
        check_label.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=100,pady=50,bg=YELLOW)
window.title('POMODORO')

img = PhotoImage(file='tomato.png')
canvas = Canvas(height=230,width=210,bg=YELLOW,highlightthickness=0)
canvas.create_image(103,110,image=img)
timer_text = canvas.create_text(102,130,text='00:00',fill='white',font=(FONT_NAME,35,'bold'))
canvas.grid(column=1,row=1)

timer_label = Label(text='Timer',fg=GREEN,font=(FONT_NAME,50),bg=YELLOW)
timer_label.grid(column=1,row=0)

start_button = Button(text='Start',bg=YELLOW,highlightbackground=YELLOW)
start_button.grid(column=0,row=2)
start_button.config(command=timer)

reset_button = Button(text='Reset',bg=YELLOW,highlightbackground=YELLOW,command=reset_all)
reset_button.grid(column=2,row=2)

check_label = Label(fg=GREEN,bg=YELLOW)
check_label.grid(column=1,row=3)
window.mainloop()