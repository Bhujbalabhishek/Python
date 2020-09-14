#Create Custom decorator to get function execution time (add differnt sleep values in differnt functions)


import time

def func_execution_time(func):

    def inner(*args, **kwargs):
        start = time.time()

        func(*args, **kwargs)

        end = time.time()

        print("time taken by ", func.__name__, end-start)
    return inner

@func_execution_time
def sum(a,b):
    c=a+b
    print(c)
    time.sleep(3)

sum(34,56)

@func_execution_time
def div(x,y):
    z =x/y
    print(z)
    time.sleep(2)

div(20,4)