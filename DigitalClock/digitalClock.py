import tkinter as Tk
import time

def update_clock():
	date = time.strftime("%d/%m/%Y")
	current_time = time.strftime("%H:%M:%S")
	date_time_text = date + " " + current_time

	clock_label.config(text=date_time_text)
	clock_label.after(1000, update_clock)

def main():
	global window, clock_label

	window = Tk.Tk()
	window.title("Digital Clock")

	clock_label = Tk.Label(window, font="Helventica 72 bold")
	clock_label.pack()

	update_clock()
	window.mainloop()

if __name__ == '__main__':
	main()