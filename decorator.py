"""def hello_decorator(func): 
	def inner1(): 
		print("Hello") 
		func() 
		print("hi") 
	return inner1 
def function_to_be_used(): 
	print("hey") 
function_to_be_used = hello_decorator(function_to_be_used)
function_to_be_used() 

def decorator(func):
    print("hello")
    def inner1(*args,**kwargs):
        print("hi")
        print("hey")
        func()
    return inner1
@decorator_fun
def fun_to():
    print("how r uh")
    fun_to()
#another way
def decorator(func):
    print("hello")
    def inner(*args,**kwargs):
        print("hi")
        print("hey")
        func()
    return inner
def fun_to():
    print("how r uh")
decorator(fun_to)()

def facto(num):
    if num==1:
        return 1
    else:
        return num*facto(num-1)
print(facto(5))


#split
a={"a":"apple","b":"ball","c":"cat"}
print(a)
keys=a.keys()
values=a.values()
print(keys)
print(values)
#zip
a={"a":"apple","b":"ball","c":"cat"}
print(a)
keys,values=zip(*a.items())
print(keys)
print(values)

a={"a":"apple","b":"ball","c":"cat"}
print(a)
keys=[]
values=[]
items=a.items()
for item in items:
    keys.append(item[0]),values.append(item[1])
print(keys)
print(values)

dict={"a":"apple","b":"ball","c":"cat"}
print(dict)

dict={"a":"apple","b":"ball","c":"cat"}
for i in dict:
    print(i)
for j in dict:
    print(dict[j])"""
    








