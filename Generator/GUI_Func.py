import json

class GUI_Func:
	def __init__(self, app, qr):
		self.app = app
		self.qr = qr

		self.app.output_buttons.to_img.configure(command=self.to_img_event)
		self.app.output_buttons.to_pdf.configure(command=self.to_pdf_event)


	def to_img_event(self):
		info = self.get_info()
		
		message = self.get_from_db(info["input"])
		if message != None:
			self.qr.create_qr(info["binnen/buiten"] == 0 or info["binnen/buiten"] == "", message)


	def to_pdf_event(self):
		print(self.get_info())


	def get_info(self):
		info = {
			"input": self.app.input_field.input.get(),
			"binnen/buiten": self.app.radio_buttons.input.get()
		}
		return info


	def get_from_db(self, info):
		db = self.loadJSON()
		for item in db:
			full_name = item["Voornaam"] + " " + item["Achternaam"]
			if full_name.lower() == info.lower():
				return item

			if item["Geboortedatum"] == info:
				return item

		return None



	def loadJSON(self):
		with open("../database_personen.json", "r") as json_file:
			return json.load(json_file)