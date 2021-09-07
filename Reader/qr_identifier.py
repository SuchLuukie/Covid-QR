import cv2
import json
from pyzbar.pyzbar import decode
import cryptography
from cryptography.fernet import Fernet

class qr_identifier:
	def __init__(self, app):
		self.app = app
		self.is_binnenlands = True
				

	def identify_qr(self, image):
		gray_img = cv2.cvtColor(image,0)
		barcode = decode(gray_img)

		for obj in barcode:
			barcodeData = obj.data
			decrypted_data = self.decrypt(barcodeData)
			if decrypted_data is None:
				return False

			json_data = json.loads(decrypted_data)
			self.app.gui_func.qr_detected(json_data, self.is_binnenlands)

			return True

		return False


	def decrypt(self, data):
		if self.is_binnenlands:
			key = open("../KEYS/binnenlands.key", "rb").read()

		else:
			key = open("../KEYS/buitenlands.key", "rb").read()

		try:
			f = Fernet(key)
			return f.decrypt(data)

		except cryptography.fernet.InvalidToken:
			return None