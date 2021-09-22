import json
import datetime
from dateutil.relativedelta import relativedelta

class GUI_Func:
	def __init__(self, app):
		self.app = app

		self.app.buttons.binnenlands.configure(command=self.binnenlands_event)
		self.app.buttons.buitenlands.configure(command=self.buitenlands_event)

	def binnenlands_event(self):
		self.app.qr_i.is_binnenlands = True
		self.app.video.activate = True

		self.app.video.imitate_qr()

	def buitenlands_event(self):
		self.app.qr_i.is_binnenlands = False
		self.app.video.activate = True

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
		
		if vac_check:
			self.trigger_green()

		else:
			self.trigger_red()

		

	def vaccination_checK(self, country, data):
		bonus_vacs = 0
		vac_count = 0
		vac_type = data["Vaccin"]


		if "-" in data["Vac1"] or data["Vac1"] == "VOLDAAN":
			vac_count += 1

		if "-" in data["Vac2"] or data["Vac2"] == "VOLDAAN":
			vac_count += 1


		if country["Accepteerd PCR test als alternatief voor 1 vaccinatie?"] != False:
			# Time in hours, var might be True bool. in that case ignore time
			pcr_max_time_elapsed = country["Accepteerd PCR test als alternatief voor 1 vaccinatie?"]

			if pcr_max_time_elapsed != False:
				if data["Geldige PCR test?"] == True:
					bonus_vacs += 1

				elif data["Geldige PCR test?"] != False:
					time_since_pcr = data["Geldige PCR test?"]
					
					if pcr_max_time_elapsed > time_since_pcr:
						bonus_vacs += 1


		if country["Telt eerdere besmetting mee als 1 vaccinatie?"] != False:
			# Tiem in months, var might be True bool
			infection_max_time_elapsed = country["Telt eerdere besmetting mee als 1 vaccinatie?"]

			if infection_max_time_elapsed != False:
				if data["Positief getest"] != False:
					infection_date = datetime.datetime.fromisoformat(data["Positief getest"])
					max_date = datetime.datetime.now() - relativedelta(months=infection_max_time_elapsed)
					
					if not max_date > infection_date:
						bonus_vacs += 1


		# If true then it's multi optional
		if len(country["Minimaal aantal vaccinaties nodig"]) == 4:
			# See if viable for second option
			min_vacs = country["Minimaal aantal vaccinaties nodig"][2]
			min_vacs_types = country["Minimaal aantal vaccinaties nodig"][3]

			if vac_type in min_vacs_types:
				if vac_count + bonus_vacs >= min_vacs:
					return True

		min_vacs = country["Minimaal aantal vaccinaties nodig"][0]
		min_vacs_types = country["Minimaal aantal vaccinaties nodig"][1]

		if vac_type in min_vacs_types or min_vacs_types == "any":
			if vac_count + bonus_vacs >= min_vacs:
				return True

		return False


	def get_country_db(self):
		with open("../database_landen.json", "r") as json_file:
			return json.load(json_file)


	def trigger_red(self):
		self.app.root.configure(bg="#FF0000")


	def trigger_green(self):
		self.app.root.configure(bg="#00FF00")


	def trigger_pink(self):
		self.app.root.configure(bg="#FFC0CB")