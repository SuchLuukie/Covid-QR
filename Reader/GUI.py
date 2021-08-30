import cv2
import tkinter as tk
from PIL import ImageTk, Image

class GUI:
	def __init__(self, root):
		self.root = root

		# Basic settings for the window
		self.root.title("Covid-19 QR-Code Reader")
		self.root.geometry("800x600")
		self.root.configure(bg="#23272A")
		self.root.update()

		# Define all the tkinter frames
		self.video = video(self.root)


class video(tk.Frame):
	def __init__(self, root):
		self.capture = cv2.VideoCapture(0)

		gm = [int(root.winfo_width()), int(root.winfo_height())] #Window geometry
		self.frame = tk.Frame(root)

		width = gm[0] * 0.75
		height = gm[1] * 0.75
		x = gm[0] * 0.125
		y = gm[1] * 0.125

		self.frame.configure(bg="grey")
		self.frame.place(width=width, height=height, x=x, y=y)

		self.label = tk.Label(self.frame, bg="grey")
		self.label.pack(fill="both")


	def video_feed(self):
		_, frame = self.capture.read()
		print(frame)
		cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
		img = Image.fromarray(cv2image)
		imgtk = ImageTk.PhotoImage(image=img)
		self.label.imgtk = imgtk
		self.label.configure(image=imgtk)
		self.label.after(1, self.video_stream) 