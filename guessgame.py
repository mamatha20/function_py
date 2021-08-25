
def sn():
    a=(input("enter a sn:"))
    a.split()
    print(a)
    gn(a)
def result(clue,a):
    while True:
        if clue==a:
            print("congratulations ur gn is succefully matched")
        else:
            print("oops ur loosed this game")
        p_a=input("do u want play again(y or n):")
        if p_a=="y":
            sn()
        elif p_a=="n":
            print("thank you.....!")
            break
                            
def gn(a):
    print("the len of sn is 3 only")
    i=0
    c=0
    clue=""
    while c<10:
        gn=(input('entera a gn:'))
        gn.split()
        print(gn)
        if gn[i] in a:
            if gn.index(gn[i])==a.index(gn[i]):
                print(gn[i],"number is matched with correct position")
                clue=clue+gn[i]
                i=i+1
                if gn==a:
                    result(clue,a)