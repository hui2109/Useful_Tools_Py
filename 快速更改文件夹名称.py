import os
path='/Users/hui99563/Desktop/肝包虫新'
for i in os.listdir(path):#i代表登记号
    if i.startswith('00'):
        count=1
        for j in os.listdir(os.path.join(path,i)):#j代表exam开头的文件
            if j.startswith('exam'):
                newname='-'.join([i,str(count)])+'.jpg'
                os.rename(os.path.join(path,i,j),os.path.join(path,i,newname))
                count+=1

