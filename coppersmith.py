
from sage.all import *

# f = (m + x)**e - c
def stereotyped(f, N):
    P.<x> = PolynomialRing(Zmod(N))
    beta = 1
    dd = f.degree()
    epsilon = beta/7
    XX = ceil(N**((beta**2/dd) - epsilon))
    rt = f.small_roots(XX, beta, epsilon)
    return rt

def N-factorize(f, N):
    P.<x> = PolynomialRing(Zmod(N))
    beta = 0.5
    dd = f.degree()
    epsilon = beta/7
    XX = ceil(N**((beta**2/dd) - epsilon))
    rt = f.small_roots(XX, beta, epsilon)
    return rt