import json

class GUI_Func:
	def __init__(self, app):
		self.app = app

		self.app.buttons.binnenlands.configure(command=self.binnenlands_event)
		self.app.buttons.buitenlands.configure(command=self.buitenlands_event)

	def binnenlands_event(self):
		self.app.qr_i.is_binnenlands = True
		self.app.video.activate = True
		#self.app.video.video_feed()
		self.app.video.imitate_qr()


	def buitenlands_event(self):
		self.app.qr_i.is_binnenlands = False
		self.app.video.activate = True
		#self.app.video.video_feed()
		self.app.video.imitate_qr()


	def qr_detected(self, data, is_binnenlands):
		selected_country = self.app.countries.listbox.get("active")
		print(selected_country)
		print(is_binnenlands)

		self.binnenlandse_criteria_check(data)


	def binnenlandse_criteria_check(self, data):
		countries = self.get_country_db()
		nederland = [country for country in countries if country["EU-Land"]=="Nederland"][0]
		print(nederland)


	def get_country_db(self):
		with open("../database_landen.json", "r") as json_file:
			return json.load(json_file)