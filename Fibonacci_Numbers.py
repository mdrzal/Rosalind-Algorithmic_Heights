def Fibs(n):
    n=n+1
    A=list()
    for i in range(1,n+1):
        if i ==1:
            A.append(0)
        if i ==2:
            A.append(1)
        if i>2:
            R=A[-2]+A[-1]
            A.append(R)
    return A[-1]
        

Fibs(20)
