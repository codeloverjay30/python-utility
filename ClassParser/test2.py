import inspect 
class BaseClass:
    def baseFunc1():
        print("baseFunc1!!!")
class TestClass(BaseClass):
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

if __name__ == '__main__':
    # r =  inspect.getclasstree(classes = TestClass,unique=True)
    r =  inspect.getclasstree(classes = globals()['TestClass'],unique=True)
    print("result:")
    print(r)