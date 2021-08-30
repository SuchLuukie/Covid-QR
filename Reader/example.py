import cv2
from cryptography.fernet import Fernet

image = cv2.imread("qrcode.png")

detector = cv2.QRCodeDetector()
data, vertices_array, binary_qrcode = detector.detectAndDecode(image)
print(data)

key = open("../KEYS/buitenlands.key", "rb").read()
f = Fernet(key)
data = f.decrypt(data.encode())
print(data)