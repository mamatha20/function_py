def multiples(limit):
    i=0
    sum=0
    while i<=limit:
        if i%3==0:
            sum=sum+i
        if i%5==0:
            sum=sum+i
        
        i+=1
    print(sum)    
multiples(limit=int(input("enter number"))) #Q.5 SARAL