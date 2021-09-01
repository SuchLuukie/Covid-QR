import json

class GUI_Func:
	def __init__(self, app):
		self.app = app
		self.qr_i = self.app.qr_i

		self.app.buttons.binnenlands.configure(command=self.binnenlands_event)
		self.app.buttons.buitenlands.configure(command=self.buitenlands_event)

		self.app.video.video_feed()


	def binnenlands_event(self):
		self.qr_i.is_binnenlands = True
		self.app.video.activate = True
		self.app.video.video_feed()


	def buitenlands_event(self):
		self.qr_i.is_binnenlands = False
		self.app.video.activate = True
		self.app.video.video_feed()


	def qr_detected(self, data):
		self.binnenlandse_criteria_check(data)


	def binnenlandse_criteria_check(self, data):
		countries = self.get_country_db()
		nederland = [country for country in countries if country["EU-Land"]=="Nederland"][0]
		print(nederland)


	def get_country_db(self):
		with open("../database_landen.json", "r") as json_file:
			return json.load(json_file)