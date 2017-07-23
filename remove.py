import os
os.chdir('E:\\QMDownload\\offlinevideo')
dir = 'E:\\QMDownload\\offlinevideo'
size = 0 
for root, dirs, files in os.walk(dir):  
    size += sum([os.path.getsize(os.path.join(root, name)) for name in files])  

import shutil
size = 0 
for root, dirs, files in os.walk(dir):  
    size = sum([os.path.getsize(os.path.join(root, name)) for name in files]) 
    print(root)
    if size<1*1024**2 and root is not dir:
        shutil.rmtree(os.path.join(root))
