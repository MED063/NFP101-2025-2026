class Point:
    def __init__(self,x):
        self.__x=x

    @classmethod
    def get_x(cls):
        return Point.__x
    
a=Point(3)
print("a : abscisse", a,get_x())