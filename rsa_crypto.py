import math

from modinv import modinv


class RSA:

    def __init__(self):
        #creating the number convert lists
        _alfabeto = "abcdefghijklmnopqrstuvwxyz "
        self._letras = {_alfabeto[i-2] : i for i in range(2,29)}
        self._numeros = {i : _alfabeto[i-2] for i in range(2,29)}
    
    # Extended Euclides Algorithm
    def _modinv(a, b):
        #if (r == 0): return
        (r0, m0, n0) = a, 1, 0
        (r1, m1, n1) = b, 0, 1

        while(r0 % r1 > 0):
            q = r0 // r1
            r0, r1 = r1, r0 % r1
            m0, m1 = m1, m0 - m1*q
            n0, n1 = n1, n0 - n1*q
        
        return m1

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
        cripted = [i**e % n for i in code_m]
        return self._listToString(cripted)
    

    def decrypting(self, cripted, p, q, e):
        tot = (p - 1)*(q - 1)
        #d = pow(e, -1, tot)
        d = modinv(e, tot)
        n = p*q
        decrypted = [i**d % n for i in cripted]
        mensage = [self._numeros[i] for i in decrypted]
        return ''.join(mensage)

