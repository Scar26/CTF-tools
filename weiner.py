from Crypto.PublicKey import RSA
from Crypto.Util.number import *
from sympy import *
import gmpy

def cf_expansion(n,d):
	a = []
	q = n//d
	r = n%d
	a.append(q)
	while r!=0:
		n,d = d,r
		q = n//d
		r = n%d
		a.append(q)
	return a

def convergents(e):
    n = [] 
    d = [] 

    for i in range(len(e)):
        if i == 0:
            ni = e[i]
            di = 1
        elif i == 1:
            ni = e[i]*e[i-1] + 1
            di = e[i]
        else:
            ni = e[i]*n[i-1] + n[i-2]
            di = e[i]*d[i-1] + d[i-2]

        n.append(ni)
        d.append(di)
        yield (ni, di)


e = 10313126904907659154044035721366030299232309115307337238069263116199564176949082532958372172524781222401197622749859873567807461466595706294618003558061807305009089579192976992088381679811566030775373564473171308640498756926134368136999882295511187054033765297409191882443609170411704473261992833838123818561
n = 109687016872270895485002266970328712710286894269700902397167363980261414713520289185733988489249689544386122785160267207726938916283070886632648506845942355973707843524843601791935989196521515362641012890949012806874239146986434010907679833739235439641970444255192335936390330185114634466512110682757108170303
c = 95417048455606507206344555772522388669483613888347553614999898346097063082564960534143412714175496839814163484993167584876285328542038828829471182631204991424293520967432055502995782228891541107492929962249088449543437905078172770522604827502428360779940479314653358332616588023267286852819042394155188966503




cf = cf_expansion(e,n)
cons = convergents(cf)

for k,d in cons:
	if k == 0:
		continue
	phi = (e*d - 1)//k
	p = Symbol('p', integer=True)
	roots = solve(p**2 + (phi - n - 1)*p + n, p)
	if len(roots) == 2 and roots[0]*roots[1] == n:
		print('found p and q')
		print('#########################')
		p = roots[0]
		q = roots[1]
		break

phi = (p-1)*(q-1)
d = inverse(e,phi)
flag = pow(c,d,n)

print(f'The flag is : {bytearray.fromhex(hex(flag)[2:])}')