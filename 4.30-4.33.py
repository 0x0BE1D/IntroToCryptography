'''
EL GAMAL Key Generation

m=2132
p=3359
alpha=α=11
a=5
He computes pow(α,a) ≡ 11^5 ≡ 3178 (mod p). 
pow(11,5,3359)=3178                         <---- pow(α,a,p)
Bob’s public key is therefore 
(p, α, αa ) = (3359, 11, 3178)

which Alice downloads from some public database. She chooses b = 69 and computes both
and
α^b ≡ 11^69 ≡ 193 (mod p)
pow(11,69,3359)                             <---- pow(α,b,p)

m(α^(ab)) ≡ 2132 · 3178^69 ≡ 2719 (mod p).
leftside=m*pow(3178,69)
2719=pow(leftside,1,3359)                   <---- m*pow(α,ab) (mod p)

ciphertext=(193,2719)
ciphertext is made of pow(α,b,p) and m*pow(α,ab) (mod p)

To recover message:
1. pow(pow(α,b),p-1-a,p)
2. Take result from previous step: r
    r*m*pow(α,ab) (mod p)     



pow(pow(α,b),p-1-a,p)
Take result from previous step: r
r*c2 (mod p)

ANSWERS:
21
200
233
2112

'''

#4.30. p=1213,a=15,c=(αb,mαab)=(661,193).
c1=661
c2=193
p=1213
a=15
r=pow(c1,(p-1-a),p)
print ((r*c2)%p)


#4.31. p=1973,a=71,c=(αb,mαab)=(596,146).
c1=596
c2=146
p=1973
a=71
r=pow(c1,(p-1-a),p)
print ((r*c2)%p)

#4.32. p=2833,a=17,c=(αb,mαab)=(522,982)
c1=522
c2=982
p=2833
a=17
r=pow(c1,(p-1-a),p)
print ((r*c2)%p)


#4.33. p = 3359, a = 19, c = (αb, mαab) = (1093, 2530).
c1=1093
c2=2530
p=3359
a=19
r=pow(c1,(p-1-a),p)
print ((r*c2)%p)



