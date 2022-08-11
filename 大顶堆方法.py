from heapq import *
def maxheap(list):
    max_list=[]
    for i in list:
        max_list.append(-i)
    heapify(max_list)
    max_list_new=[]
    for i in max_list:
        max_list_new.append(-i)
    return max_list_new
#下面部分是测试代码
def test_maxheap():
    a=list(range(10))
    a.extend([8.1,7.2])
    print(maxheap(a))
if __name__=='__main__':
    test_maxheap()


