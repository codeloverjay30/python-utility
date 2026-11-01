import inspect

def named_func():
    class TestClass:
        def Hello():
            def HelloWorld():
                print("HelloWorld!!!")
            print("Hello!!!")
        def Sound():
            class Animal:
                class Dog:
                    def Bark():
                        print("Bark!!!")
                class Cat:
                    def Mow():
                        print("Mow!!!")
            print("Sound!!!")
        class a:
            def a1_func1():
                print("a1_func1!!!")
            class a1_1:
                def a1_1_func1():
                    print("a1_1_func1!!!")
                @staticmethod
                def a1_1_func2():
                    print("a1_1_func2!!!")
    
    for i in range(0, len(inspect.stack()),1):
        func_name = inspect.stack()[0].function
        func_obj = inspect.stack()[1].frame.f_locals[func_name]
        print("i:",i,func_name, func_obj, func_obj.xxx)
        print("-"*20)
        func_obj()

named_func.xxx = 15
named_func()