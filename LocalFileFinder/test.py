import types
# from LocalFileFinder import LocalFileFinder
import sys
import inspect
import importlib
from os import listdir, getcwd
from os.path import isfile, join

def TestFunc1():
    pass

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

def GetClasses(
        onlyfiles
    ):
    result = list()
    for x in onlyfiles:
        module = importlib.import_module(x)
        for ( name, obj ) in inspect.getmembers(module):
            if inspect.isclass(obj):
                result.append(obj)
    return result
   
"""         
mo = sys.modules[__name__]
r = LocalFileFinder.GetLocalFunctions(mo)
print(r)
r = LocalFileFinder.GetLocalClasses(mo)
print(r)
r  = [x for x in dir(TestClass) if inspect.isclass(getattr(TestClass, x))]
print(r)
"""

mypath = getcwd()
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
r = GetClasses(onlyfiles)
print(r)

