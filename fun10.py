def string_reverse(n):
    str1=''
    index=len(n)
    while index>0:
        str1+=n[index-1]
        index-=1
    return str1

print(string_reverse('abncgu123'))

    #reverse