import sys
class ModuleFinder():
    @staticmethod
    def GetClasses(
        moduleName : str
    ):
        return sys.modules[moduleName]

