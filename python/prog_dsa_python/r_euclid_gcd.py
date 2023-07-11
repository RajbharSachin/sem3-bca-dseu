def regcd(m,n):
    if(m<n):
        (m,n)=(n,m)
    
    if(m%n)==0:
        return n
    else:
        return regcd(n,m%n)