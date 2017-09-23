Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class pila:
	def __init__(self):
		self.pila = []
	def obtener(self):
		return self.pila.pop()
	def meter(self,e):
		self.pila.insert(0,e)
		return len(self.pila)
	@property
	def longitud(self):
		return len(self.pila)

	
>>> p= pila()
>>> p.meter(1)
1
>>> p.meter(2)
2
>>> p.meter(100)
3
>>> p.obtener()
1
>>> p.longitud
2
>>> 
