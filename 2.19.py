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


#take the result and turn it into integer bytes
#01100001000110100000100010010000010100011010000100
solution=[0b01100,
0b00100,
0b01101,
0b00000,
0b10001,
0b00100,
0b00010,
0b10001,
0b10100,
0b00100]

for i in solution:
    print (numbertoletter[i])

#turn the result into int bytes
#take 5 digits of the result and append 0b to the start
#01011000011010010011011000000001101010001001001010010000110100011
#01011000011010010011011000000001101010001001001010010000110100011

solution = [0b01011,
0b00001,
0b10100,
0b10011,
0b01100,
0b00000,
0b01101,
0b01000,
0b10010,
0b01010,
0b01000,
0b01101,
0b00011]

for i in solution:
    print (numbertoletter[i])
    
#plaintext string is 'Man is cruel but man is kind'
