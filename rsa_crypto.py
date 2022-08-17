import math


class RSA:

    def __init__(self):
        #creating the number convert lists
        _alfabeto = "abcdefghijklmnopqrstuvwxyz "
        self._letras = {_alfabeto[i-2] : i for i in range(2,29)}
        self._numeros = {i : _alfabeto[i-2] for i in range(2,29)}

    def generatePublicKey(self, p, q, e):
        # Testar se p e q são primos
        n = p * q

        # Testa se e é relativamente primo a tot de n -> mdc(tot, e) = 1
        tot = (p - 1)*(q - 1)
        if math.gcd(tot, e) != 1:
            raise ValueError("O valor de e não é primo com totiente de n")

        return n, e

    def _listToString(self, list):
        newList = [str(i) for i in list]
        return " ".join(newList)
    
    def encrypting(self, mensage, n, e):
        code_m = [self._letras[i] for i in mensage.lower()]
        cripted = [pow(i, e, n) for i in code_m]
        return self._listToString(cripted)
    

    def decrypting(self, cripted, p, q, e):
        tot = (p - 1)*(q - 1)
        d = pow(e, -1, tot)
        n = p*q
        decrypted = [pow(i, d, n) for i in cripted]
        mensage = [self._numeros[i] for i in decrypted]
        return ''.join(mensage)

