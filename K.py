Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from heapq import heappop, heappush
>>> from copy import deepcopy
>>> import random
>>> import time
>>> def permutation(lst):
	if len(lst) == 0:
		return []
	if len(lst) == 1:
		return [lst]
	l = []
	for i in range (len(lst)):
		m = lst[i]
		remLst = lst[:i] + lst[i+1:]
		for p in permutation(remLst):
			l.append([m] + p)
	return l

>>> class Fila:
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

	
>>> class Pila:
	def __init__(self):
		self.pila = []
	def obtener(self):
		return self.pila.pop()
	def meter(self,e):
		self.pila.append(e)
		return len(self.pila)
	@property
	def longitud(self):
		return len(self.pila)

	
>>> def flatten(L):
	while len(L) > 0:
		yield L[0]
		L = L[1]

		
>>> class Grafo:
	def __init__(self):
		self.V = set()
		self.E = dict()
		self.vecinos = dict()
	def agrega(self,v):
		self.V.add(v)
		if not v in self.vecinos:
			self.vecinos[v]=set()
	def conecta(self,v,u,peso=1):
		self.agrega(v)
		self.agrega(u)
		self.E[(v,u)] = self.E[(u,v)]=peso
		self.vecinos[v].add(u)
		self.vecinos[u].add(v)
	def complemento(self):
		comp=Grafo()
		for v in self.V:
			for w in self.V:
				if v!=w and (v,w) not in self.E:
					comp.conecta(v,w,1)
		return comp
	def shortests(self,v):
		q=[(0,v,())]
		dist=dict()
		visited=set()
		while len(q)>0:
			(l,u,p)=heappop(q)
			if u not in visited:
				visited.add(u)
				dist[u]=(l,u,list(flatten(p))[::-1]+[u])
			p=(u,p)
			for n in self.vecinos[u]:
				if n not in visited:
					el=self.E[(u,n)]
					heappush(q,(l+el,n,p))
		return dist


>>> 
