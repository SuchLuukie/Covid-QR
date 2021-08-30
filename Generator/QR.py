# Import libraries
import json
import qrcode
from cryptography.fernet import Fernet

class QR:
	def create_qr(self, binnenlands, info):
		info = json.dumps(info)
		encrypted_info = self.encrypt(binnenlands, info)
		img = qrcode.make(encrypted_info)

		print(encrypted_info)
		img.save("qrcode.png")


	def encrypt(self, binnenlands, info):
		key = self.get_key(binnenlands)
		f = Fernet(key)

		return f.encrypt(info.encode())

	# If wrong key it raises invalidtoken error and means that the qrcode is meant for the opposite key
	def decrypt(self, binnenlands, encrypted_info):
		key = self.get_key(binnenlands)
		f = Fernet(key)

		return f.decrypt(encrypted_info).decode()


	def get_key(self, binnenlands):
		if binnenlands:
			string = "../KEYS/binnenlands"
		else:
			string = "../KEYS/buitenlands"

		return open(f"{string}.key", "rb").read()