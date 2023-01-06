'''
Let n = 26, and let M = C = Z/26Z. Define an Affine Cipher as follows.
Encipher(m) = 7m + 5 = c ∈ Z/26Z, and since inverse of 7 ≡ 15 (mod 26),
Decipher(c) = 15(c − 5) = 15c − 23 ∈ Z/26Z = M.
'''

numbertoletter={
    0:'a',
1:'b',
2:'c',
3:'d',
4:'e',
5:'f',
6:'g',
7:'h',
8:'i',
9:'j',
10:'k',
11:'l',
12:'m',
13:'n',
14:'o',
15:'p',
16:'q',
17:'r',
18:'s',
19:'t',
20:'u',
21:'v',
22:'w',
23:'x',
24:'y',
25:'z'}


def affine_cipher(digit):
   return((7*digit+5)%26)

def affine_decipher(digit):
   return((15*digit-23)%26)




input_array=[
    [5,4,4,13,15,9,7,8,25,18,8,2,7,3,7,1,8,7,20,18,14,20,25,18,8],
    [25,18,4,17,5,14,20,7,7,1,25,15,4,18,7,22,7,20,21,20,25,3,1,25,4,0],
    [7,22,7,20,17,1,9,18,9,1,8,2,7,20,7,1,15,4,8,25,14,5,19,25,4,4,5,12,25,20,5,8,9,25,18],
    [8,2,7,3,2,9,8,7,11,5,18,1,12,15,20,0,25,18]]
ans=''


for input in input_array:
 ans=''
 for i in input:
   deciphered_digit=affine_decipher(i)
   ans=ans+(numbertoletter[deciphered_digit])
 print(ans)

'''
'''
Let n = 26, and let M = C = Z/26Z. Define an Affine Cipher as follows.
Encipher(m) = 7m + 5 = c ∈ Z/26Z, and since inverse of 7 ≡ 15 (mod 26),
Decipher(c) = 15(c − 5) = 15c − 23 ∈ Z/26Z = M.
'''

numbertoletter={
    0:'a',
1:'b',
2:'c',
3:'d',
4:'e',
5:'f',
6:'g',
7:'h',
8:'i',
9:'j',
10:'k',
11:'l',
12:'m',
13:'n',
14:'o',
15:'p',
16:'q',
17:'r',
18:'s',
19:'t',
20:'u',
21:'v',
22:'w',
23:'x',
24:'y',
25:'z'}


def affine_cipher(digit):
   return((7*digit+5)%26)

def affine_decipher(digit):
   return((15*digit-23)%26)

input_array=[
    [5,4,4,13,15,9,7,8,25,18,8,2,7,3,7,1,8,7,20,18,14,20,25,18,8],
    [25,18,4,17,5,14,20,7,7,1,25,15,4,18,7,22,7,20,21,20,25,3,1,25,4,0],
    [7,22,7,20,17,1,9,18,9,1,8,2,7,20,7,1,15,4,8,25,14,5,19,25,4,4,5,12,25,20,5,8,9,25,18],
    [8,2,7,3,2,9,8,7,11,5,18,1,12,15,20,0,25,18]]
ans=''

for input in input_array:
 ans=''
 for i in input:
   deciphered_digit=affine_decipher(i)
   ans=ans+(numbertoletter[deciphered_digit])
 print(ans)
 
'''
allquietonthewesternfront
onlyafreesoulnevergrowsold
everysinistheresultofacollaboration
thewhitemansburden
'''
