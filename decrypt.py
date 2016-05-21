#mohamedm2_tyutyunnykd
# This code decrypts Caesar ciphers

def fshift(x, y, z): # This function compares the shifts of e,a, and t and finds the shift or quits.
    if x == y:
        x= int(y)  
    elif x == z:
        x = int(z)
    else:
        print("This code is unbreakable by this program")
        quit()
    return x  
    
    
def fdecoder( e, f): # This function decrypts all of the letters using the correct shift
    d = chr((((e-97) - f) % 26 ) + 97)
    return d 
    
	
def main ():
	decoded = open("decoded.txt", "w")
	fileName ="encoded.txt"
	myfile = open(fileName)
	eline = myfile.readline()
	
	elist =[]
	while eline: # converts file into a string, and a list of words
		elist.append(eline)
		eline = myfile.readline()
	myfile.close()
	estring = ''.join(elist)
	
	estring3 = estring 
	# This leaves only lower case letters in the string estring2
	estring2 = estring.strip() 
	estring2 = estring2.lower()
	estring2 = estring2.replace(" ", "")
	estring2 = estring2.replace(".", "")
	estring2 = estring2.replace(",", "")
	esrting2 = estring2.replace("-", "")
	
	nlist = [ord(c) for c in estring2] # this converts all of the letters into numbers
	import statistics
	for c in nlist:
		nlist = sorted(nlist)
		findnumber = int(statistics.mode(nlist)) # finds the mode and assigns it to findnumber
		
		nlist2 = [y for y in nlist if y != findnumber] # deletes the the mode
		nlist2 = sorted(nlist2)
		findnumber2 = int(statistics.mode(nlist2)) # finds the second most common number and assigns to findnumber2
		
	if 101 - findnumber > 0: # shift of most common letter from e
		shift = ((123-101) + (findnumber - 97))
	else:
		shift = abs(101 - findnumber)

	shift2 = abs(97 - findnumber2) # finds the shift of the second most common letter from a

	if 116 - findnumber2 > 0: # finds the shift of the second most common letter from t
		shift3 = ((123-116) + (findnumber2 - 97))
	else: 
		shift3 = abs(116 - findernumber2)
		
	s1 = shift
	s2 = shift2
	s3 = shift3
	shift = fshift(s1, s2, s3) # uses the function fshift to find the shift
	
	decodedlist =[]

	estring3 = estring3.lower()

	nlist2 = [ord(c) for c in estring3] # this creates a new list with all characters converted to numbers
	for c in nlist2:
		if 97<= c <= 122: # shifts only the letters, and adds to decodedlist
			n = int(c)
			sh = shift
			decode = fdecoder(n, sh)
			decodedlist.append(decode)
		else:
			n = chr(int(c)) # convets all characters that are not between a-z back to letters and adds them to decodedlist
			decodedlist.append(n)

        
	decodedlist = ''.join(decodedlist) # this joins all the strings in decodedlist
	decoded.write(decodedlist) # this writes decodedlist to the new file decode.txt
main()
