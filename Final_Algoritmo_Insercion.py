Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def insercion(I):
	for i in range(len(I)):
		for j in range(i,0,-1):
			if(I[j-1]>I[j]):
				aux=I[j]
				I[j]=I[j-1]
				I[j-1]=aux
	print(I)


>>> I=[6,5,3,1,8,7,2,4]
>>> print(I)
[6, 5, 3, 1, 8, 7, 2, 4]
>>> insercion(I)
[1, 2, 3, 4, 5, 6, 7, 8]
>>> 
