import tkinter

#
# window =tkinter.Tk()
# window.title("My Window")
# window.minsize(height=300, width=400)
#
# label = tkinter.Label(text="This is my label", font=("Arial", 18, "bold"))
# label.pack(side="left")


def add(*args):
    print(type(args))
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(1,2,3,4,5,6,7))
print(add(1,2))
print(add(3))

def calculate(n, **kwargs):
    # print(kwargs)
    # print(type(kwargs))
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n+=kwargs["add"]
    n*=kwargs["multiply"]
    n-=kwargs["subtract"]
    return n

print(calculate(7, add=1, multiply=5, subtract=5))

class Car:

    def __init__(self, **kwargs):
        # we use .get() instead of [""] because it will return none instead. If no Kwargs, no issue
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")








# window.mainloop()