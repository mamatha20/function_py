def showNumbers(limit):
    i=0
    while i<=limit:
        if i%2==0:
            print(i,"even")
        else:
            print(i,"odd")
        i+=1
showNumbers(limit=int(input("enter number"))) 
#even and odd (Q.4 saral)