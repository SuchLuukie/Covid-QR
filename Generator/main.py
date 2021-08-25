# Import libraries
import tkinter as tk

# Import files
from GUI import GUI
from GUI_Func import GUI_Func
from QR import QR

def main():
	root = tk.Tk()

	qr = QR()
	app = GUI(root)
	gui_func = GUI_Func(app, qr)

	root.mainloop()


if __name__ == "__main__":
	main()