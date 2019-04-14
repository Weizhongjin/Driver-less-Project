import os
xmlfilepath='./bdd100k/Annotations/val'  
txtsavepath='./bdd100k/ImageSets/Main/'

xmlfile=os.listdir(xmlfilepath)
ftrain=open(txtsavepath+'val.txt','w')
for file in xmlfile:
    if not os.path.isdir(file):
        name = os.path.splitext(file)[0]
        ftrain.write(name+'\n')

ftrain.close()
