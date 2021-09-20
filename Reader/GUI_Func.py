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
		countries = self.get_country_db()

		if is_binnenlands:
			country = [country for country in countries if country["EU-Land"]=="Nederland"][0]

		else:
			country = [country for country in countries if country["EU-Land"]==selected_country][0]

		check = self.criteria_check(country, data)



	def criteria_check(self, country, data):
		vac_check = self.vaccination_checK(country, data)

		print(country)
		print(data)

	def vaccination_checK(country, data):
		total_vaccinations = 0
		if "-" in data["Vac1"] or data["Vac1"] == "VOLDAAN":
			total_vaccinations += 1

		if "-" in data["Vac2"] or data["Vac2"] == "VOLDAAN":
			total_vaccinations += 1

		vac_required = 0


		if country["Accepteerd PCR test als alternatief voor 1 vaccinatie?"]:
			if len(country["Minimaal aantal vaccinaties nodig"]) == 4:
				return


	def get_country_db(self):
		with open("../database_landen.json", "r") as json_file:
			return json.load(json_file)


	def trigger_red(self):
		print("RED")


	def trigger_green(self):
		print("GREEN")