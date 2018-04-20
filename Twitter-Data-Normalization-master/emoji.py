'''
Created on Mar 21, 2016

@author: ugur
'''
emojis=    {'(=^..^=)' : '@gülümseyen kedi[(=^..^=)]', 
             '(=^.^=)'  : '@gülümseyen kedi[(=^.^=)]',
    '(N)'      : '@beğenmedim[(N)]',
    '(Y)'      : '@beğendim[(Y)]',
    '(]:{'     : '@sarıklı hoca[(]:{]',
    '(n)'      : '@beğenmedim[(n)]',
    '(y)'      : '@beğendim[(y)]',
    '<@%'      : '@arı[<@%]',
    '-_-'      : '@ifadesiz yüz[-_-]',
    ':"('      : '@göz yaşları dinmeyen yüz[:"(]',
    ":'("      : "@ağlayan yüz[:'(]",
    ':('       : '@üzgün surat[:(]',
    ':(:)'     : '@üzgün domuz[:(:)]',
    ':(|)'     : '@üzgün maymun[:(|)]',
    ':)'       : '@gülümseyen yüz[:)]',
    ':*'       : '@öpücük veren yüz[:*]',
    ':-('      : '@sırıtan ve içten pazarlıklı yüz[:-(]',
    ':-)'      : '@gülümseyen yüz[:-)]',
    #####################################################
    ':-*' : '@öpücük veren yüz[:-*]',
    ':-/' : '@üzgün gülümseme[:-/]',
    ':-/' : '@üzgün gülümseme[:-/]',
    ':-D' : '@kahkaha atan yüz[:-D]',
    ':-O' : '@şaşıran yüz[:-)]',   
    ':-P' : '@dil çıkaran gülümseme[:-P]',
    ':-S' : '@üzülen yüz[:S]',  
    "':-\'" : '@üzgün gülümseme', 
    ':/' : '@üzgün gülümseme[:/]',
    ':3' : '@aşık kedi[',
    ':D' : '@kahkaha atan yüz[:D]',
    ':O' : '@afallayan gülümseme[:O]',
    ':P' : '@dil çıkaran gülümseme[:P]',
    ':S' : '@üzgün gülümseme[:S]',
    ':X)' : '@gülümseyen kedi[',
    #####################################################
    '":\"' : '@üzgün gülümseme[:\]',
    ':o' : '@afallayan gülümseme[:o]',
    ':p' : '@dil çıkaran gülümseme[:p]',
    ':s' : '@üzgün gülümseme[:s]',
    ':|' : 'ifadesiz yüz[:|]',
    ';)' : 'göz kırpan yüz[;)]',
    ';*' : '@aşkla öpücük veren yüz[;*]',
    ';-)' : '@gülümseyen yüz[;-)]',
    ';-*' : '@aşkla öpücük veren yüz[;-*]',
    ';-P' : '@dil çıkaran gülümseme[;-P]',
    ';-p' : '@dil çıkaran gülümseme[;-p]',
    ';P' : '@dil çıkaran gülümseme[;P]',
    ';_;' : '@ağlayan yüz[;_;]',
    ';p' : '@dil çıkaran gülümseme[;p]',
    '</3' : '@kırık kalp[</3]',
    '<3' : '@kalp[<3]',
    '<\3' : '@kırık kalp[<\3]',
    "='(" : '@ağlayan yüz',
    '=(' :'@mutsuz yüz[=(]'  ,
    #####################################################
    '=)' : '@gülümseyen yüz[=)]',
    '=*' : '@öpücük atan yüz[*=]',
    '=/' : '@üzgün gülümseme[=/]',
    '=D' : '@kahkaha atan yüz[=D]',
    '=O' : '@afallayan gülümseme[=O]',
    '=P' : '@dil çıkaran gülümseme[=]',
    'B)' : '@hava atan gülümseme[B)]',
    'B-)' : '@hava atan gülümseme[B-)]',
    #####################################################
    'D:' : 'hayal kırıklığına uğramış yüz[D:]',
    'O.O' : '@afallayan gülümseme[O.O]',
    'O:)' : '@gülümseyen melek yüz[O:)]',
    'O:-)' : '@gülümseyen melek yüz[O:)]',
    'O=)' : '@gülümseyen melek yüz[O=)]',
    '^_^;;' : '@alnından soğuk terler döken gülümseme[^_^;;]',
    'u_u' : '@morali bozuk gülümseme[u_u]',
    #####################################################
    '}:)' : '@şeytani[}:)]',
    '}:-)' : '@şeytani[}:-)]',
    '}=)' : '@şeytani[}=)]',
    '~@~' : '@insanpisliği[~@~]'}
   
    
text="adebayor :D :O ve aslıhan bize geldiler."
print(text)
for abbrev in emojis :
    text=text.replace(abbrev,emojis[abbrev])

print (text)
   



    








