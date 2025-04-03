import tkinter
def button_clicked():
    print("I was clicked")
    new_text = input.get()
    label.config(text=new_text)

window =tkinter.Tk()
window.title("My Window")
window.minsize(height=300, width=400)

label = tkinter.Label(text="This is my label", font=("Arial", 18, "bold"))
label.config(text="New Text")
label.grid(column=0, row=0)
#label.pack() #using place puts them using x and y values

button = tkinter.Button(text="click me", command=button_clicked)
button.grid(column=1, row=1)

new_button = tkinter.Button(text="click me2")
new_button.grid(column=2, row=0)
#button.pack()


input = tkinter.Entry(width=10)
print(input.get())
input.grid(column=3, row=3)
#input.pack()



# def add(*args):
#     print(type(args))
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
# print(add(1,2,3,4,5,6,7))
# print(add(1,2))
# print(add(3))
#
# def calculate(n, **kwargs):
#     # print(kwargs)
#     # print(type(kwargs))
#     # for key, value in kwargs.items():
#     #     print(key)
#     #     print(value)
#     n+=kwargs["add"]
#     n*=kwargs["multiply"]
#     n-=kwargs["subtract"]
#     return n
#
# print(calculate(7, add=1, multiply=5, subtract=5))
#
# class Car:
#
#     def __init__(self, **kwargs):
#         # we use .get() instead of [""] because it will return none instead. If no Kwargs, no issue
#         self.make = kwargs.get("make")
#         self.model = kwargs.get("model")








window.mainloop()