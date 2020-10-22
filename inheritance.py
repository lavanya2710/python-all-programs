"""class person(object):
    def __init__(self,name):
        self.name=name
    def getname(self):
        return self.name
    def isemployee(self):
        return False
class employee(person):
    def isemployee(self):
        return True
emp=person("geeks")
print(emp.getname(),emp.isemployee())
emp=employee("geeks1")
print(emp.getname,emp.isemployee())
class base(object):
    pass
class derived(base):
    pass
print(issubclass(base,derived))
print(issubclass(derived,base))
b=base()
d=derived()
print(isinstance(b,derived))
print(isinstance(d,base))

class base(object):
    def __init__(self,x):
        self.x=x
class  derived(base):
    def __init__(self,x,y):
        base.x=x
        self.y=y
    def printxy(self):
        print(base.x,self.y)
d=derived(10,20)
d.printxy()"""

