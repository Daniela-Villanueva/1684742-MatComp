Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def insercion(A):
   for i in range(1,len(A)):
       valor=A[i]
       i=i-1
       while i>=0:
         if valor<a[i]:
            a[i+1]=a[i]
            a[i]=valor
            i-=1
       else:
          break

        
>>> A=[26,2,45,30,1,450,1]
>>> print(A)
[26, 2, 45, 30, 1, 450, 1]
>>> insercion(A)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    insercion(A)
  File "<pyshell#1>", line 6, in insercion
    if valor<a[i]:
NameError: name 'a' is not defined
>>> 
>>> def insercion(A):
   for i in range(1,len(A)):
       valor=A[i]
       i=i-1
       while i>=0:
         if valor<a[i]:
            a[i+1]=a[i]
            a[i]=valor
            i-=1
       else:
          break
   return A

>>> A=[26,2,45,30,1,450,1]
>>> insercion(A)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    insercion(A)
  File "<pyshell#7>", line 6, in insercion
    if valor<a[i]:
NameError: name 'a' is not defined
>>> def insercion(A):
  for i in range(len(A)):
   for j in range(i,0,-1):
    if(A[j-1]>A[j]):
      aux=A[j]
      A[j]=A[j-1]
      A[j-1]=aux
  
  print(A)

>>> A=[6,5,3,1,8,7,2,4]
>>> print(A)
[6, 5, 3, 1, 8, 7, 2, 4]
>>> insercion(A)
[1, 2, 3, 4, 5, 6, 7, 8]
>>> 
