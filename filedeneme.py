'''
Created on Apr 25, 2016

@author: ugur
'''
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
text_file = open(filename, "r")
text_file_readlines=text_file.readlines()

print(filename)
print(text_file_readlines)