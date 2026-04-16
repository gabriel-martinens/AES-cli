import base64
import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad, pad

modo = sys.argv[1]
arquivo = sys.argv[2]
chave = sys.argv[3].encode()

with open(arquivo, "rb") as f:
    data = f.read()

cipher = AES.new(chave, AES.MODE_ECB)

if modo == "dec":
    data = base64.b64decode(data)
    resultado = unpad(cipher.decrypt(data), 16)
    print(resultado.decode("utf-8"))

elif modo == "enc":
    criptografado = cipher.encrypt(pad(data, 16))
    print(base64.b64encode(criptografado).decode())
