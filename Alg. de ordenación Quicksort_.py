Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def quicksort(A,B,C):
	if(B<C):
		p=particion(A,B,C)
		quicksort(A,B,C)
		quicksort(A,p+1,C)

		
>>> def particion(A,B,C):
	pivote=A[B]
	i=B
	j=C
	for true:
		
SyntaxError: invalid syntax
>>> def quicksort(A,B,C):
	if(B<C):
		p=particion(A,B,C)
		quicksort(A,B,C)
		quicksort(A,p+1,C)

		
>>> def particion(A,B,C):
	pivote=A[B]
	i=B
	j=C
	for true
	
SyntaxError: invalid syntax
>>>  def quicksort(A,B,C):
	if(B<C):
		p=particion(A,B,C)
		quicksort(A,B,C)
		quicksort(A,p+1,C)


SyntaxError: unexpected indent
>>> def quicksort(A,B,C):
	if(B<C):
		p=particion(A,B,C)
		quicksort(A,B,C)
		quicksort(A,p+1,C)

		
>>> def particion(A,B,C):
	pivote=A[B]
	i=B
	j=C
	while true:
		while(A[j]>pivote):
			j=j-1
		while(A[i]<pivote):
			i=i+1
		if(i<j):
			aux=A[j]
			A[i]=A[j]
			A[j]=aux
		else:
			return j

		
>>> A=[6,5,3,1,8,7,2,4]
>>> print(A)
[6, 5, 3, 1, 8, 7, 2, 4]
>>> quicksort(A,0,len(A)-1)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    quicksort(A,0,len(A)-1)
  File "<pyshell#16>", line 3, in quicksort
    p=particion(A,B,C)
  File "<pyshell#29>", line 5, in particion
    while true:
NameError: name 'true' is not defined
>>> def quicksort(A,B,C):
	if(B<C):
		p=particion(A,B,C)
		quicksort(A,B,C)
		quicksort(A,p+1,C)


>>> def particion(A,B,C):
	pivote=A[B]
	i=B
	j=C
	while true:
		while(A[j]>pivote):
			j=j-1
		while(A[i]<pivote):
			i=i+1
		if(i<j):
			aux=A[j]
			A[i]=A[j]
			A[j]=aux
		else:
			return j

		
>>> A=[6,5,3,1,8,7,2,4]
>>> print(A)
[6, 5, 3, 1, 8, 7, 2, 4]
>>> quicksort(A,B,C)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    quicksort(A,B,C)
NameError: name 'B' is not defined
>>> print(A)
[6, 5, 3, 1, 8, 7, 2, 4]
>>> quicksort(A,B,C)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    quicksort(A,B,C)
NameError: name 'B' is not defined
>>> quicksort(A,p+1,C)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    quicksort(A,p+1,C)
NameError: name 'p' is not defined
>>> quicksort(A,B,C):
	
SyntaxError: invalid syntax
>>> quicksort(A,B,C):
	
SyntaxError: invalid syntax
>>> quicksort(A,B,C)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    quicksort(A,B,C)
NameError: name 'B' is not defined
>>> def quicksort(A,B,C):
	if(B<C):
		p=particion(A,B,C)
		quicksort(A,B,p)
		quicksort(A,p+1,C)

		
>>> def particion(A,B,C):
	pivote=A[B]
	i=B
	j=C
	while true:
		while(A[j]>pivote):
			j=j-1
		while(A[i]<pivote):
			i=i+1
		if(i<j):
			aux=A[j]
			A[i]=A[j]
			A[j]=aux
		else:
			return j

		
>>> A=[6,5,3,1,8,7,2,4]
>>> print(A)
[6, 5, 3, 1, 8, 7, 2, 4]
>>> quicksort(A,0,len(A)-1)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    quicksort(A,0,len(A)-1)
  File "<pyshell#50>", line 3, in quicksort
    p=particion(A,B,C)
  File "<pyshell#52>", line 5, in particion
    while true:
NameError: name 'true' is not defined
>>> quicksort(A,B,C)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    quicksort(A,B,C)
NameError: name 'B' is not defined
>>> 
>>> 
>>> def quicksort(A,lo,hi):
	if(lo<hi):
		p=particion(A,lo,hi)
		quicksort(A,lo,p)
		quicksort(A,p+1,hi)

		
>>> def particion(A,lo,hi):
	pivote=A[lo]
	i=lo
	j=hi
	while true:
		whilw(A[j]>pivote):
			
SyntaxError: invalid syntax
>>> def quicksort(A,lo,hi):
	if(lo<hi):
		p=particion(A,lo,hi)
		quicksort(A,lo,p)
		quicksort(A,p+1,hi)

		
>>> def particion(A,lo,hi):
	pivote=A[lo]
	i=lo
	j=hi
	while true:
	   while(A[j]>pivote):
		   j=j-1
           while(A[i]<pivote):
		   
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> def quicksort(A,lo,hi):
	if(lo<hi):
		p=particion(A,lo,hi)
		quicksort(A,lo,p)
		quicksort(A,p+1,hi)


>>> def particion(A,lo,hi):
	pivote=A[lo]
	i=lo
	j=hi
	while true:
		while(A[j]>pivote):
			j=j-1
		while(A[i]<pivote):
			i=i+1
		if(i<j):
			aux=A[i]
			A[i]=A[j]
			A[j]=aux
		else:
			return j
	A=[6,5,3,1,8,7,2,4]
	ptint(A)
	quicksort(A,0,len(A)-1)
	print(A)

	
>>> A=[6,5,3,1,8,7,2,4]
>>> print(A)
[6, 5, 3, 1, 8, 7, 2, 4]
>>> quicksort(A,0,len(A)-1)
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    quicksort(A,0,len(A)-1)
  File "<pyshell#77>", line 3, in quicksort
    p=particion(A,lo,hi)
  File "<pyshell#93>", line 5, in particion
    while true:
NameError: name 'true' is not defined
>>> def quicksort(A,lo,hi):
	if(lo<hi):
		p=particion(A,lo,hi)
		quicksort(A,lo,p)
		quicksort(A,p+1,hi)

		
>>> def particion(A,lo,hi):
	pivote=A[lo]
	i=lo
	j=hi
	while true:
		while(A[j]>pivote):
			j=j-1
		while(A[i]<pivote):
			i=i+1
		if(i<j):
			aux=A[i]
			A[i]=A[j]
			A[j]=aux
		else:
			return j

		
>>> A=[6,5,3,1,8,7,2,4]
>>> print(A)
[6, 5, 3, 1, 8, 7, 2, 4]
>>> quicksort(A,lo,hi)
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    quicksort(A,lo,hi)
NameError: name 'lo' is not defined
>>> def quicksort(L,first,last):
	i=first
	j=last
	pivote=(L[i]+L[j])/2
	while i<j:
		while L[i]<pivote:
			i+=1
		while L[j]>pivote:
			j-=1
		if i<=j:
			x=L[j]
			L[j]=L[i]
			L[i]=x
			i+=1
			j-=1
	if first<j:
		L=quicksort(L,first,j)
	if last>i:
		L=quicksort(L,i,last)
	return L

>>> L=[6,5,3,1,8,7,2,4]
>>> print(L)
[6, 5, 3, 1, 8, 7, 2, 4]
>>> quicksort(L,first,last)
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    quicksort(L,first,last)
NameError: name 'first' is not defined
>>> 
