Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def selection(arr):
	contador=0
	for i in range(0,len(arr)-1):
		val=i
		for j in range(i,len(arr)):
			contador=contador+1
			if(val!=i):
				aux=arr[i]
				arr[i]=arr[val]
				arr[val]=aux
				return arr

			
>>> import random
>>> def ran_n(n,lim_i=0,lim_s=100):
	arr=[]
	for i in range(n):
		arr.append(random.randint(lim_i,lim_s))
		return arr
	
