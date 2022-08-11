import math
class Point():
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    #point代表的是另一个Point对象
    def distance(self,point):
        return math.sqrt((self.x-point.x)**2+(self.y-point.y)**2)
    #point1代表的是三角形的另一个Point对象，point2代表的是三角形的第三个Point对象
    def triangle(self,point1,point2):
        a=self.distance(point1)
        b=self.distance(point2)
        c=point1.distance(point2)
        if a>b and a>c:
            max_distance=a
            if b>c:
                min_distance=c
                mid_distance=b
            else:
                min_distance=b
                mid_distance=c
        elif a<b and a<c:
            min_distance=a
            if b<c:
                max_distance=c
                mid_distance=b
            else:
                max_distance=b
                mid_distance=c
        else:
            mid_distance=a
            if b>c:
                max_distance=b
                min_distance=c
            else:
                max_distance=c
                min_distance=b
        if min_distance**2+mid_distance**2<round(max_distance**2,4):
            print('这是一个钝角三角形')
        elif min_distance**2+mid_distance**2>max_distance**2:
            print('这是一个锐角三角形')
        else:
            print('这是一个直角三角形')
x=Point(3,6)
y=Point(3,4)
z=Point(5,4)
x.triangle(y,z)
y.triangle(x,z)
z.triangle(x,y)


