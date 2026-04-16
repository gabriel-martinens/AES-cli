# AES-cli
criptografador e descriptografador de cifra AES-ECB na biblioteca pycryptodome

---

## para o que serve?

- descriptografa arquivos usando AES-ECB
- Lê arquivos externos
- Usa chave fixa ou via argumento

---

## Como usar
Execute o arquivo com os seguintes argumentos
```bash
python AES.py MODO SEU_ARQUIVO SUA_CHAVE
```
utilize o modo "dec" para descriptografar e o modo "enc" para encriptar
### Exemplo:

```bash
python AES.py dec 7.txt "YELLOW SUBMARINE"
