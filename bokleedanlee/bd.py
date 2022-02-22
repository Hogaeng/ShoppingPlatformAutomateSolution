def boklee(monthly,rate,n,s):
    rate/=100
    total=s
    interest=0
    for i in range(n):
        total+=monthly
        total*=(1+rate/(n-i))
    interest=(total-n*monthly)
    total=n*monthly
    return total+interest*(1-0.154)
def danlee(monthly,rate,n,s):
    rate/=100
    total=s
    interest=0
    for i in range(n):
        total+=monthly
        interest+=monthly*rate/(n-i)
    return total+interest*(1-0.154)