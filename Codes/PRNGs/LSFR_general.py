import galois

def LS(seed,n=64):
    f = galois.primitive_poly(2, n, method="min")
    print(f)
    temp=f._coeffs
    poly=[]
    for i in range(1,len(temp)):
        if temp[i]==1:
            poly.append(n-i)

    while (True):
        yield seed
        # print(seed)
        bit=0
        for i in range(len(poly)):
            bit^= (seed>>poly[i])
        bit&=1
        seed = (seed >> 1) | (bit << (n-1))
        # print(((seed ^ (seed >> 62)) & 1) << 63)

