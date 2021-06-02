def divisiable_of_5():
	a=[15,5,10,12,13,14]
	i=0
	list=[]
	while i<len(a):
		if a[i]%5==0:
			list.append(a[i])
		i+=1
	return list
c=divisiable_of_5()
def greater_than_10(e):
	j=0
	list2=[]
	while j<len(e):
		if e[j]>=10:
			list2.append(e[j])
		j+=1
	print(list2)
greater_than_10(c)
# this question is 5 divisible and greater 10