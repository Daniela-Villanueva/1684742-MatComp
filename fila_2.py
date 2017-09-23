Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class fila:
	def __init__(self):
		self.fila = []
	def obtener(self):
		return self.fila.pop()
	def meter(self,e):
		self.fila.insert(0,e)
		return len(self.fila)
	@property
	def longitud(self):
		return len(self.fila)

	
>>> f=fila()
>>> f.meter(1)
1
>>> f.meter(2)
2
>>> f.meter(100)
3
>>> print(f.longitud)
3
>>> printt(f.obtener())
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    printt(f.obtener())
NameError: name 'printt' is not defined
>>> print(f.obtener)
<bound method fila.obtener of <__main__.fila object at 0x02D05A30>>
>>> 
