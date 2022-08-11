from tkinter import *
class App:
    def __init__(self,master):
        self.master=master
        self.initWidgets()
    def initWidgets(self):
        self.show=Label(relief=SUNKEN,font=('Courier New',24),\
                        width=25,bg='white',anchor=E)
        self.show.pack(side=TOP,pady=10,fill=BOTH,expand=YES)
        p=Frame(self.master)
        p.pack(side=TOP)
        names=('0','1','2','3','4','5','6','7','8','9','+','-','*','/'\
                ,'.','=','(',')','C','Del')
        for i in range(len(names)):
            b=Button(p,text=names[i],font=('Verdana',20),width=2)
            b.grid(row=i//5,column=i%5)
            b.bind('<Button-1>',self.click)
    def click(self,event):
        if (event.widget['text'] in ('0','1','2','3','4','5','6','7','8','9','+','-','*','/'\
                ,'.','(',')')):
            self.show['text']=self.show['text']+event.widget['text']
        elif (event.widget['text'] =='C'):
            self.show['text']=''
        elif (event.widget['text']=='Del'):
            self.show['text']=self.show['text'][:-1]
        elif (event.widget['text']=='='):
            self.expr=self.show['text']
            self.show['text']=str(eval(self.show['text']))
root=Tk()
root.title('计算器')
App(root)
root.mainloop()