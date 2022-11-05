class Rectangle:
    def __init__(self, length, breadth, unit_cost=0):
        self.length = length
        self.breadth = breadth
        self.unit_cost = unit_cost

    def get_perimeter(self):
        return 2 * (self.length + self.breadth)

    def get_area(self):
        return self.length * self.breadth

    def calculate_cost(self):
        area = self.get_area()
        return area * self.unit_cost


# breadth = 120 cm, length = 160 cm, 1 cm^2 = Rs 2000
r = Rectangle(160, 120, 2000)
print(f"Area of Rectangle: {r.get_area()} cm^2")
print(f"Cost of rectangular field: Rs. {r.calculate_cost()} ")


# Python Program illustrate how
# to overload an binary + operator

class A:
    def __init__(self, a):
        self.a = a

    # adding two objects
    def __add__(self, other):
        return self.a + other.a


ob1 = A(1)
ob2 = A(2)
ob3 = A("Geeks")
ob4 = A("For")

print(ob1 + ob2)
print(ob3 + ob4)
# =====================================================================
#Any and All
list1 = []
list2 = []

# Index ranges from 1 to 10 to multiply
for i in range(1, 11):
    list1.append(4*i)

# Index to access the list2 is from 0 to 9
for i in range(0, 10):
    list2.append(list1[i] % 5 == 0)

print('See whether at least one number is divisible by 5 in list 1=>')
print(any(list2))
