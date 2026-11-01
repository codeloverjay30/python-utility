import inspect
import types
def a_func1():
    def a1_func1():
        return "a1_func1"
    print(inspect.getframeinfo(inspect.currentframe()))
    return "a_func1"
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
                    
class TestClass2:
    def Greeting():
        def NiceToMeetYou():
            print("NiceToMeetYou!!!")
    def Food():
        class Fruit:
            class Banana:
                def Sex():
                    print("Sex!!!")
            class Apple:
                def Phone():
                    print("Phone!!!")
        print("Sound!!!")
    class b:
        def b1_func1():
            print("b1_func1!!!")
        class b1_1:
            def b1_1_func1():
                print("b1_1_func1!!!")
            @staticmethod
            def b1_1_func2():
                print("a1_1_func2!!!")

def GetListOfClassFunctions(foo):
    # foo - a class object
    funcList = [ foo.__dict__.get(a) for a in dir(foo) if isinstance(foo.__dict__.get(a), types.FunctionType)]
    funcFilter = filter(lambda x: x.func_code.co_filename == foo.__module__, funcList)
    return sorted(funcFilter , key=lambda x: x.func_code.co_firstlineno)
if __name__ == '__main__':
    GetListOfClassFunctions(TestClass2)
