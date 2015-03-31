# program to consolidate files in exercism-python exercises after restore
import os, shutil, glob

for org_dir in os.listdir(os.getcwd()):
    #move files
    try:
        os.chdir(os.getcwd()+'/'+org_dir+'/python/'+org_dir)
    except OSError:
        print 'non-existent directory {}'.format(os.getcwd())
        os.chdir('..')
        continue
    if glob.glob('*.py') != []:
        for filename in glob.glob('*.py'):
            shutil.move(filename, os.chdir('../..'))
            
    #remove old directories        
    try:

        os.rmdir(os.getcwd()+'/'+org_dir+'/python/'+org_dir)
        os.chdir("..")
    except OSError:
        print 'Files found in {}'.format(os.getcwd())
        os.chdir("../..")
        continue        
    try:        
        os.rmdir(os.getcwd()+'/'+org_dir+'/python')
        os.chdir("..")
    except OSError:
        print 'Files found in {}'.format(os.getcwd())
        os.chdir("../..")
        continue
    
    
print 'Done'    

    
# need to find out how to manipulate os, system, files & file names
#---using os module to access file system

