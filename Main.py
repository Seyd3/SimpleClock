import sys
import time
from tkinter import *


def times():
    current_time = time.strftime("%H:%M:%S")
    clock.config(text=current_time)
    clock.after(200, times)


root = Tk()
root.geometry("440x240")
root.title("Digitale Uhr")
root.wm_attributes("-topmost", 1)
clock = Label(root, font=("times", 50, "bold"), bg="#088A4B")
clock.grid(row=2, column=2, pady=25, padx=95)
times()

digi = Label(root, text="Digitale Uhr  ", font="times 25 bold", bg="#D7DF01")
digi.grid(row=0, column=2)

digi2 = Label(root, text="Von Seyd", font="times 12 bold", bg="#0489B1")
digi2.grid(row=1, column=2)

nota = Label(root, text="       Stunden     Minuten   Sekunden      ", font="times 15 bold", bg="#8A0808")
nota.grid(row=3, column=2)

root.mainloop()
