Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
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
           self.E[(v, u)] = self.E[(u, v)] = peso
           self.vecinos[v].add(u)
           self.vecinos[u].add(v)
