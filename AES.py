import base64
import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad, pad

if len(sys.argv) < 3:
    print("Uso: python AES.py <enc/dec> <arquivo> [chave]")
    sys.exit()

modo = sys.argv[1]
arquivo = sys.argv[2]

if len(sys.argv) >= 4:
    chave = sys.argv[3].encode()
else:
    chave = input("Digite a chave: ").encode()


chave = chave.ljust(16, b'\0')[:16]

with open(arquivo, "rb") as f:
    data = f.read()

cipher = AES.new(chave, AES.MODE_ECB)

if modo == "dec":
    try:
        data = base64.b64decode(data)
        resultado = unpad(cipher.decrypt(data), 16)

        
        with open(arquivo, "wb") as f:
            f.write(resultado)

        print("arquivo descriptografado com sucesso!")

    except:
        print("erro: chave errada ou arquivo corrompido")


elif modo == "enc":
    criptografado = cipher.encrypt(pad(data, 16))
    b64 = base64.b64encode(criptografado)

    with open(arquivo, "wb") as f:
        f.write(b64)

    print("Arquivo criptografado com sucesso!")
