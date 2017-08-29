Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a=0
>>> def minimo(cjt):
	aux=cjt
	global a
	result=-1
	for i in range(0,len(cjt)):
		esminimo=true
		for j in range(0,len(aux)):
			b=-1
			if cjt[i]>arr[j]:
				esminimo=false
				break
			else:
				aux=cjt
				return result

			
>>> def ordenamiento(cjt):
	aux=cjt
	result=[]
	for i in range(0,len(cjt)):
		m=minimo(aux)
		result.append(aux[m])
		return result

	
>>> import random
>>> p=random.sample(range(2,102),100)
>>> a=0
>>> print(p)
[56, 61, 76, 41, 83, 89, 26, 73, 74, 75, 51, 71, 62, 98, 20, 97, 67, 53, 8, 34, 93, 19, 66, 92, 27, 65, 63, 47, 10, 16, 100, 80, 58, 91, 36, 30, 37, 32, 33, 15, 101, 39, 6, 96, 70, 35, 78, 3, 60, 57, 77, 21, 18, 44, 69, 90, 88, 48, 64, 22, 94, 4, 52, 87, 54, 38, 5, 95, 72, 29, 17, 85, 46, 24, 14, 42, 11, 7, 59, 31, 84, 23, 40, 79, 12, 25, 9, 68, 50, 81, 45, 86, 99, 2, 13, 28, 55, 49, 43, 82]
>>> print(min(p))
2
>>> print(a)
0
>>> 
