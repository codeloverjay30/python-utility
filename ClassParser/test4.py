x = 2
def a_func1():
    def a_func1_1():
        return "a_func1_1"
    return "a_func1"
print(locals())

print("~"*50)

r = locals()['a_func1']

print(r)
print(type(r))
print(dir(r))