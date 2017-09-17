Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def quicksort(Q,a,b):
	if(a<b):
		p=parte(Q,a,b)
		quicksort(Q,a,p)
		quicksort(Q,p+1,b)

		
>>> def parte(Q,a,b):
	pivote=Q[a]
	i=a
	j=b
	while(Q[j]>pivote):
		j=j+1
		while(Q[i]<pivote):
			i=i+1
			if(i<j):
				aux=Q[i]
				Q[i]=Q[j]
				Q[j]=aux

>>> Q=[6,5,3,1,8,7,2,4]
>>> print(Q)
[6, 5, 3, 1, 8, 7, 2, 4]
>>> quicksort(Q,0,len(Q)-1)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    quicksort(Q,0,len(Q)-1)
  File "<pyshell#1>", line 4, in quicksort
    quicksort(Q,a,p)
  File "<pyshell#1>", line 2, in quicksort
    if(a<b):
TypeError: '<' not supported between instances of 'int' and 'NoneType'
>>> 
