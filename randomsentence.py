#tyutyunnykd_mohamedm2
# this code generates random sentences based on imported text using Markov chain method



import sys
import random

def startword(filess): #creates list of start words  used in the beginning of the random sentence
    fileName = filess  #opens textfile 
    myfile = open(fileName)
    eline = myfile.readline()
	
    elist =[]
    while eline: # converts file into a string, and a list of words
        elist.append(eline)
        eline = myfile.readline()
    myfile.close()

    Keylist=[]  #creates list of Key for the dictionary
    for line in elist:
        wordlist = line.split(" ")
        for string in wordlist:
            string=string.strip()
            if string not in Keylist:
                Keylist.append(string)
        
    Startlist=[] 
    for string in Keylist:
        if any(c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for c in string) and string not in Startlist:
            Startlist.append(string)
    return Startlist 
        
        
def Lastword(filess): # function creates a list of words that have !.? in them used to tell the random sentence to stop
    fileName = filess  #opens textfile 
    myfile = open(fileName)
    eline = myfile.readline()
	
    elist =[]
    while eline: # converts file into a string, and a list of words
        elist.append(eline)
        eline = myfile.readline()
    myfile.close()

    Keylist=[]  #creates list of Key for the dictionary
    for line in elist:
        wordlist = line.split(" ")
        for string in wordlist:
            string=string.strip()
            if string not in Keylist:
                Keylist.append(string)
    Endlist=[] #creates list of end words
    for string in Keylist:
        if any(c in ".?!" for c in string) and string not in Endlist:
            Endlist.append(string)
    return Endlist
            
            
def dict(filess): # function creates a dictionary 
    fileName = filess  #opens textfile 
    myfile = open(fileName)
    eline = myfile.readline()
    elist =[]
    while eline: # converts file into a string, and a list of words
        elist.append(eline)
        eline = myfile.readline()
    myfile.close()
        
    Diclist=[] #recreates text so each word is a string
    for line in elist:
        wordlist = line.split(" ")
        for string in wordlist:
            string=string.strip()
            string = string.strip("")
            Diclist.append(string)


    #creates the dictionary 
    s = Diclist
    dic = {}
    svalue=[]
    for i in range(0,len(s)-1):
        wor=s[i]
        nexwor=s[i+1]
        if not(wor in dic.keys()):
            dic[wor] = [nexwor]
        else:
            dic[wor].append(nexwor)
    return dic


def create(filess): # function creates the random sentence
    file = filess  #opens textfile 
    
    dic = dict(file)
    Startlist = startword(file)
    Endlist = Lastword(file)
    
    RanSen=[]
    randomstart= random.choice(Startlist)
    start = randomstart
    RanSen.append(start)
    while (len(RanSen)-1) < 50 : # runs code while the list contain the sentence is less than 50 
        for i in (len(RanSen)-1,len(RanSen)):
            x = RanSen[i]
            newl = dic[x]
            neww = random.choice(newl)
            if neww in Endlist and 4<=len(RanSen)-1:  # stops the list if it contains !?. only if its longer than 4 characters
                RanSen.append(neww)
                RanSen = " ".join(RanSen)
                print(RanSen)
                quit()
            else:
                RanSen.append(neww)
    return RanSen









# main function 
def main(): 
    filex = sys.argv[1]
    inputs = input("Enter 'c' to continue of 'q' to quit: ")

    
    
    found = True

    if  inputs != "q":
        found = False
        randomsentence = create(filex)
        print(RanSen)
        inputs = input("Enter 'c' to continue of 'q' to quit: ")
    if not Found:
        quit()
    

    
main()
   
  
    






        
     



    

    
    
            
    
    
     
       

    
 
      
    
    
    
    
    
    
    
    
         


    
    

    



