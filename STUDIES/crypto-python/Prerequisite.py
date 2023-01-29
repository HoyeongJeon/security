# Math
# - addition
# - muliplication
# - prime number (2, 3, 5, 7, ...)

# What we will learn
# - XOR
# - Modular calculataion

# Python
# - Integer operations (addition, muliplication, division, XOR, modular)
a = 3
b = 7
sum = a + b;
print(sum)
print(a + b)
print(a // b)
# - Functions
def add(a, b):
    return a + b

print(add(3 , 7))
print(add(5 , 7))

# - for and while loops
for i in range(5):
    print(i)

cnt = 5
while True:
    cnt -= 1
    print("cnt is", cnt)
    if cnt < 0:
        break

# - dictionaries
d = {}
d['a'] = 'b'
print("Dictionary d['a'] = ",d['a'])
d['b'] = 'c'
print("Dictionary d['b'] = ",d['b'])
# - lists
my_list = ['ddd'] * 5
my_list.append(5)
print(my_list)
# - class / objects
class MyClass:
    def __init__(self,name="MyName"):
        self.name = name

    def get_name(self):
        return self.name
m = MyClass()
print("m name is ",m.get_name())
m2 = MyClass("Hoyeong")
print("m2 name is ", m2.get_name())
