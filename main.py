#!/usr/bin/env python3

import random
import tkinter as tk

def csv_reader(path):
    """
    Parse a csv file and return a random line.
    [str] path: path to the csv-file
    """
    with open(path) as file:
        lines = file.readlines()
        line = lines[random.randint(0, len(lines)-1)]
        return line

def handle_yes():
    lbl_compliment["text"] = "Så bra! Ha en fin dag videre ❤️"
    btn_no.destroy()
    btn_yes.destroy()
    btn_exit.pack(padx=10, pady=10)


def handle_no():
    compliment = csv_reader("kompliment.csv")
    lbl_compliment["text"] = f"{compliment}\nGår det bedre nå?"

def handle_exit():
    window.destroy()

window = tk.Tk()
window.title("Komplimentmaskinen")
window.columnconfigure(0, minsize=150, weight=1)
window.rowconfigure([0, 1], minsize=20, weight=1)

lbl_compliment = tk.Label(
    master=window,
    text="Velkommen til komplimentmaskinen! Har du det bra i dag?",
    width=50,
    height=10
)
lbl_compliment.grid(row=0, sticky="nsew")

frm_buttons = tk.Frame(
    master=window
)
frm_buttons.grid(row=1)

btn_no = tk.Button(
    master=frm_buttons,
    text="Nei",
    command=handle_no,
    width=10,
    height=2
)
btn_no.pack(side=tk.RIGHT, padx=10, pady=10)

btn_yes = tk.Button(
    master=frm_buttons,
    text="Ja",
    command=handle_yes,
    width=10,
    height=2
)
btn_yes.pack(side=tk.RIGHT, padx=10, pady=10)

btn_exit = tk.Button(
    master=frm_buttons,
    text="Avslutt",
    command=handle_exit,
    width=10,
    height=2
)

window.mainloop()
