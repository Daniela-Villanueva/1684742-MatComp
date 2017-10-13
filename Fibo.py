Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> contador=0
>>> def fibo(n):
	global contador
	if n == 0 or n == 1:
		return(1)
	r,r1,r2 = 0,1,2
	for i in range (2,n):
		contador+=1
		r=r1+r2
		r2=r1
		r1=r
	return(r)

>>> fibo(3)
3
>>> contador
1
>>> fibo(28)
439204
>>> contador
27
>>> 
