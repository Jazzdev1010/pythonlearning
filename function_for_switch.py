def func1():
    print("Function 1")

def func2():
    print("Function 2")

def func3():
    print("Function 3")

def switch(argument):
    switcher = {
        1: func1,
        2: func2,
        3: func3
    }
    func = switcher.get(argument, lambda: print("Invalid"))
    func()

switch(2)