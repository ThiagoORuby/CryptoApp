"""
Autor: ThiagoORuby

Objetivos: 
- Criação de uma UI com tkinter
- Api rest com Flask
- App mobile com Flutter
"""

from rsa_crypto import RSA

module = RSA()

print("====== CRIPTOGRAFIA RSA =======")
while True:
    print("\nO que deseja fazer? ")
    print("\n1 - Gerar chave pública\n2 - Encriptar\n3 - Desencriptar\n0 - Sair")
    option = int(input())
    if option == 0:
        break
    elif option == 1:
        print("\nInforme os valores de p, q e e:")
        p = int(input())
        q = int(input())
        e = int(input())
        n, e = module.generatePublicKey(p, q, e)
        print(f"Chave pública: n = {n} e e = {e}")
    elif option == 2:
        print("\nInforme a mensagem e os valores de chave pública:")
        mensagem = str(input())
        n = int(input())
        e = int(input())
        crypted = module.encrypting("ola mundo", n, e)
        #print(crypted)
        print(f"Mensagem criptografada: \n{crypted}")
    elif option == 3:
        print("\nInforme os valores da mensagem criptografada e os valores da chave privada:")
        crypted = list(map(int, input().split()))
        p = int(input())
        q = int(input())
        e = int(input())
        print("\nMensagem desencriptada: {}".format(module.decrypting(crypted, p, q, e)))
    else:
        print("\nInfome um valor válido\n")
        continue