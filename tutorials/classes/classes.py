class Point: # Classes define new type like int,string,float,boolean and are name with Pascal naming convention
    # Constructors
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def move(self):
        print('move')

    def draw(self):
        print('draw')


point1 = Point(11,21)
point2 = Point(23,45)
point3 = Point(10,20)

point1.x = 10
point1.y = 20
point2.x = 1

print(point1.y)
print(point2.x)
point1.draw()
print(point3.x)


