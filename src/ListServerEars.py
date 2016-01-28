#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "58128"
__date__ = "$08-Jan-2016 08:35:35$"

#import glob
#import os
#os.chdir("c:/IBM8.5/WebSphere/AppServer/profiles/AppSrv01")
#for file in glob.glob("NBP_Ear*"):
#    print(file)

print("searching server directory for enterprise apps")
import os
#for root, dirs, files in os.walk("c:\\IBM8.5\\WebSphere\\AppServer\\profiles\\AppSrv01"):
#    for file in files:
#        if file.endswith(".ear"):        
#             print(os.path.join(root, file))

rootDir = "c:\\IBM8.5\\WebSphere\\AppServer\\profiles\\AppSrv01"
for dirName, subdirList, fileList in os.walk(rootDir):
    if dirName.endswith(".ear"):
        print('Dir: %s' % dirName)
        for fname in fileList:
            if fname.contains(".txt."):
                print('File: \t%s' % fname)
                #os.remove(fname)