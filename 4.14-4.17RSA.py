#c is ciphertext
'''''''''''''''
you have p and q.
n=p * q
r or 0n is (p-1)*(q-1)
e is also given
m is the message
 
d is something
d=pow(e,-1,r)
 
m=pow(c,d,n)
c=pow(m,e,n)
 
'''''''''''''''
 
#4.14. (p,q) = (167,547), n = 91349, e = 5, and c ≡ 88291(mod n).
p=167
q=547
e=5
n=91349
c=88291
r=(p-1)*(q-1)
d=pow(e,-1,r)
m=pow(c,d,n)
print (m)
 
#4.16. (p, q) = (367, 911), n = 334337, e = 17, and c ≡ 226756 (mod n). 
p=367
q=911
e=17
n=334337
c=226756
r=(p-1)*(q-1)
d=pow(e,-1,r)
m=pow(c,d,n)
print (m)
#4.17. (p, q) = (1187, 1481), n = 1757947, e = 13, and c ≡ 1757118 (mod n).
p=1187
q=1481
e=13
n=1757947
c=1757118
r=(p-1)*(q-1)
d=pow(e,-1,r)
m=pow(c,d,n)
print (m)
 
 
#4.15. (p, q) = (211, 691), n = 145801, e = 11, and c ≡ 121919 (mod n). 
p=211
q=691
e=11
n=145801
c=121919
r=(p-1)*(q-1)
d=pow(e,-1,r)
m=pow(121919,d,n)
print (m)
 
#4.17. (p, q) = (1187, 1481), n = 1757947, e = 13, and c ≡ 1757118 (mod n).
p=1187
q=1481
e=13
n=p*q
c=1754118
r=(p-1)*(q-1)
d=pow(e,-1,r)
m=pow(c,d,n)
print (m)
