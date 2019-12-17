#Вариант 4

class Circle:
    def __init__(self, rad, x, y):
        self.rad = rad
        self.x = x
        self.y = y

    def __str__(self):
        return "Круг имеет радиус: %d \n x: %d \n y: %d " %(self.rad, self.x, self.y)

    def __add__(self, other):
        self.rad += other.rad
        self.x += other.x
        self.y += other.y
        return Circle(self.rad, self.x, self.y)

    def __rmul__(self, other): 
        return Circle(self.rad * other, self.x * other, self.y * other)

A = Circle(2, 2, 2)
B = Circle(3, 3, 3)

print(A) 
print(B) 
print(A + B) 
print(2*B)
 
        
        













