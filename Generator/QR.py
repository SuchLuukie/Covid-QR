# Import libraries
import json
import qrcode
from cryptography.fernet import Fernet

class QR:
	def create_qr(self, binnenlands_bool, info):
		info = json.dumps(info)
		encrypted_info = self.encrypt(binnenlands_bool, info)

		img = qrcode.make(encrypted_info)
		img.save("../qrcode.png")

	def encrypt(self, binnenlands_bool, info):
		key = self.get_key(binnenlands_bool)
		f = Fernet(key)

		return f.encrypt(info.encode())

	# If wrong key it raises invalidtoken error and means that the qrcode is meant for the opposite key
	def decrypt(self, binnenlands_bool, encrypted_info):
		key = self.get_key(binnenlands_bool)
		f = Fernet(key)

		return f.decrypt(encrypted_info).decode()


	def get_key(self, binnenlands_bool):
		if binnenlands_bool:
			string = "../KEYS/binnenlands"
		else:
			string = "../KEYS/buitenlands"

		return open(f"{string}.key", "rb").read()