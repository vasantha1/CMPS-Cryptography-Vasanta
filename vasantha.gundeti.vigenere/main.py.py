##########################################
#Name:Vasantha Gundeti
#Class:CMPS 5363 Cryptography
#Date:29 july 2015
#Program 2-Randomized Vigenere cipher
##########################################

import argparse
import randomized_vigenere as rv


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-m", "--mode", dest="mode", default = "encrypt", help="Encrypt or Decrypt")
	parser.add_argument("-i", "--inputfile", dest="inputFile", help="Input Name")
	parser.add_argument("-o", "--outputfile", dest="outputFile", help="Output Name")
	parser.add_argument("-s", "--seed", dest="seed",help="Integer seed")
	args = parser.parse_args()
	
	seed=args.seed
	f = open(args.inputFile,'r')
	message = f.read()
	#print(message)
	#table = rv.Vigenere(seed)
	#table.setmessage(message)
    
	if(args.mode == 'encrypt'):
		table=rv.encrypt(message,int(seed))
		#data = rv.encrypt(message,seed)
		o = open(args.outputFile,'w')
		o.write(str(table))
		o.close()
    
	else:
		table=rv.m_decrypt(message,int(seed))
		#data = rv.decrypt(cipherText,seed)
		o = open(args.outputFile,'w')
		
		o.write(str(table))
		o.close()
    
    
#print(table.seed)
#print(table.message)



if __name__ == '__main__':
    main()
    
