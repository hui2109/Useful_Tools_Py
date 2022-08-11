from typing import Iterable,Union
class MyRanking:
    def __init__(self,y:Iterable[Union[int,float]]):
        self.compare_list=list(y)
        self.y1=self.compare_list.pop()
        self.judge=False
        self.ranking_list=[]
        self.ranking_list.append(self.y1)
    def compare(self,x1,x2=None):
        if x2 is None:
            return x1
        else:
            if x1<=x2:
                return x1
            else:
                return x2
    def loop(self):
        if len(self.compare_list)>0:
            y2=self.compare_list.pop()
            if self.compare(y2,self.ranking_list[0])==y2:
                self.ranking_list.insert(0,y2)
            elif self.compare(y2,self.ranking_list[-1])!=y2:
                self.ranking_list.append(y2)
            else:
                for i in self.ranking_list[1:-2]:
                    if self.compare(y2,i)==y2:
                        self.ranking_list.insert(self.ranking_list.index(i),y2)
                        self.judge=True
                        break
                if self.judge is False:
                    self.ranking_list.insert(-1,y2)
            return self.loop()
        else:
            return self.ranking_list
if __name__ == '__main__':
    a=MyRanking([2,1,6,1,8,2,2.1])
    print(a.loop())
