
# Online Python - IDE, Editor, Compiler, Interpreter
'''
'''
beta=pow(2,251,3469)
print (beta)
#gamma=pow(((1121−(153*2142))*251),-1,3468)
#print (gamma)
print (((1121-(153*2142))*(pow(251,-1,3468))))
print ( (100-127*29)*431%466 )
print ((1121-153*2142)*2639%3468)

print ((pow(2501,2142)*pow(2142,1849))%3469)
print ((pow(2,1121))%3469)

#public key is (p,alpha,y)
# message is m
# signature is (beta,gamma)

‘’’
To check if message is signed these two should be equal
pow(y,beta)*pow(beta,gamma)%p
pow(alpha,m)%p
‘’’

#4.34
p=641
alpha=3
y=88
beta=480
gamma=532
m=121

print(pow(y,beta)*pow(beta,gamma)%p)
print(pow(alpha,m)%p)

#4.35
p=3023
alpha=5
y=2391
beta=335
gamma=2367
m=203

print(pow(y,beta)*pow(beta,gamma)%p)
print(pow(alpha,m)%p)

#4.36
p=5023
alpha=3
y=3796
beta=2294
gamma=3740
m=444

print(pow(y,beta)*pow(beta,gamma)%p)
print(pow(alpha,m)%p)

#4.37
p=7481
alpha=6
y=5979
beta=1723
gamma=7045
m=487

print(pow(y,beta)*pow(beta,gamma)%p)
print(pow(alpha,m)%p)


