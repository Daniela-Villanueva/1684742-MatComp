Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
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
>>> g.conecta('a','c',5)
>>> g.conecta('a','b',2)
>>> g.conecta('a','d',9)
>>> g.conecta('b','e',7)
>>> g.conecta('e','f',3)
>>> print(g.shortests('b','f'))
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    print(g.shortests('b','f'))
TypeError: shortests() takes 2 positional arguments but 3 were given
>>> print(g.shortests('f'))
{'f': (0, 'f', ['f']), 'b': (1, 'b', ['f', 'b']), 'c': (1, 'c', ['f', 'c']), 'e': (2, 'e', ['f', 'c', 'e']), 'a': (3, 'a', ['f', 'b', 'a']), 'd': (12, 'd', ['f', 'b', 'a', 'd'])}
>>> g.conecta('g','h',5)
>>> g.conecta('g','i',3)
>>> g.conecta('g','j',5)
>>> g.conecta('j','k',6)
>>> g.conecta('j','l',4)
>>> g.conecta('l','m',2)
>>> g.conecta('l','n',7)
>>> print(g.shortests('g'))
{'g': (0, 'g', ['g']), 'i': (3, 'i', ['g', 'i']), 'h': (5, 'h', ['g', 'h']), 'j': (5, 'j', ['g', 'j']), 'l': (9, 'l', ['g', 'j', 'l']), 'k': (11, 'k', ['g', 'j', 'k']), 'm': (11, 'm', ['g', 'j', 'l', 'm']), 'n': (16, 'n', ['g', 'j', 'l', 'n'])}
>>> print(g.shortests('i'))
{'i': (0, 'i', ['i']), 'g': (3, 'g', ['i', 'g']), 'h': (8, 'h', ['i', 'g', 'h']), 'j': (8, 'j', ['i', 'g', 'j']), 'l': (12, 'l', ['i', 'g', 'j', 'l']), 'k': (14, 'k', ['i', 'g', 'j', 'k']), 'm': (14, 'm', ['i', 'g', 'j', 'l', 'm']), 'n': (19, 'n', ['i', 'g', 'j', 'l', 'n'])}
>>> print(g.shortests('j'))
{'j': (0, 'j', ['j']), 'l': (4, 'l', ['j', 'l']), 'g': (5, 'g', ['j', 'g']), 'k': (6, 'k', ['j', 'k']), 'm': (6, 'm', ['j', 'l', 'm']), 'i': (8, 'i', ['j', 'g', 'i']), 'h': (10, 'h', ['j', 'g', 'h']), 'n': (11, 'n', ['j', 'l', 'n'])}
>>> print(g.shortests('k'))
{'k': (0, 'k', ['k']), 'j': (6, 'j', ['k', 'j']), 'l': (10, 'l', ['k', 'j', 'l']), 'g': (11, 'g', ['k', 'j', 'g']), 'm': (12, 'm', ['k', 'j', 'l', 'm']), 'i': (14, 'i', ['k', 'j', 'g', 'i']), 'h': (16, 'h', ['k', 'j', 'g', 'h']), 'n': (17, 'n', ['k', 'j', 'l', 'n'])}
>>> print(g.shortests('l'))
{'l': (0, 'l', ['l']), 'm': (2, 'm', ['l', 'm']), 'j': (4, 'j', ['l', 'j']), 'n': (7, 'n', ['l', 'n']), 'g': (9, 'g', ['l', 'j', 'g']), 'k': (10, 'k', ['l', 'j', 'k']), 'i': (12, 'i', ['l', 'j', 'g', 'i']), 'h': (14, 'h', ['l', 'j', 'g', 'h'])}
>>> print(g.shortests('m'))
{'m': (0, 'm', ['m']), 'l': (2, 'l', ['m', 'l']), 'j': (6, 'j', ['m', 'l', 'j']), 'n': (9, 'n', ['m', 'l', 'n']), 'g': (11, 'g', ['m', 'l', 'j', 'g']), 'k': (12, 'k', ['m', 'l', 'j', 'k']), 'i': (14, 'i', ['m', 'l', 'j', 'g', 'i']), 'h': (16, 'h', ['m', 'l', 'j', 'g', 'h'])}
>>> print(g.shortests('n'))
{'n': (0, 'n', ['n']), 'l': (7, 'l', ['n', 'l']), 'm': (9, 'm', ['n', 'l', 'm']), 'j': (11, 'j', ['n', 'l', 'j']), 'g': (16, 'g', ['n', 'l', 'j', 'g']), 'k': (17, 'k', ['n', 'l', 'j', 'k']), 'i': (19, 'i', ['n', 'l', 'j', 'g', 'i']), 'h': (21, 'h', ['n', 'l', 'j', 'g', 'h'])}
>>> print(g.shortests('h'))
{'h': (0, 'h', ['h']), 'g': (5, 'g', ['h', 'g']), 'i': (8, 'i', ['h', 'g', 'i']), 'j': (10, 'j', ['h', 'g', 'j']), 'l': (14, 'l', ['h', 'g', 'j', 'l']), 'k': (16, 'k', ['h', 'g', 'j', 'k']), 'm': (16, 'm', ['h', 'g', 'j', 'l', 'm']), 'n': (21, 'n', ['h', 'g', 'j', 'l', 'n'])}
>>> g.conecta('o','a',12)
>>> g.conecta('o','c',10)
>>> g.conecta('o','p',7)
>>> g.conecta('p','c',6)
>>> g.conecta('p','f',14)
>>> g.conecta('q','m',8)
>>> g.conecta('l','q',9)
>>> print(g.shortests('l'))
{'l': (0, 'l', ['l']), 'm': (2, 'm', ['l', 'm']), 'j': (4, 'j', ['l', 'j']), 'n': (7, 'n', ['l', 'n']), 'g': (9, 'g', ['l', 'j', 'g']), 'q': (9, 'q', ['l', 'q']), 'k': (10, 'k', ['l', 'j', 'k']), 'i': (12, 'i', ['l', 'j', 'g', 'i']), 'h': (14, 'h', ['l', 'j', 'g', 'h'])}
>>> print(g.shortests('q'))
{'q': (0, 'q', ['q']), 'm': (8, 'm', ['q', 'm']), 'l': (9, 'l', ['q', 'l']), 'j': (13, 'j', ['q', 'l', 'j']), 'n': (16, 'n', ['q', 'l', 'n']), 'g': (18, 'g', ['q', 'l', 'j', 'g']), 'k': (19, 'k', ['q', 'l', 'j', 'k']), 'i': (21, 'i', ['q', 'l', 'j', 'g', 'i']), 'h': (23, 'h', ['q', 'l', 'j', 'g', 'h'])}
>>> print(g.shortests('p'))
{'p': (0, 'p', ['p']), 'c': (6, 'c', ['p', 'c']), 'e': (7, 'e', ['p', 'c', 'e']), 'f': (7, 'f', ['p', 'c', 'f']), 'o': (7, 'o', ['p', 'o']), 'a': (8, 'a', ['p', 'c', 'e', 'a']), 'b': (8, 'b', ['p', 'c', 'f', 'b']), 'd': (17, 'd', ['p', 'c', 'e', 'a', 'd'])}
>>> print(g.shortests('o'))
{'o': (0, 'o', ['o']), 'p': (7, 'p', ['o', 'p']), 'c': (10, 'c', ['o', 'c']), 'e': (11, 'e', ['o', 'c', 'e']), 'f': (11, 'f', ['o', 'c', 'f']), 'a': (12, 'a', ['o', 'c', 'e', 'a']), 'b': (12, 'b', ['o', 'c', 'f', 'b']), 'd': (21, 'd', ['o', 'c', 'e', 'a', 'd'])}
>>> print(g.shortests('m'))
{'m': (0, 'm', ['m']), 'l': (2, 'l', ['m', 'l']), 'j': (6, 'j', ['m', 'l', 'j']), 'q': (8, 'q', ['m', 'q']), 'n': (9, 'n', ['m', 'l', 'n']), 'g': (11, 'g', ['m', 'l', 'j', 'g']), 'k': (12, 'k', ['m', 'l', 'j', 'k']), 'i': (14, 'i', ['m', 'l', 'j', 'g', 'i']), 'h': (16, 'h', ['m', 'l', 'j', 'g', 'h'])}
>>> g.conecta('q','r',10)
>>> g.conecta('r','p',7)
>>> g.conecta('r','s',9)
>>> g.conecta('s','t',4)
>>> g.conecta('t','u',6)
>>> print(g.shortests('q'))
{'q': (0, 'q', ['q']), 'm': (8, 'm', ['q', 'm']), 'l': (9, 'l', ['q', 'l']), 'r': (10, 'r', ['q', 'r']), 'j': (13, 'j', ['q', 'l', 'j']), 'n': (16, 'n', ['q', 'l', 'n']), 'p': (17, 'p', ['q', 'r', 'p']), 'g': (18, 'g', ['q', 'l', 'j', 'g']), 'k': (19, 'k', ['q', 'l', 'j', 'k']), 's': (19, 's', ['q', 'r', 's']), 'i': (21, 'i', ['q', 'l', 'j', 'g', 'i']), 'c': (23, 'c', ['q', 'r', 'p', 'c']), 'h': (23, 'h', ['q', 'l', 'j', 'g', 'h']), 't': (23, 't', ['q', 'r', 's', 't']), 'e': (24, 'e', ['q', 'r', 'p', 'c', 'e']), 'f': (24, 'f', ['q', 'r', 'p', 'c', 'f']), 'o': (24, 'o', ['q', 'r', 'p', 'o']), 'a': (25, 'a', ['q', 'r', 'p', 'c', 'e', 'a']), 'b': (25, 'b', ['q', 'r', 'p', 'c', 'f', 'b']), 'u': (29, 'u', ['q', 'r', 's', 't', 'u']), 'd': (34, 'd', ['q', 'r', 'p', 'c', 'e', 'a', 'd'])}
>>> print(g.shortests('r'))
{'r': (0, 'r', ['r']), 'p': (7, 'p', ['r', 'p']), 's': (9, 's', ['r', 's']), 'q': (10, 'q', ['r', 'q']), 'c': (13, 'c', ['r', 'p', 'c']), 't': (13, 't', ['r', 's', 't']), 'e': (14, 'e', ['r', 'p', 'c', 'e']), 'f': (14, 'f', ['r', 'p', 'c', 'f']), 'o': (14, 'o', ['r', 'p', 'o']), 'a': (15, 'a', ['r', 'p', 'c', 'e', 'a']), 'b': (15, 'b', ['r', 'p', 'c', 'f', 'b']), 'm': (18, 'm', ['r', 'q', 'm']), 'l': (19, 'l', ['r', 'q', 'l']), 'u': (19, 'u', ['r', 's', 't', 'u']), 'j': (23, 'j', ['r', 'q', 'l', 'j']), 'd': (24, 'd', ['r', 'p', 'c', 'e', 'a', 'd']), 'n': (26, 'n', ['r', 'q', 'l', 'n']), 'g': (28, 'g', ['r', 'q', 'l', 'j', 'g']), 'k': (29, 'k', ['r', 'q', 'l', 'j', 'k']), 'i': (31, 'i', ['r', 'q', 'l', 'j', 'g', 'i']), 'h': (33, 'h', ['r', 'q', 'l', 'j', 'g', 'h'])}
>>> print(g.shortests('s'))
{'s': (0, 's', ['s']), 't': (4, 't', ['s', 't']), 'r': (9, 'r', ['s', 'r']), 'u': (10, 'u', ['s', 't', 'u']), 'p': (16, 'p', ['s', 'r', 'p']), 'q': (19, 'q', ['s', 'r', 'q']), 'c': (22, 'c', ['s', 'r', 'p', 'c']), 'e': (23, 'e', ['s', 'r', 'p', 'c', 'e']), 'f': (23, 'f', ['s', 'r', 'p', 'c', 'f']), 'o': (23, 'o', ['s', 'r', 'p', 'o']), 'a': (24, 'a', ['s', 'r', 'p', 'c', 'e', 'a']), 'b': (24, 'b', ['s', 'r', 'p', 'c', 'f', 'b']), 'm': (27, 'm', ['s', 'r', 'q', 'm']), 'l': (28, 'l', ['s', 'r', 'q', 'l']), 'j': (32, 'j', ['s', 'r', 'q', 'l', 'j']), 'd': (33, 'd', ['s', 'r', 'p', 'c', 'e', 'a', 'd']), 'n': (35, 'n', ['s', 'r', 'q', 'l', 'n']), 'g': (37, 'g', ['s', 'r', 'q', 'l', 'j', 'g']), 'k': (38, 'k', ['s', 'r', 'q', 'l', 'j', 'k']), 'i': (40, 'i', ['s', 'r', 'q', 'l', 'j', 'g', 'i']), 'h': (42, 'h', ['s', 'r', 'q', 'l', 'j', 'g', 'h'])}
>>> print(g.shortests('t'))
{'t': (0, 't', ['t']), 's': (4, 's', ['t', 's']), 'u': (6, 'u', ['t', 'u']), 'r': (13, 'r', ['t', 's', 'r']), 'p': (20, 'p', ['t', 's', 'r', 'p']), 'q': (23, 'q', ['t', 's', 'r', 'q']), 'c': (26, 'c', ['t', 's', 'r', 'p', 'c']), 'e': (27, 'e', ['t', 's', 'r', 'p', 'c', 'e']), 'f': (27, 'f', ['t', 's', 'r', 'p', 'c', 'f']), 'o': (27, 'o', ['t', 's', 'r', 'p', 'o']), 'a': (28, 'a', ['t', 's', 'r', 'p', 'c', 'e', 'a']), 'b': (28, 'b', ['t', 's', 'r', 'p', 'c', 'f', 'b']), 'm': (31, 'm', ['t', 's', 'r', 'q', 'm']), 'l': (32, 'l', ['t', 's', 'r', 'q', 'l']), 'j': (36, 'j', ['t', 's', 'r', 'q', 'l', 'j']), 'd': (37, 'd', ['t', 's', 'r', 'p', 'c', 'e', 'a', 'd']), 'n': (39, 'n', ['t', 's', 'r', 'q', 'l', 'n']), 'g': (41, 'g', ['t', 's', 'r', 'q', 'l', 'j', 'g']), 'k': (42, 'k', ['t', 's', 'r', 'q', 'l', 'j', 'k']), 'i': (44, 'i', ['t', 's', 'r', 'q', 'l', 'j', 'g', 'i']), 'h': (46, 'h', ['t', 's', 'r', 'q', 'l', 'j', 'g', 'h'])}
>>> print(g.shortests('u'))
{'u': (0, 'u', ['u']), 't': (6, 't', ['u', 't']), 's': (10, 's', ['u', 't', 's']), 'r': (19, 'r', ['u', 't', 's', 'r']), 'p': (26, 'p', ['u', 't', 's', 'r', 'p']), 'q': (29, 'q', ['u', 't', 's', 'r', 'q']), 'c': (32, 'c', ['u', 't', 's', 'r', 'p', 'c']), 'e': (33, 'e', ['u', 't', 's', 'r', 'p', 'c', 'e']), 'f': (33, 'f', ['u', 't', 's', 'r', 'p', 'c', 'f']), 'o': (33, 'o', ['u', 't', 's', 'r', 'p', 'o']), 'a': (34, 'a', ['u', 't', 's', 'r', 'p', 'c', 'e', 'a']), 'b': (34, 'b', ['u', 't', 's', 'r', 'p', 'c', 'f', 'b']), 'm': (37, 'm', ['u', 't', 's', 'r', 'q', 'm']), 'l': (38, 'l', ['u', 't', 's', 'r', 'q', 'l']), 'j': (42, 'j', ['u', 't', 's', 'r', 'q', 'l', 'j']), 'd': (43, 'd', ['u', 't', 's', 'r', 'p', 'c', 'e', 'a', 'd']), 'n': (45, 'n', ['u', 't', 's', 'r', 'q', 'l', 'n']), 'g': (47, 'g', ['u', 't', 's', 'r', 'q', 'l', 'j', 'g']), 'k': (48, 'k', ['u', 't', 's', 'r', 'q', 'l', 'j', 'k']), 'i': (50, 'i', ['u', 't', 's', 'r', 'q', 'l', 'j', 'g', 'i']), 'h': (52, 'h', ['u', 't', 's', 'r', 'q', 'l', 'j', 'g', 'h'])}
>>> print(g.shortests('p'))
{'p': (0, 'p', ['p']), 'c': (6, 'c', ['p', 'c']), 'e': (7, 'e', ['p', 'c', 'e']), 'f': (7, 'f', ['p', 'c', 'f']), 'o': (7, 'o', ['p', 'o']), 'r': (7, 'r', ['p', 'r']), 'a': (8, 'a', ['p', 'c', 'e', 'a']), 'b': (8, 'b', ['p', 'c', 'f', 'b']), 's': (16, 's', ['p', 'r', 's']), 'd': (17, 'd', ['p', 'c', 'e', 'a', 'd']), 'q': (17, 'q', ['p', 'r', 'q']), 't': (20, 't', ['p', 'r', 's', 't']), 'm': (25, 'm', ['p', 'r', 'q', 'm']), 'l': (26, 'l', ['p', 'r', 'q', 'l']), 'u': (26, 'u', ['p', 'r', 's', 't', 'u']), 'j': (30, 'j', ['p', 'r', 'q', 'l', 'j']), 'n': (33, 'n', ['p', 'r', 'q', 'l', 'n']), 'g': (35, 'g', ['p', 'r', 'q', 'l', 'j', 'g']), 'k': (36, 'k', ['p', 'r', 'q', 'l', 'j', 'k']), 'i': (38, 'i', ['p', 'r', 'q', 'l', 'j', 'g', 'i']), 'h': (40, 'h', ['p', 'r', 'q', 'l', 'j', 'g', 'h'])}
>>> 
