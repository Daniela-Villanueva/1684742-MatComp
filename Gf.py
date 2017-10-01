Python 3.7.0a1 (v3.7.0a1:8f51bb4, Sep 19 2017, 18:50:29) [MSC v.1900 32 bit (Intel)] on win32
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

	
>>> class Grafo:
	def __init__(self):
		self.V=set()
		self.E=dict()
		self.vecinos=dict()
	def agrega(self,v):
		self.V.add(v)
		if not v in self.vecinos:
			self.vecinos[v]=set()
	def conecta(self,v,u,peso=1):
		self.agrega(v)
		self.agrega(u)
		self.E[(v,u)]=self.E[(u,v)]=peso
		self.vecinos[v].add(u)
		self.vecinos[u].add(v)


>>> def BFS(G,ni):
	visitados=[]
	f=fila()
	f.meter(ni)
	while(f.longitud>0):
		na=f.obtener()
		visitados.append(na)
		ln=G.vecinos[na]
		for nodo in ln:
			if nodo not in visitados:
				f.meter(nodo)
        return visitados
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> 
>>> return     
