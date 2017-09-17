Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def seleccion(S):
	for i in range(len(S)):
		minimo=i
		for j in range(i,len(S)):
			if(S[j]<S[minimo]):
				minimo=j
				if(minimo!=i):
					aux=S[i]
					S[i]=S[minimo]
					S[minimo]=aux
					print(S)

					
>>> S=[6,5,3,1,8,7,2,4]
>>> print(S)
[6, 5, 3, 1, 8, 7, 2, 4]
>>> seleccion(S)
[5, 6, 3, 1, 8, 7, 2, 4]
[3, 6, 5, 1, 8, 7, 2, 4]
[1, 6, 5, 3, 8, 7, 2, 4]
[2, 6, 5, 3, 8, 7, 1, 4]
[2, 5, 6, 3, 8, 7, 1, 4]
[2, 3, 6, 5, 8, 7, 1, 4]
[2, 1, 6, 5, 8, 7, 3, 4]
[2, 1, 5, 6, 8, 7, 3, 4]
[2, 1, 3, 6, 8, 7, 5, 4]
[2, 1, 4, 6, 8, 7, 5, 3]
[2, 1, 4, 5, 8, 7, 6, 3]
[2, 1, 4, 3, 8, 7, 6, 5]
[2, 1, 4, 3, 7, 8, 6, 5]
[2, 1, 4, 3, 6, 8, 7, 5]
[2, 1, 4, 3, 5, 8, 7, 6]
[2, 1, 4, 3, 5, 7, 8, 6]
[2, 1, 4, 3, 5, 6, 8, 7]
[2, 1, 4, 3, 5, 6, 7, 8]
>>> 
