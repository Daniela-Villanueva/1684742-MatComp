Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from heapq import heappop, heappush
>>> from copy import deepcopy
>>> def flatten(L):
	while len(L)>0:
		yield L[0]
		L=L[1]

		
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


>>> g=Grafo()
>>> g.conecta('a','b',1)
>>> g.conecta('a','c',1)
>>> g.conecta('a','d',1)
>>> g.conecta('a','e',1)
>>> g.conecta('c','e',1)
>>> g.conecta('c','f',1)
>>> g.conecta('b','f',1)
>>> print(g.shortests('c'))
{'c': (0, 'c', ['c']), 'a': (1, 'a', ['c', 'a']), 'e': (1, 'e', ['c', 'e']), 'f': (1, 'f', ['c', 'f']), 'b': (2, 'b', ['c', 'a', 'b']), 'd': (2, 'd', ['c', 'a', 'd'])}
>>> print(g.shortests('a'))
{'a': (0, 'a', ['a']), 'b': (1, 'b', ['a', 'b']), 'c': (1, 'c', ['a', 'c']), 'd': (1, 'd', ['a', 'd']), 'e': (1, 'e', ['a', 'e']), 'f': (2, 'f', ['a', 'b', 'f'])}
>>> print(g.shortests('e'))
{'e': (0, 'e', ['e']), 'a': (1, 'a', ['e', 'a']), 'c': (1, 'c', ['e', 'c']), 'b': (2, 'b', ['e', 'a', 'b']), 'd': (2, 'd', ['e', 'a', 'd']), 'f': (2, 'f', ['e', 'c', 'f'])}
>>> print(g.shortests('f'))
{'f': (0, 'f', ['f']), 'b': (1, 'b', ['f', 'b']), 'c': (1, 'c', ['f', 'c']), 'a': (2, 'a', ['f', 'b', 'a']), 'e': (2, 'e', ['f', 'c', 'e']), 'd': (3, 'd', ['f', 'b', 'a', 'd'])}
>>> 
