#!/usr/bin/env python2
#encoding: windows-1252

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "58128"
__date__ = "$28-Jan-2016 11:49$"

#def check_file_name(self, filename):
#    words = ['.txt.'] #I am not sure if adj and adv are variables
#    for i in words:
#        if i in filename:
#            self.word_type = str(i) #just make sure its string
#        else:
#            self.word_type = ''
#    return self.word_type

print("searching server directory for enterprise apps")
import os

i=0
rootDir = "d:\\TEMP\\NBP_Logs\\NewBankingPlatform"
for dirName, subdirList, fileList in os.walk(rootDir):
    print('Dir: %s' % dirName)
    
    for fname in fileList:
        if ".txt." in fname:
            if not fname.endswith(".ascii"):
                filepath = '%s\\%s' % (dirName, fname)
                i = i+1                
                os.remove(filepath)
            
print("%s files have been removed" % i)