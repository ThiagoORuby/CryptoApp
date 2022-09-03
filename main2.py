from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from rsa_crypto import RSA

rsa = RSA()

class Manager(ScreenManager):
	pass

class HomeScreen(Screen):
	pass

class GenerateKeyScreen(Screen):

	def callback(self):
		self.parent.current = 'home'
	
	def gerar_chaves(self, **kw):
		p = int(self.ids.p.text)
		q = int(self.ids.q.text)
		e = int(self.ids.e.text)
		n, e = rsa.generatePublicKey(p, q, e)
		self.ids.valores.text = f"n = {n}, e = {e}"
		
class EncryptScreen(Screen):

	def callback(self):
		self.parent.current = 'home'
	
	def gerar_chaves(self, **kw):
		mensage = self.ids.mensage.text
		n = int(self.ids.n.text)
		e = int(self.ids.e.text)
		cripted = rsa.encrypting(mensage, n, e)
		self.ids.valores.text = f"Cripted mensage: {cripted}"
		
class DecryptScreen(Screen):
	
	def callback(self):
		self.parent.current = 'home'
	
	def gerar_chaves(self, **kw):
		cripted = self.ids.p.text
		p = int(self.ids.p.text)
		q = int(self.ids.q.text)
		e = int(self.ids.e.text)
		n, e = rsa.decrypting(cripted, p, q, e)
		self.ids.valores.text = f"n = {n}, e = {e}"
		

class Main(MDApp):
	
	def build(self):
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "Purple"
		return Manager()
		

if __name__ == "__main__":
	Main().run()
		
