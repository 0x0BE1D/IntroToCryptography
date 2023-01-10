'''
Diffie-Helmann Key
'''
def calculate_key(p,alpha,x,y):
    bigY=pow(alpha,y,p)
    key=pow(bigY,x,p)
    print(key)
    
calculate_key(877,2,25,3)
calculate_key(907,2,32,153)
calculate_key(1193,3,69,96)
calculate_key(1471,6,51,22)

'''
794
121
489
1084
'''
