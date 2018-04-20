'''
Created on Mar 15, 2016

@author: ugur
'''
import nltk
import re
import difflib
import collections
from deasciifier import Deasciifier
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
text_file = open(filename, "r")
text_file_readlines=text_file.readlines()


before_normalize=' '.join(text_file_readlines)
before_normalize=re.sub(' +',' ',before_normalize)
#print (before_normalize)

print ("##################################################")

aaa=before_normalize.split(" ")
#print (aaa)
for i in range(len(aaa)):
    ####### HTTPLERİ TEMİZLEME
    if aaa[i].find("http")!= -1:
        if aaa[i].startswith("http"):
            if aaa[i].endswith("\n"):
                aaa[i]="\n"
            else :
                aaa[i]=""
        else :
            aaa[i]="" 
    ####### � TEMİZLEME           
    elif aaa[i].find("�")!=-1:
        if aaa[i].startswith("�"):
            if aaa[i].endswith("\n"):
                aaa[i]="\n"
            else :
                aaa[i]=aaa[i].replace("�","") 
        else :
                aaa[i]=aaa[i].replace("�","")
    ####### ☀ TEMİZLEME 
    elif aaa[i].find("☀")!=-1:
        if aaa[i].startswith("☀"):
            if aaa[i].endswith("\n"):
                aaa[i]="\n"
            else :
                aaa[i]=aaa[i].replace("☀","") 
        else :
                aaa[i]=aaa[i].replace("☀","") 
                                  
    ####### @ TEMİZLEME           
    elif aaa[i].find("@")!=-1:
        if aaa[i].startswith("@"):
            if aaa[i].endswith("\n"):
                aaa[i]="\n"
            else :
                aaa[i]="" 
        if aaa[i].startswith("@ "):
            if aaa[i].endswith("\n"):
                aaa[i]="\n"
            else :
                aaa[i]=""         
        elif (aaa[i].startswith("(@") or aaa[i].startswith("( @")):  
            if aaa[i].endswith("\n"):
                aaa[i]="\n"
            else :
                aaa[i]=""                    
       
        else :
            aaa[i]=""         
   
    ####### RT TEMİZLEME
    elif aaa[i].find("RT")!=-1:        
        if aaa[i].startswith("RT"):  
            if aaa[i].endswith("\n"):
                aaa[i]="\n"
            else :
                aaa[i]=""       
        else :
            aaa[i]="" 
                    
    ####### # TEMİZLEME
    elif aaa[i].find("#")!=-1:        
        if aaa[i].startswith("#"):  
            if aaa[i].endswith("\n"):
                aaa[i]="\n"
            else :
                aaa[i]=""       
        else :
            aaa[i]=""
    
    ####### " TEMİZLEME
    elif aaa[i].find('"')!=-1:   
        if aaa[i].startswith('"'): 
            if aaa[i].endswith(":"):
                aaa[i]=""
            else :
                aaa[i]=aaa[i].replace('"',"")  
        else :
                aaa[i]=aaa[i].replace('"',"")
                
                
    ####### ✌ TEMİZLEME 
    elif aaa[i].find("✌")!=-1:
        if aaa[i].startswith("✌"):
            if aaa[i].endswith("\n"):
                aaa[i]="\n"
            else :
                aaa[i]=aaa[i].replace("✌","") 
        else :
                aaa[i]=aaa[i].replace("✌","") 
    ####### ✌ TEMİZLEME 
    elif aaa[i].find("✌")!=-1:
        if aaa[i].startswith("✌"):
            if aaa[i].endswith("\n"):
                aaa[i]="\n"
            else :
                aaa[i]=aaa[i].replace("✌","") 
        else :
                aaa[i]=aaa[i].replace("✌","")             
    
    ####### "☔️" TEMİZLEME 
    elif aaa[i].find("☔️")!=-1:
        if aaa[i].startswith("☔️"):
            if aaa[i].endswith("\n"):
                aaa[i]="\n"
            else :
                aaa[i]=aaa[i].replace("☔️","") 
        else :
                aaa[i]=aaa[i].replace("☔️","")                         
                        
    ####### . TEMİZLEME
    elif aaa[i].find(".")!= -1:
        if aaa[i].startswith("."):
            if aaa[i].endswith("\n"):
                aaa[i]="\n"
            else :
                aaa[i]=""
        elif aaa[i].endswith("."):
            if aaa[i].endswith("\n"):
                aaa[i]="\n"
            else :
                aaa[i]=aaa[i].replace(".","")       
        else :
            aaa[i]=aaa[i].replace(".","")    
    
    ####### ! TEMİZLEME
    elif aaa[i].find("!")!= -1:
        if aaa[i].startswith("!"):
            if aaa[i].endswith("\n"):
                aaa[i]="\n"
            else :
                aaa[i]=aaa[i].replace("!","")
        elif aaa[i].endswith("!"):
            aaa[i]=aaa[i].replace("!","")
        else:
            aaa[i]=aaa[i].replace("!","")      
    ####### ? TEMİZLEME
    elif aaa[i].find('?')!=-1:   
        if aaa[i].startswith("?"): 
            aaa[i]=aaa[i].replace("?","") 
        elif aaa[i].endswith("?"): 
            aaa[i]=aaa[i].replace("?","")  
        else: 
            aaa[i]=aaa[i].replace("?","") 
            
    ####### , TEMİZLEME
    elif aaa[i].find(',')!=-1:   
        if aaa[i].startswith(","): 
            aaa[i]=aaa[i].replace(",","") 
        elif aaa[i].endswith(","): 
            aaa[i]=aaa[i].replace(",","")  
        else: 
            aaa[i]=aaa[i].replace(",","")  
    ####### \ TEMİZLEME
    elif aaa[i].find("'\'")!=-1: 
        if aaa[i].startswith("'\'"):
            aaa[i]=aaa[i].replace(aaa[i],"") 
        elif aaa[i].endswith("'\'"): 
            aaa[i]=aaa[i].replace(aaa[i],"\n")  
        else: 
            aaa[i]=aaa[i].replace(aaa[i],"")                      
    ####### w/ TEMİZLEME
    elif aaa[i].find("w/")!=-1: 
        if aaa[i].startswith("w/"):
            aaa[i]=aaa[i].replace(aaa[i],"") 
        elif aaa[i].endswith("'w/'"): 
            aaa[i]=aaa[i].replace(aaa[i],"\n")  
        else: 
            aaa[i]=aaa[i].replace(aaa[i],"") 
    ####### ” TEMİZLEME
    elif aaa[i].find("”")!=-1: 
        if aaa[i].startswith("”"):
            aaa[i]=aaa[i].replace("”","") 
        elif aaa[i].endswith("”"): 
            aaa[i]=aaa[i].replace("”","\n")  
        else: 
            aaa[i]=aaa[i].replace("”","")                
    ####### “ TEMİZLEME
    elif aaa[i].find("“")!=-1: 
        if aaa[i].startswith("“"):
            if aaa[i].endswith("”"): 
                if aaa[i].endswith("\n"):
                    aaa[i]=aaa[i].replace("”","\n") 
                    aaa[i]=aaa[i].replace("“","")
                else:
                    aaa[i]=aaa[i].replace("”","") 
                    aaa[i]=aaa[i].replace("“","")
            else:
                aaa[i]=aaa[i].replace("”","")               
       
        else: 
            aaa[i]=aaa[i].replace("“","")
    
    ####### ; TEMİZLEME
    elif aaa[i].find(";")!=-1: 
        if aaa[i].startswith(";"):
            aaa[i]=aaa[i].replace(";","") 
        elif aaa[i].endswith(";"):
            if aaa[i].endswith("\n"):
                aaa[i]=aaa[i].replace(";","\n") 
            else:
                aaa[i]=aaa[i].replace(";","")  
        else: 
            aaa[i]=aaa[i].replace(";","")
    
    ####### - TEMİZLEME
    elif aaa[i].find("-")!=-1: 
        if aaa[i].startswith("-"):
            aaa[i]=aaa[i].replace("-"," ") 
        elif aaa[i].endswith("-"): 
            aaa[i]=aaa[i].replace("-","\n")  
        else: 
            aaa[i]=aaa[i].replace("-"," ")                 
    
    ####### ' TEMİZLEME
    elif aaa[i].find("'")!=-1: 
        if aaa[i].startswith("'"):
            if aaa[i].endswith("\n"): 
                aaa[i]=aaa[i].replace("'","\n")
            else:    
                aaa[i]=aaa[i].replace("'","") 
        elif aaa[i].endswith("'"): 
            if aaa[i].endswith("\n"): 
                aaa[i]=aaa[i].replace("'","\n")  
        else: 
            aaa[i]=aaa[i].replace("'","")
    ####### … TEMİZLEME
    elif aaa[i].find("…")!=-1: 
        if aaa[i].startswith("…"):
            if aaa[i].endswith("\n"): 
                aaa[i]=aaa[i].replace("…","\n")
            else:    
                aaa[i]=aaa[i].replace("…","") 
        elif aaa[i].endswith("…"): 
            if aaa[i].endswith("\n"): 
                aaa[i]=aaa[i].replace("…","\n")
            else:
                aaa[i]=aaa[i].replace("…","")     
        else: 
            aaa[i]=aaa[i].replace("…","")                     
    
    ####### ) TEMİZLEME
    elif aaa[i].find(")")!=-1: 
        if aaa[i].startswith(")"):
            if aaa[i].endswith("\n"): 
                aaa[i]=aaa[i].replace(aaa[i],"\n")
            else:    
                aaa[i]=aaa[i].replace(")","") 
        elif aaa[i].endswith(")"): 
            if aaa[i].endswith("\n"): 
                aaa[i]=aaa[i].replace(aaa[i],"\n")
            else:
                aaa[i]=aaa[i].replace(")","")     
        else: 
            aaa[i]=aaa[i].replace(")","")
       
    ####### emoji shortcut TEMİZLEME
    elif aaa[i].find(":")!=-1:
        if aaa[i].startswith(":"):
            if aaa[i].endswith("\n"):
                aaa[i]="\n"
            else :
                aaa[i]=aaa[i].replace(":","") 
        elif aaa[i].endswith(":"):
            if aaa[i].endswith("\n"):
                aaa[i]="\n"
            else :
                aaa[i]=aaa[i].replace(":","")
        else :
            aaa[i]=aaa[i].replace(":","")              
        
        
           
clear_sign=' '.join(aaa)
clear_sign=re.sub(' +',' ',clear_sign)

tweet_nltk=clear_sign.split(" ")
for i in range(len(tweet_nltk)) :
    if "$" in tweet_nltk[i]:
        tweet_nltk[i]=tweet_nltk[i].replace("$","ş")
    elif (tweet_nltk[i]=="aeo" or tweet_nltk[i]=="a.e.o" or tweet_nltk[i]=="a. e. o") :
        tweet_nltk[i]=tweet_nltk[i].replace(tweet_nltk[i],"allaha emanet ol")
    elif (tweet_nltk[i]=="ii" or tweet_nltk[i]=="i i") :
        tweet_nltk[i]=tweet_nltk[i].replace(tweet_nltk[i],"iyi")     
    elif "£" in tweet_nltk[i]:
        tweet_nltk[i]=tweet_nltk[i].replace("£","e")
        
    elif "€" in tweet_nltk[i]:
        tweet_nltk[i]=tweet_nltk[i].replace("€","e")
          
tweet2=' '.join(tweet_nltk)
tweet2=re.sub(' +',' ',tweet2) 
print ("\n\n")  
  

ugur=[]

########### STEP  : EMPHASIZE WORDS

class groupby:
    # [k for k, g in groupby('AAAABBBCCDAABBB')] --> A B C D A B
    # [list(g) for k, g in groupby('AAAABBBCCD')] --> AAAA BBB CC D
    def __init__(self, iterable, key=None):
        if key is None:
            key = lambda x: x
        self.keyfunc = key
        self.it = iter(iterable)
        self.tgtkey = self.currkey = self.currvalue = object()
    def __iter__(self):
        return self
    def __next__(self):
        while self.currkey == self.tgtkey:
            self.currvalue = next(self.it)    # Exit on StopIteration
            self.currkey = self.keyfunc(self.currvalue)
        self.tgtkey = self.currkey
        return (self.currkey, self._grouper(self.tgtkey))
    def _grouper(self, tgtkey):
        while self.currkey == tgtkey:
            yield self.currvalue
            try:
                self.currvalue = next(self.it)
            except StopIteration:
                return
            self.currkey = self.keyfunc(self.currvalue)

for k, g in groupby(tweet2):
    ugur.append(k) 

tweet3="".join(ugur)

#tokenizer = WordPunctTokenizer()
#token = tokenizer.tokenize(tweet3)
token=tweet3.split(" ")
print (token)
for i in range(len(token)) :
    if token[i].startswith("@"):
        token[i] = "@mention[" + token[i] +"]"
    elif token[i].startswith("#"):
        token[i] = "@hashtag[#" + token[i] +"]"
    elif token[i].startswith("w."):
        if token[i].endswith(".com"):
            token[i] = "@url[ww" + token[i] + "]"
    elif token[i].startswith("htp."):
        if token[i].endswith(".com"):
            token[i] = "@url[" + token[i] + "]"        
    elif token[i].endswith("tcem"):
        token[i]=token[i].replace("tcem","deceğim")
    elif token[i].endswith("tçem"):
        token[i]=token[i].replace("tçem","deceğim")    
    elif token[i].endswith("micem"):
        token[i]=token[i].replace("micem","meyeceğim")
    elif token[i].endswith("mıcam"):
        token[i]=token[i].replace("mıcam","mayacağım")
    elif token[i].endswith("rcam"):
        token[i]=token[i].replace("rcam","racağım")
    elif token[i].endswith("pcam"):
        token[i]=token[i].replace("pcam","pacağım")    
    elif token[i].startswith("bi"):
        if token[i].startswith("bir"):
            continue
        else :  
            token[i]=token[i].replace("bi","bir")
    elif token[i].startswith("die"):
        token[i]=token[i].replace("die","diye")

########### STEP  : FORGOTTEN LETTERS IN WORDS

def unforgotten(word):

    text_file = open("turkce_sozluk2.txt", "r")
    asli=text_file.readlines()
    text_file.close()
   # print(len(asli))
    #print("****")
    ugur1="".join(asli)

    ugur1=ugur1.replace(" ","\n")
    ugur1=ugur1.replace(" ","\t")
    ugur1=ugur1.lower()

    ugur2=ugur1.split("\n")

    ugur3=[]        
    [ugur3.append(item) for item, count in collections.Counter(ugur2).items() if count >=1 ]        
    ugur4=[]

    for x in sorted(ugur3):
        ugur4.append(x)
   

    text_file2 = open("turkce_sozluk2.txt", "w")
    for item in ugur4:
        text_file2.write("%s\n" % item)

    text_file.close()    

    ugur5=difflib.get_close_matches(word, ugur4)[0]
    return ugur5

for i in range(len(token)):
    if token[i].find("a")==-1 :
        if token[i].find("e")==-1 :
            if token[i].find("ı")==-1 :
                if token[i].find("i")==-1 :
                    if token[i].find("o")==-1 :
                        if token[i].find("ö")==-1 :
                            if token[i].find("u")==-1 :
                                if token[i].find("ü")==-1 :
                                    if (token[i].find(" ")!=-1 or token[i].find('"')!=-1 or 
                                        token[i].find(",")!=-1 or token[i].find(".")!=-1 or 
                                        token[i].find(":)")!=-1 or token[i].find(":(")!=-1 or
                                        token[i].find(":/")!=-1 or token[i].find('(=^..^=)')!=-1 or
                                        token[i].find('(=^.^=)')!=-1 or token[i].find('(N)')!=-1 or
                                        token[i].find('(Y)')!=-1 or token[i].find('(]:{')!=-1 or
                                        token[i].find('(n)')!=-1 or token[i].find('(y)')!=-1 or      
                                        token[i].find('<@%')!=-1 or token[i].find('-_-')!=-1 or      
                                        token[i].find(':"(')!=-1 or token[i].find(":'(")!=-1 or     
                                        token[i].find(':(')!=-1 or token[i].find(':(:)')!=-1 or     
                                        token[i].find(':(|)')!=-1 or token[i].find(':)')!=-1 or   
                                        token[i].find(':*')!=-1 or token[i].find(':-(')!=-1 or 
                                        token[i].find(':-)')!=-1 or token[i].find(':-*')!=-1 or
                                        token[i].find(':-/')!=-1 or token[i].find(':-/')!=-1 or
                                        token[i].find(':-D')!=-1 or token[i].find(':-O')!=-1 or   
                                        token[i].find(':-P')!=-1 or token[i].find(':-S')!=-1 or 
                                        token[i].find("':-\'")!=-1 or token[i].find(':/')!=-1 or
                                        token[i].find(':3')!=-1 or token[i].find(':D')!=-1 or
                                        token[i].find(':O')!=-1 or token[i].find(':P')!=-1 or
                                        token[i].find(':S')!=-1 or token[i].find(':X)')!=-1 or
                                        token[i].find('":\"')!=-1 or token[i].find(':o')!=-1 or
                                        token[i].find(':p')!=-1 or token[i].find(':s')!=-1 or
                                        token[i].find(':|')!=-1 or token[i].find(';)')!=-1 or
                                        token[i].find(';*')!=-1 or token[i].find(';-)')!=-1 or
                                        token[i].find(';-*')!=-1 or token[i].find(';-P')!=-1 or
                                        token[i].find(';-p')!=-1 or token[i].find(';P' )!=-1 or
                                        token[i].find(';_;')!=-1 or token[i].find(';p')!=-1 or
                                        token[i].find('</3')!=-1 or token[i].find('<3')!=-1 or
                                        token[i].find('<\3')!=-1 or token[i].find("='(")!=-1 or
                                        token[i].find('=(' )!=-1 or token[i].find('=)')!=-1 or
                                        token[i].find('=*')!=-1 or token[i].find('=/')!=-1 or
                                        token[i].find('=D')!=-1 or token[i].find('=O')!=-1 or
                                        token[i].find('=P')!=-1 or token[i].find('B)')!=-1 or 
                                        token[i].find('B-)')!=-1 or token[i].find('D:')!=-1 or
                                        token[i].find('O.O')!=-1 or token[i].find('O:)')!=-1 or
                                        token[i].find('O:-)')!=-1 or token[i].find('O=)')!=-1 or
                                        token[i].find('^_^;;')!=-1 or token[i].find('u_u')!=-1 or
                                        token[i].find('}:)')!=-1 or token[i].find('}:-)')!=-1 or
                                        token[i].find('}=)')!=-1 or token[i].find('~@~')!=-1 
                                                                                                                     
                                        ) :
                                        continue
                                    elif token[i].find("\n")!=-1 :
                                        continue 
                                    elif (token[i]=="mrb" or token[i]=="merhb") :
                                        token[i]=token[i].replace(token[i],"merhaba")
                                    elif (token[i]=="nbr" or token[i]=="nabr") :
                                        token[i]=token[i].replace(token[i],"ne haber")                                      
                                    elif (token[i]=="slm" or token[i]=="selm") :
                                        token[i]=token[i].replace(token[i],"selam")                                      
                                    elif token[i]=="glyn" :
                                        token[i]=token[i].replace(token[i],"geliyorsun")
                                    elif token[i]=="ltf" or token[i]=="ltfn" :
                                        token[i]=token[i].replace(token[i],"lütfen")
                                    elif token[i]=="hrkt" :
                                        token[i]=token[i].replace(token[i],"hareket")        
                                    elif token[i]=="slcm" or token[i]=="sylcm" or token[i]=="sylcm" :
                                        token[i]=token[i].replace(token[i],"söyleyeceğim")         
                                    
                                    else : 
                                        token[i]=token[i].replace(token[i],unforgotten(token[i]))
                                        
                                         
                                else:
                                    continue      
                            else:
                                continue    
                        else:
                            continue 
                    else:
                        continue 
                else:
                    continue
            else:
                continue
        else:
            continue
    else:
        continue
        
    
xxx=' '.join(token)
xxx=re.sub(' +',' ',xxx)
print ("\n\n") 

my_ascii_turkish_txt = xxx
deasciifier = Deasciifier(my_ascii_turkish_txt)
my_deasciified_turkish_txt = deasciifier.convert_to_turkish()
print (my_deasciified_turkish_txt)



text_file2 = open("myclean.txt", "w")
text_file2.write(my_deasciified_turkish_txt)
text_file2.close()
print("#########################################")




    
   
    
  
    
    

