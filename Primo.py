Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def primo(n):
	cnt=0
	for(i in round(2,n**0.5))):
		
SyntaxError: invalid syntax
>>> def primo(n):
	cnt=0
	for i in range(2,round(n**0.5)):
		cnt=cnt+1
		if((n%i)==0):
			break
	return cnt

>>> 
