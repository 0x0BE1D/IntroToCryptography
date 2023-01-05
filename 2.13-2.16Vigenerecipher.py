
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


#create the vigenere cipher
#create all the rows and append them as a list. So we have a list of rows.

vigcipher=[]

for j in range(26):
 newlist=[]
 for i in range(26):
    newlist.append((i+j)%26)
 #print (newlist)
 vigcipher.append(newlist)

#to print the numbers in vigenere cipher
#for i in range(len(vigcipher)):
 #   print(vigcipher[i])



def deciphertext(letters):

    #this is the key
    key=ord('z')-96-1
    
    #converting the letters to numbers
    numbers = []
    for letter in letters:
        number = ord(letter) - 96-1
        numbers.append(number)

    ans=''

    #deciphering the numbers. As numbers.
    for i in range(len(letters)):
        pos=0
        done = False
        for k in range(len(vigcipher[key])):
            if (vigcipher[key][k]) == numbers[i]:
                pos = k
            
        
        key=pos
        ans=ans+numbertoletter[key]
    
    print (ans)

letters_array = ["kzjzmasksvqrtbwrwfrv","lmncgfddgwwtvnzurglahdgww","rltkoptnjyjdbgklna","ndedfknhvbrgasgur"]
letters=''
for letters in letters_array:
    deciphertext(letters)

'''
loveisakindofwarfare
manproposesbutgoddisposes
stakelifeupontruth
opportunityisagod
'''
