import tkinter as tk
import os

window = tk.Tk()
window.title("Button click game")
window.geometry('500x500')
window.resizable(False, False)
window.configure(bg='#ffc2ec')

icon = tk.PhotoImage(file='icon.png')
window.iconphoto(True, icon)

if not os.path.exists('save'):
    with open('save', "w") as save:
        save.write("0")

with open("save") as save:
	click_count = int(save.read())

def click():
	global click_count
	click_count+=1
	ccdisplay.config(text="Click count: " + str(click_count))
	with open("save", "w") as save:
		save.write(str(click_count))

def ccreset():
	global click_count
	click_count = 0
	ccdisplay.config(text="Click count: " + str(click_count))
	with open("save", "w") as save:
		save.write(str(click_count))

clickbutton = tk.Button(
	text="Click me!",
	font="Arial, 30",
	padx=5,
	pady=57,
	command=click
	)

resetbutton = tk.Button(
	text="Reset click count",
	font="Arial, 20",
	command=ccreset
	)

ccdisplay = tk.Label(
	text="Click count: " + str(click_count),
	font="Arial, 20"
	)

clickbutton.place(x=150, y=100)
resetbutton.place(relx=0.51, rely=0.581, anchor=tk.N)
ccdisplay.place(relx=0.5, rely=0.1, anchor=tk.N)
window.mainloop()