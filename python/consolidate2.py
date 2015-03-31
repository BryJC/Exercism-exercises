# THIS WORKED!!!!!! WOOOOOOOOOOOOO (March 30th 2015)

# program to consolidate files in exercism-python exercises after restore
import os, shutil, glob, re

expy = '/home/bryjc/Projects/exercism/python/'

for _dir in os.listdir(expy):
    
    #remove bad files
    for filen in glob.glob(expy + _dir +'/*'):
        tests = re.findall(r'test', filen)
        reads = re.findall(r'README', filen)
        pyfis = re.findall(r'\.py', filen)
        if (tests == []) and (reads == []) and (pyfis != []):
            os.remove(filen)
   
    #move files
    try:
        os.chdir(expy + _dir + '/python/' + _dir +'/')
        if glob.glob('*.py') != []:
            for filen in glob.glob(expy + _dir + '/python/' + _dir + '/' + '*'):
                shutil.move(filen, expy + _dir + '/')
    except OSError:
        print 'non-existent directory {}'.format(
                                          expy + _dir + '/python/' + _dir + '/')
        continue
    
            
    #remove old directories        
    try:
        os.rmdir(expy + _dir + '/python/' + _dir)
    except OSError:
        print 'Files found in {}'.format(expy + _dir + '/python/' + _dir)
        continue        
    try:        
        os.rmdir(expy + _dir + '/python/')
    except OSError:
        print 'Files found in {}'.format(expy + _dir + '/python/' + _dir)
        continue    
    
print 'Done'    

    
# need to find out how to manipulate os, system, files & file names
#---using os module to access file system
