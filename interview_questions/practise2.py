
# def outer(text):
#     print("Printing in outer",text)
#     def inner():
#         print(text)
#     return inner

# call = outer("profun")
# print("I'm here")
# call()

def div(a, b):
    print(a / b)

def smart_div(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)
    return inner

div = smart_div(div)
div(2, 4)