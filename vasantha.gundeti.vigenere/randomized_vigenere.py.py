import random
import sys

#--------------------------------------------------        
def keywordFromseed(seed):
    Letters = []
    
    while seed > 0:
        Letters.insert(0,chr((seed % 100) % 26 + 65))
        seed = seed // 100
    return ''.join(Letters)
    
#-----------------------------------------------------	
def buildVigenere(seed):
    random.seed(seed)
    symbols = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\] ^_`abcdefghijklmnopqrstuvwxyz{|}~"""
    #n = len(symbols)
    n = len(symbols)
    vigenere = [[0 for i in range(n)] for i in range(n)]

    #vigenere = [[0 for i in range(n)] for i in range(n)]
    symbols = list(symbols)
    random.shuffle(symbols)
    symbols = ''.join(symbols)
    #print('new symbols:')
    #print(symbols)
    #print(' ')
    
    for sym in symbols:
        random.seed(seed)
        myList = []
    
        for i in range(n):
            r = random.randrange(n)
            
            if r not in myList:
                myList.append(r)
            else:
                while(r in myList):
                    r = random.randrange(n)
            
                myList.append(r)
                               
            while(vigenere[i][r] != 0):
                r = (r + 1) % n
            
            vigenere[i][r] = sym
            
    return vigenere
#------------------------------------------------------------------
#function for encryption of message using key
def encrypt(message,seed):
	key=keywordFromseed(seed)
	vigenere=buildVigenere(seed)
	cipherText = ""
	i=0
	for i in range(len(message)):
		mi = i
		ki = i % len(key)
		col = ord(message[mi]) - 32
		row = ord(key[ki]) - 32
		cipherText = cipherText + vigenere[row][col]
	return cipherText

	
#--------------------------------------------------------------------  
def decrypt(cipherText,key,ki,emi,vigenere):
	#key=keywordFromseed(seed)
	row = ord(key[ki])-32
	message = cipherText[emi]
	symbols = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\] ^_`abcdefghijklmnopqrstuvwxyz{|}~"""
	i = 0
	n=len(symbols)
	#while(i<n):
	for i in range(n):
		if cipherText[emi]==vigenere[row][i]:
			decryptchar=chr(i+32)
			return(decryptchar)
			#return vigenere[i][0]
			i += 1
   

#function for decryption of ciphertext into plaintext using key
def m_decrypt(cipherText,seed):
	Dec_Text = ""
	key=keywordFromseed(seed)
	vigenere=buildVigenere(seed)
	i=0
	for i in range(len(cipherText)):
		emi = i
		ki = i % len(key)
    #print(message[i])
		if ord(cipherText[i]) == 32:
			Dec_Text = Dec_Text + ' '
		else:
			Dec_Text = Dec_Text + decrypt(cipherText,key,ki,emi,vigenere)
	return Dec_Text
	
