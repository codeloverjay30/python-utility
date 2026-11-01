from ModuleFinder import ModuleFinder
import inspect
import sys
def TestFunc1():
    return 'TestFunc1!!!'

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
                
if __name__ == '__main__':
   mainModule = ModuleFinder.GetClasses(moduleName = __name__ )
   print("!!!-------------------!!!")
   classes = dir(mainModule)
   print(classes)
   print("-------------------")
   classes = [ x for x in classes if inspect.isclass(x) == True] 
   print(classes)
   print("!!!-------------------!!!")
   classes = globals()
   print(classes)
   print("-------------------")
   classes = [ k for (k,v) in classes.items() if ( inspect.isclass(v) == True )]
   print(classes)
   print("!!!-------------------!!!")
   classes = inspect.getmembers(__name__)
   print(classes)
   classes = [ k for (k,v) in classes if ( inspect.isclass(v) == True )]
   print("-------------------")
   print(classes)
   print("!!!-------------------!!!")
