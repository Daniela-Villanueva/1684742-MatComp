Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> contador=0
>>> def fibonacci(n):
	global contador
	contador+=1
	if n == 0 or n == 1:
		return(1)
	return fibonacci(n-2)+fibonacci(n-1)

>>> fibonacci(10)
89
>>> contador
177
>>> 
