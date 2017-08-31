a=0
def minimo(cjt):
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

			
def ordenamiento(cjt):
	aux=cjt
	result=[]
	for i in range(0,len(cjt)):
		m=minimo(aux)
		result.append(aux[m])
		return result

	
import random
p=random.sample(range(2,102),100)
a=0
print(p)

print(min(p))

print(a)
 
© 2017 GitHub, Inc.
Terms
Privacy
Security
Status
Help
Contact GitHub
API
Training
Shop
Blog
