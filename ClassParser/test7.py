from ClassParser import ClassFuncParser

class TestClass:
    class Class1:
        def Func1():
            return "Func1"
        
if __name__ == '__main__':
    inst = TestClass()
    attr1 = getattr(inst, 'Class1.Func1')
    r = attr1()
    print(r)
    