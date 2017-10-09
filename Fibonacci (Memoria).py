Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> D={}
>>> cnt=0
>>> def fibonacci(n):
	global D, cnt
	cnt+=1
	if n==0 or n==1:
		return(1)
	if n in D:
		return D[n]
	else:
		val=fibonacci(n-2)+fibonacci(n-1)
		D[n]=val
		return val

	
>>> fibonacci(34)
9227465
>>> cnt
67
>>> fibonacci(2)
2
>>> cnt
68
>>> 
