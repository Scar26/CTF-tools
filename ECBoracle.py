from pwn import *

r = remote('crypto.chal.csaw.io', 1003)

blength = 0

r.recvline()
r.sendline('a')
r.recvline()
r.recvline()


print '###################################'
print 'Calculating block length'
print '  '
for i in range(100):
     r.sendline('a'*i) 
     r.recvline()
     a1 = r.recvline()
     r.sendline('a'*(i+1))
     r.recvline()
     a2 = r.recvline()
     if a1[:128] == a2[:128]:
             print "block length : " + str(i)
             blength = i
             break

flag = ''


flag = 'flag{y0u_kn0w_h0w_B10cks'

for k in range(25,blength+1):
        pload = 'a'*(blength-k)
        r.sendline(pload)
        r.recvline()
        h1 = r.recvline()
        for j in range(32,127):
                r.sendline(pload +flag+ chr(j))
                r.recvline()
                hj = r.recvline()
                if hj[:128] == h1[:128]:
                        flag += chr(j)
                        print flag
                        break
