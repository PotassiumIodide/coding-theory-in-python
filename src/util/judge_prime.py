import random

def fermat_test(q) -> bool:
    q = abs(q)
    if q == 2: return True
    if q < 2 or q&1 == 0: return False
    return pow(2, q-1, q) == 1


def improved_fermat_test(q, k=100) -> bool:
    q = abs(q)
    if q == 2: return True
    if q < 2 or q&1 == 0: return False
    for i in range(3,k):
        x,y = q,i
        while y:
            x, y =  y, x % y
        if x != 1: continue
        if pow(i, q-1, q) != 1:
            return False
    return True


def miller_rabin_test(q,k=50):
    q = abs(q)
    # Process in advance some numbers which are not worth calculated.
    if q == 2: return True
    if q < 2 or q&1 == 0: return False

    # Set n-1=2^s*d, where a is an integer and d is odd, and then find the d.
    d = (q-1)>>1
    while d&1 == 0:
        d >>= 1
    
    # Repeat the judge k times.
    for i in range(k):
        a = random.randint(1,q-1)
        t = d
        y = pow(a,t,q)
        # Check all range in [0,s-1]
        while t != q-1 and y != 1 and y != q-1: 
            y = pow(y,2,q)
            t <<= 1
        if y != q-1 and t&1 == 0:
            return False
    return True