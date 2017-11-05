Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from heapq import heappop,heappush
>>> from copy import deepcopy
>>> import random
>>> import time
>>> def permutation(lst):
	if len(lst)==0:
		return[]
	if len(lst)==1:
		return[lst]
	l=[]
	for i in range(len(lst)):
		m=lst[i]
		remlst=lst[:i]+lst[i+1:]
		for p in permutation(remlst):
			l.append([m]+p)
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
		self.pila.insert(0,e)
		return len(self.pila)
	@property
	def longitud(self):
		return len(self.pila)

	
>>> def flatten(L):
	while len(L) > 0:
		yield L [0]
		L = L[1]

		
>>> class Grafo:
	def __init__(self):
		self.V = set()
		self.E = dict()
		self.vecinos = dict()
	def agrega(self, v):
		self.V.add(v)
		if not v in self.vecinos:
			self.vecinos[v] = set()
	def conecta(self, v, u, peso=1):
		self.agrega(v)
		self.agrega(u)
		self.E[(v, u)] = self.E[(u, v)] = peso
		self.vecinos[v].add(u)
		self.vecinos[u].add(v)
	def complemento(self):
		comp= Grafo()
		for v in self.V:
			for w in self.V:
				if v != w and (v, w) not in self.E:
					comp.conecta(v, w, 1)
		return comp
	def BFS(self,ni):
		visitados=[]
		f=Fila()
		f.meter(ni)
		while (f.longitud>0):
			na=f.obtener()
			visitados.append(na)
			ln=self.vecinos[na]
			for nodo in ln:
				if nodo not in visitados:
					f.meter(nodo)
		return visitados
	def DFS(self,ni):
		visitados=[]
		f=Pila()
		f.meter(ni)
		while (f.longitud>0):
			na=f.obtener()
			visitados.append(na)
			ln=self.vecinos[na]
			for nodo in ln:
				if nodo not in visitados:
					f.meter(nodo)
		return visitados
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
	def kruskal(self):
		e=deepcopy(self.E)
		arbol=Grafo()
		peso=0
		comp=dict()
		t=sorted(e.keys(),key=lambda k:e[k],reverse=True)
		nuevo=set()
		while len(t)>0 and len(nuevo)<len(self.V):
			print(len(t))
			arista=t.pop()
			w=e[arista]
			del e[arista]
			(u,v)=arista
			c=comp.get(v,{v})
			if u not in c:
				print('u',u,'v',v,'c',c)
				arbol.conecta(u,v,w)
				peso+=w
				nuevo=c.union(comp.get(u,{u}))
				for i in nuevo:
					comp[i]=nuevo
		print('MST con peso', peso, ':', nuevo, '\n', arbol.E)
		return arbol
	def vecinoMasCercano(self):
		ni = random.choice(list(self.V))
		result=[ni]
		while len(result) < len(self.V):
			ln = set(self.vecinos[ni])
			le = dict()
			res =(ln-set(result))
			for nv in res:
				le[nv]=self.E[(ni,nv)]
			menor = min(le, key=le.get)
			result.append(menor)
			ni=menor
		return result

	
>>> g=Grafo()
>>> g.conecta('a','b',284)
>>> g.conecta('a','c',1286)
>>> g.conecta('d','c',1103)
>>> g.conecta('c','e',1733)
>>> g.conecta('f','e',1170)
>>> g.conecta('f','g',122)
>>> g.conecta('f','h',219)
>>> g.conecta('a','i',1483)
>>> g.conecta('d','j',316)
>>> g.conecta('k','e',831)
>>> g.conecta('a','d',913)
>>> print(g.kruskal())
22
u g v f c {'f'}
21
20
u h v f c {'g', 'f'}
19
18
u b v a c {'a'}
17
16
u j v d c {'d'}
15
14
u e v k c {'k'}
13
12
u d v a c {'b', 'a'}
11
10
u c v d c {'j', 'd', 'b', 'a'}
9
8
u e v f c {'h', 'g', 'f'}
7
6
5
4
u i v a c {'d', 'b', 'c', 'j', 'a'}
3
2
u e v c c {'d', 'b', 'c', 'i', 'j', 'a'}
MST con peso 8174 : {'c', 'a', 'd', 'e', 'g', 'h', 'j', 'f', 'k', 'i', 'b'} 
 {('g', 'f'): 122, ('f', 'g'): 122, ('h', 'f'): 219, ('f', 'h'): 219, ('b', 'a'): 284, ('a', 'b'): 284, ('j', 'd'): 316, ('d', 'j'): 316, ('e', 'k'): 831, ('k', 'e'): 831, ('d', 'a'): 913, ('a', 'd'): 913, ('c', 'd'): 1103, ('d', 'c'): 1103, ('e', 'f'): 1170, ('f', 'e'): 1170, ('i', 'a'): 1483, ('a', 'i'): 1483, ('e', 'c'): 1733, ('c', 'e'): 1733}
<__main__.Grafo object at 0x023164D0>
>>> print(g.shortests('c'))
{'c': (0, 'c', ['c']), 'd': (1103, 'd', ['c', 'd']), 'a': (1286, 'a', ['c', 'a']), 'j': (1419, 'j', ['c', 'd', 'j']), 'b': (1570, 'b', ['c', 'a', 'b']), 'e': (1733, 'e', ['c', 'e']), 'k': (2564, 'k', ['c', 'e', 'k']), 'i': (2769, 'i', ['c', 'a', 'i']), 'f': (2903, 'f', ['c', 'e', 'f']), 'g': (3025, 'g', ['c', 'e', 'f', 'g']), 'h': (3122, 'h', ['c', 'e', 'f', 'h'])}
>>> print(g)
<__main__.Grafo object at 0x02202B10>
>>> k=g.kruskal()
22
u g v f c {'f'}
21
20
u h v f c {'g', 'f'}
19
18
u b v a c {'a'}
17
16
u j v d c {'d'}
15
14
u e v k c {'k'}
13
12
u d v a c {'b', 'a'}
11
10
u c v d c {'j', 'd', 'b', 'a'}
9
8
u e v f c {'h', 'g', 'f'}
7
6
5
4
u i v a c {'d', 'b', 'c', 'j', 'a'}
3
2
u e v c c {'d', 'b', 'c', 'i', 'j', 'a'}
MST con peso 8174 : {'c', 'a', 'd', 'e', 'g', 'h', 'j', 'f', 'k', 'i', 'b'} 
 {('g', 'f'): 122, ('f', 'g'): 122, ('h', 'f'): 219, ('f', 'h'): 219, ('b', 'a'): 284, ('a', 'b'): 284, ('j', 'd'): 316, ('d', 'j'): 316, ('e', 'k'): 831, ('k', 'e'): 831, ('d', 'a'): 913, ('a', 'd'): 913, ('c', 'd'): 1103, ('d', 'c'): 1103, ('e', 'f'): 1170, ('f', 'e'): 1170, ('i', 'a'): 1483, ('a', 'i'): 1483, ('e', 'c'): 1733, ('c', 'e'): 1733}
>>> print([print(x,k.E[x]) for x in k.E])
('g', 'f') 122
('f', 'g') 122
('h', 'f') 219
('f', 'h') 219
('b', 'a') 284
('a', 'b') 284
('j', 'd') 316
('d', 'j') 316
('e', 'k') 831
('k', 'e') 831
('d', 'a') 913
('a', 'd') 913
('c', 'd') 1103
('d', 'c') 1103
('e', 'f') 1170
('f', 'e') 1170
('i', 'a') 1483
('a', 'i') 1483
('e', 'c') 1733
('c', 'e') 1733
[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
>>> for r in range(10):
	ni=random.choice(list(k.V))
	dfs=k.DFS(ni)
	c=0
	print(dfs)
	print(len(dfs))
	for f in range(len(dfs)-1):
		c+=g.E[(dfs[f],dfs[f+1])]
		print(dfs[f],dfs[f+1],g.E[(dfs[f],dfs[f+1])])
	c+=g.E[(dfs[-1],dfs[0])]
	print(dfs[-1],dfs[0],g.E[(dfs[-1],dfs[0])])print('costo',c)
	
SyntaxError: invalid syntax
>>> for r in range(10):
	ni=random.choice(list(k.V))
	dfs=k.DFS(ni)
	c=0
	print(dfs)
	print(len(dfs))
	for f in range(len(dfs)-1):
		c+=g.E[(dfs[f],dfs[f+1])]
		print(dfs[f],dfs[f+1],g.E[(dfs[f],dfs[f+1])])
	c+=g.E[(dfs[-1],dfs[0])]
	print(dfs[-1],dfs[0],g.E[(dfs[-1],dfs[0])])print('costo',c)
	
SyntaxError: invalid syntax
>>> for r in range(10):
	ni=random.choice(list(k.V))
	dfs=k.DFS(ni)
	c=0
	print(dfs)
	print(len(dfs))
	for f in range(len(dfs)-1):
		c+=g.E[(dfs[f],dfs[f+1])]
		print(dfs[f],dfs[f+1],g.E[(dfs[f],dfs[f+1])])
	c+=g.E[(dfs[-1],dfs[0])]
	print(dfs[-1],dfs[0],g.E[(dfs[-1],dfs[0])])
	print('costo',c)

	
['g', 'f', 'e', 'h', 'c', 'k', 'd', 'j', 'a', 'i', 'b']
11
g f 122
f e 1170
Traceback (most recent call last):
  File "<pyshell#36>", line 8, in <module>
    c+=g.E[(dfs[f],dfs[f+1])]
KeyError: ('e', 'h')
>>> vmc=g.vecinoMasCercano()
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    vmc=g.vecinoMasCercano()
  File "<pyshell#14>", line 94, in vecinoMasCercano
    menor = min(le, key=le.get)
ValueError: min() arg is an empty sequence
>>> print(g.kruskal())
22
u g v f c {'f'}
21
20
u h v f c {'g', 'f'}
19
18
u b v a c {'a'}
17
16
u j v d c {'d'}
15
14
u e v k c {'k'}
13
12
u d v a c {'b', 'a'}
11
10
u c v d c {'j', 'd', 'b', 'a'}
9
8
u e v f c {'h', 'g', 'f'}
7
6
5
4
u i v a c {'d', 'b', 'c', 'j', 'a'}
3
2
u e v c c {'d', 'b', 'c', 'i', 'j', 'a'}
MST con peso 8174 : {'c', 'a', 'd', 'e', 'g', 'h', 'j', 'f', 'k', 'i', 'b'} 
 {('g', 'f'): 122, ('f', 'g'): 122, ('h', 'f'): 219, ('f', 'h'): 219, ('b', 'a'): 284, ('a', 'b'): 284, ('j', 'd'): 316, ('d', 'j'): 316, ('e', 'k'): 831, ('k', 'e'): 831, ('d', 'a'): 913, ('a', 'd'): 913, ('c', 'd'): 1103, ('d', 'c'): 1103, ('e', 'f'): 1170, ('f', 'e'): 1170, ('i', 'a'): 1483, ('a', 'i'): 1483, ('e', 'c'): 1733, ('c', 'e'): 1733}
<__main__.Grafo object at 0x023286D0>
>>> data = list('abcdfghij')
>>> tim = time.clock()
>>> per = permutation(data)
>>> vm,rm=100000000000,[]
>>> for e in per:
	print(e)
	c=0
	for f in range(len(e)-1):
		c+=g.E[(e[f],e[f+1])]
	c+=g.E[(e[-1],e[0])]
	if c < vm:
		vm,rm = c,e

['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j']
Traceback (most recent call last):
  File "<pyshell#51>", line 5, in <module>
    c+=g.E[(e[f],e[f+1])]
KeyError: ('b', 'c')
>>> print(time.clock()-tim)
208.02209814504621
>>> print('minimo exacto',vm,rm)
minimo exacto 100000000000 []
>>> 
