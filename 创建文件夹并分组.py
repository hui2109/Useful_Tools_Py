import shutil,os
rootpath='/Users/hui99563/Desktop/肝包虫新'
def move():
    for i in os.listdir(rootpath):
        if i.startswith('00'):
            os.mkdir(os.path.join(rootpath,i,'超声报告'))
            for j in os.listdir(os.path.join(rootpath,i)):
                if j=='超声报告-1.png' or j=='超声报告-2.png':
                    shutil.move(os.path.join(rootpath,i,j),\
                    os.path.join(rootpath,i,'超声报告',j))
                    print(j)
move()

