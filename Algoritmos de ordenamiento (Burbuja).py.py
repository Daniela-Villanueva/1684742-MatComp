Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def burbuja(B):
   for i in range(1,len(B)):
       for j in range(0,len(B)):
           if(B[j+1]):
               aux=B[j]:
               B[j]=B[j+1]:
               B[j+1]=aux:
		       
SyntaxError: invalid syntax
>>> def burbuja(B):
   for i in range(1,len(B)):
       for j in range(0,len(B)):
           if(B[j+1]):
               aux=B[j]
               B[j]=B[j+1]
               B[j+1]=aux

               
>>> print(B)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(B)
NameError: name 'B' is not defined
>>> B=[]
>>> def burbuja(B):
   for i in range(1,len(B)):
       for j in range(0,len(B)):
           if(B[j+1]):
               aux=B[j]
               B[j]=B[j+1]
               B[j+1]=aux

               
>>> print(B)
[]
>>> B=[6,5,3,1,8,7,2,4]
>>> def burbuja(B):
   for i in range(1,len(B)):
       for j in range(0,len(B)):
           if(B[j+1]):
               aux=B[j]
               B[j]=B[j+1]
               B[j+1]=aux

               
>>> print(B)
[6, 5, 3, 1, 8, 7, 2, 4]
>>> B=[6,5,3,1,8,7,2,4]
>>> def burbuja(B):
   for i in range(1,len(B)):
       for j in range(0,len(B)):
           if(B[j+1]):
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
[5, 3, 1, 8, 6, 7, 2, 4]
[5, 3, 1, 8, 7, 6, 2, 4]
[5, 3, 1, 8, 7, 2, 6, 4]
[5, 3, 1, 8, 7, 2, 4, 6]
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    burbuja(B)
  File "<pyshell#16>", line 4, in burbuja
    if(B[j+1]):
IndexError: list index out of range
>>> B=[6,5,3,1,8,7,2,4]B=[6,5,3,1,8,7,2,4]
SyntaxError: invalid syntax
>>> def burbuja(B):
   for i in range(1,len(B)):
       for j in range(0,len(B)):
           if(B[j+1]):
               aux=B[j]
               B[j]=B[j+1]
               B[j+1]=aux

    print(B)

B=[6,5,3,1,8,7,2,4]
print(B)
burbuja(B)
SyntaxError: unindent does not match any outer indentation level
>>> 
>>> def burbuja(B):
   for i in range(1,len(B)):
       for j in range(0,len(B)):
           if(B[j+1]):
               aux=B[j]
               B[j]=B[j+1]
               B[j+1]=aux

    print(B)
    
SyntaxError: unindent does not match any outer indentation level
>>> 
>>> def burbuja(B):
   for i in range(1,len(B)-1):
       for j in range(0,len(B)):
           if(B[j+1]<B[j]):
               aux=B[j]
               B[j]=B[j+1]
               B[j+1]=aux

    print(B)

B=[6,5,3,1,8,7,2,4]
print(B)
burbuja(B)
SyntaxError: unindent does not match any outer indentation level
>>> def burbuja(B):
   for i in range(1,len(B)-1):
       for j in range(0,len(B)):
           if(B[j+1]<B[j]):
               aux=B[j]
               B[j]=B[j+1]
               B[j+1]=aux

    print(B)def burbuja(B):
       for i in range(1,len(B)-1):
           for j in range(0,len(B)):
               if(B[j+1]<B[j]):
                   aux=B[j]
                   B[j]=B[j+1]
                   B[j+1]=aux

        print(B)
        
SyntaxError: unindent does not match any outer indentation level
>>> def burbuja(B):
   for i in range(1,len(B)-1):
       for j in range(0,len(B)):
           if(B[j+1]<B[j]):
               aux=B[j]
               B[j]=B[j+1]
               B[j+1]=aux

               
>>> print(B)
[5, 3, 1, 8, 7, 2, 4, 6]
>>> B=[6,5,3,1,8,7,2,4]
print(B)
burbuja(B)
SyntaxError: multiple statements found while compiling a single statement
>>> def burbuja(B):
   for i in range(1,len(B)-1):
       for j in range(0,len(B)):
           if(B[j+1]<B[j]):
               aux=B[j]
               B[j]=B[j+1]
               B[j+1]=aux

>>> print(B)
[5, 3, 1, 8, 7, 2, 4, 6]
>>> B=[6,5,3,1,8,7,2,4]
>>> print(B)
[6, 5, 3, 1, 8, 7, 2, 4]
>>> burbuja(B)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    burbuja(B)
  File "<pyshell#31>", line 4, in burbuja
    if(B[j+1]<B[j]):
IndexError: list index out of range
>>> def burbuja(B):
   for i in range(1,len(B)-1):
       for j in range(0,len(B)):
           if(B[j+1]<B[j]):
               aux=B[j]
               B[j]=B[j+1]
               B[j+1]=aux

               
>>> 
>>> def burbuja(B):
   for i in range(1,len(B)-1):
       for j in range(0,len(B)):
           if(B[j+1]<B[j]):
               aux=B[j]
               B[j]=B[j+1]
               B[j+1]=aux

    print(B)

SyntaxError: unindent does not match any outer indentation level
>>> B=[6,5,3,1,8,7,2,4]
>>> print(B)
[6, 5, 3, 1, 8, 7, 2, 4]
>>> burbuja(B)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    burbuja(B)
  File "<pyshell#37>", line 4, in burbuja
    if(B[j+1]<B[j]):
IndexError: list index out of range
>>> def burbuja(B):
   for i in range(1,len(B)):
       for j in range(0,len(B)-1):
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
