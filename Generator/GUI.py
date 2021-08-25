import tkinter as tk

class GUI:
	def __init__(self, root):
		self.root = root

		# Basic settings for the window
		self.root.title("Covid-19 QR-Code Generator")
		self.root.geometry("600x400")
		self.root.configure(bg="#23272A")
		self.root.update()

		# Define all the tkinter frames
		self.input_field = input_field(self.root)
		self.radio_buttons = radio_buttons(self.root)
		self.output_buttons = output_buttons(self.root)


class input_field(tk.Frame):
	def __init__(self, root):
		gm = [int(root.winfo_width()), int(root.winfo_height())] #Window geometry
		self.frame = tk.Frame(root)

		width = gm[0] * 0.75
		height = gm[1] * 0.1
		x = gm[0] * 0.125
		y = gm[1] * 0.125

		self.frame.configure(bg="grey")
		self.frame.place(width=width, height=height, x=x, y=y)

		self.label = tk.Label(self.frame, bg="grey")
		self.label.pack(fill="both")

		self.input = PlaceholderEntry(master=self.label, placeholder='Full name or Date of Birth', borderwidth=0, justify="center")
		self.input.pack(fill="both")
		self.input.configure(font=("default", int(height*0.60), "bold"))


class radio_buttons(tk.Frame):
	def __init__(self, root):
		gm = [int(root.winfo_width()), int(root.winfo_height())] #Window geometry
		self.frame = tk.Frame(root)

		width = gm[0] * 0.5
		height = gm[1] * 0.2
		x = gm[0] * 0.25
		y = gm[1] * 0.25

		self.frame.configure(bg="#23272A")
		self.frame.place(width=width, height=height, x=x, y=y)

		self.input = tk.IntVar()
		binnenlands = tk.Radiobutton(self.frame, text="Binnenlands", variable=self.input, indicator=0, value=0)
		buitenlands = tk.Radiobutton(self.frame, text="Buitenlands", variable=self.input, indicator=0, value=1)

		binnenlands.pack(pady=2)
		buitenlands.pack(pady=2)

		binnenlands.configure(font=("default", 13, "bold"), width=int(gm[0]*0.1))
		buitenlands.configure(font=("default", 13, "bold"), width=int(gm[0]*0.1))


class output_buttons(tk.Frame):
	def __init__(self, root):
		gm = [int(root.winfo_width()), int(root.winfo_height())] #Window geometry
		self.frame = tk.Frame(root)

		width = gm[0] * 0.25
		height = gm[1] * 0.15
		x = gm[0] * (0.75 / 2)
		y = gm[1] * 0.5

		self.frame.configure(bg="grey")
		self.frame.place(width=width, height=height, x=x, y=y)

		self.to_img = tk.Button(self.frame, text="To IMG")
		self.to_pdf = tk.Button(self.frame, text="To PDF")

		self.to_img.configure(font=("default", 13, "bold"), width=int(gm[0]*0.1))
		self.to_pdf.configure(font=("default", 13, "bold"), width=int(gm[0]*0.1))

		self.to_img.pack()
		self.to_pdf.pack()


class PlaceholderEntry(tk.Entry):
    def __init__(self, master=None, placeholder='', cnf={}, fg='black',
                 fg_placeholder='grey50', *args, **kw):
        super().__init__(master, cnf={}, bg='white', *args, **kw)
        self.fg = fg
        self.fg_placeholder = fg_placeholder
        self.placeholder = placeholder
        self.bind('<FocusOut>', lambda event: self.fill_placeholder())
        self.bind('<FocusIn>', lambda event: self.clear_box())
        self.fill_placeholder()

    def clear_box(self):
        if not self.get() and super().get():
            self.config(fg=self.fg)
            self.delete(0, tk.END)

    def fill_placeholder(self):
        if not super().get():
            self.config(fg=self.fg_placeholder)
            self.insert(0, self.placeholder)
    
    def get(self):
        content = super().get()
        if content == self.placeholder:
            return ''
        return content