import cv2
import json
import tkinter as tk
from PIL import ImageTk, Image

from qr_identifier import qr_identifier
from GUI_Func import GUI_Func

class GUI:
	def __init__(self, root):
		self.root = root

		# Basic settings for the window
		self.root.title("Covid-19 QR-Code Reader")
		self.root.geometry("800x800")
		self.root.configure(bg="#23272A")
		self.root.update()

		# Define all the tkinter frames
		self.video = video(self.root, self)
		self.buttons = buttons(self.root)
		self.countries = countries(self.root)

		self.qr_i = qr_identifier(self)
		self.gui_func = GUI_Func(self)

		self.video.imitate_qr()


class countries(tk.Frame):
	def __init__(self, root):
		gm = [int(root.winfo_width()), int(root.winfo_height())] #Window geometry
		self.frame = tk.Frame(root)
		self.all_countries()

		width = gm[0] * 0.15
		height = gm[1] * 0.1
		x = gm[0] * (0.75 / 4 * 3) + 0.2
		y = gm[1] * 0.85

		self.frame.configure(bg="grey")
		self.frame.place(width=width, height=height, x=x, y=y)

		self.listbox = tk.Listbox(self.frame, listvariable=self.country_list)
		self.listbox.pack()

		self.scrollbar = tk.Scrollbar(self.frame)
		self.scrollbar.pack(side = "right", fill = "both")

		self.listbox.config(yscrollcommand = self.scrollbar.set)
		self.scrollbar.config(command = self.listbox.yview)


	def all_countries(self):
		with open("../database_landen.json", "r") as json_file:
			countries = json.load(json_file)

		self.country_list = tk.StringVar(value=[country["EU-Land"] for country in countries])


class buttons(tk.Frame):
	def __init__(self, root):
		gm = [int(root.winfo_width()), int(root.winfo_height())] #Window geometry
		self.frame = tk.Frame(root)

		width = gm[0] * 0.25
		height = gm[1] * 0.1
		x = gm[0] * (0.75 / 4)
		y = gm[1] * 0.85

		self.frame.configure(bg="#23272A")
		self.frame.place(width=width, height=height, x=x, y=y)

		self.binnenlands = tk.Button(self.frame, text="Binnenlands")
		self.buitenlands = tk.Button(self.frame, text="Buitenlands")

		self.binnenlands.configure(font=("default", 13, "bold"), width=int(gm[0]*0.1))
		self.buitenlands.configure(font=("default", 13, "bold"), width=int(gm[0]*0.1))

		self.binnenlands.pack()
		self.buitenlands.pack()


class video(tk.Frame):
	def __init__(self, root, app):
		self.capture = cv2.VideoCapture(0)
		self.app = app
		self.activate = True

		gm = [int(root.winfo_width()), int(root.winfo_height())] #Window geometry
		self.frame = tk.Frame(root)

		self.width = round(gm[0] * 0.85)
		self.height = round(gm[1] * 0.75)
		x = gm[0] * (0.125 / 2)
		y = gm[1] * (0.125 / 2)

		self.frame.configure(bg="grey")
		self.frame.place(width=self.width, height=self.height, x=x, y=y)

		self.label = tk.Label(self.frame, bg="grey")
		self.label.pack(fill="both")


	def imitate_qr(self):
		cv2image = cv2.imread("../qrcode.png", cv2.COLOR_BGR2RGBA)
		img = Image.fromarray(cv2image).resize((self.width, self.height), Image.ANTIALIAS)
		imgtk = ImageTk.PhotoImage(image=img)

		self.label.image = imgtk
		self.label.configure(image=imgtk)

		self.activate = not self.app.qr_i.identify_qr(cv2image)


	def video_feed(self):
		ok, frame = self.capture.read()
		if ok:
			cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

			img = Image.fromarray(cv2image).resize((self.width, self.height), Image.ANTIALIAS)
			imgtk = ImageTk.PhotoImage(image=img)

			self.label.image = imgtk
			self.label.configure(image=imgtk)

			self.activate = not self.app.qr_i.identify_qr(cv2image)

		if self.activate:
			self.label.after(1, self.video_feed)