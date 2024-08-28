class Rectangle:
    def __init__(self,length:float,width:float):
        self.leng=length
        self.wid=width
    def calculate_area(self):
        area=self.leng*self.wid
        print("area of the rectangle is",area)

    def calculate_perimeter(self):
        perimeter=2*self.wid*self.leng
        print("perimeter of the rectangle is",perimeter)


x=Rectangle(7.0,8.0)
x.calculate_area()
x.calculate_perimeter()
