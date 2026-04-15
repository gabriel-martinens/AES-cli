import base64
import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

arquivo = sys.argv[1]
chave = sys.argv[2]
with open(arquivo) as f:
    arquivo = base64.b64decode(f.read())

cipher = AES.new(chave, AES.MODE_ECB)

descriptografado = unpad(cipher.decrypt(arquivo),16)

print(descriptografado.decode("utf-8"))
