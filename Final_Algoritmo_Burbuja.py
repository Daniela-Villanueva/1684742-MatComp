Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def burbuja(B):
	contador=0
	for i in range(1,len(B)):
		for j in range(0,len(B)-1):
			contador=contador+1
			if(B[j+1]<B[j]):
				aux=B[j]
				B[j]=B[j+1]
				B[j+1]=aux
				print(B)

				
>>> B=[6,5,3,1,8,7,2,4]
>>> print(B)
[6, 5, 3, 1, 8, 7, 2, 4]
>>> burbuja(B)
[5, 6, 3, 1, 8, 7, 2, 4]
[5, 3, 6, 1, 8, 7, 2, 4]
[5, 3, 1, 6, 8, 7, 2, 4]
[5, 3, 1, 6, 7, 8, 2, 4]
[5, 3, 1, 6, 7, 2, 8, 4]
[5, 3, 1, 6, 7, 2, 4, 8]
[3, 5, 1, 6, 7, 2, 4, 8]
[3, 1, 5, 6, 7, 2, 4, 8]
[3, 1, 5, 6, 2, 7, 4, 8]
[3, 1, 5, 6, 2, 4, 7, 8]
[1, 3, 5, 6, 2, 4, 7, 8]
[1, 3, 5, 2, 6, 4, 7, 8]
[1, 3, 5, 2, 4, 6, 7, 8]
[1, 3, 2, 5, 4, 6, 7, 8]
[1, 3, 2, 4, 5, 6, 7, 8]
[1, 2, 3, 4, 5, 6, 7, 8]
>>> 
