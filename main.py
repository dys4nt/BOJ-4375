while True:
    try:
        n = int(input())
    except EOFError:
        break
    i=1
    while i:
        a = (10**i-1)//9
        if a%n==0:
            print(i)
            break
        i+=1