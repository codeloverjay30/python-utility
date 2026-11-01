from modulefinder import ModuleFinder

class ModuleLister: 
    @staticmethod
    def GetLoadedModules(
            fileName : str
    ):
        finder = ModuleFinder()
        finder.run_script(fileName)
        
        moduleslist = {}
        print(finder.modules)
        for name, mod in finder.modules.items():
            filename = mod.__file__
            if filename is None:
                continue
            if '__' in name:
                continue
            moduleslist[name.split(".")[0]] = True
        
        result = list()
        for (name, dummy) in moduleslist.items():
            result.append( [name] )
        return result
    @staticmethod 
    def IsLoadedModule(
            fileName : str,
            moduleName : str
    ) -> bool :
        result = ModuleLister.GetLoadedModules(fileName=fileName)
        keys = [ k for (k,v) in result ]
        if moduleName in keys :
            return True
        return False

if __name__ == '__main__' :
    print('Loaded modules:')
    r = ModuleLister.GetLoadedModules("ModuleLister_v2.py")
    print(r)
    print("-"*20)
    r = ModuleLister.IsLoadedModule("ModuleLister_v2.py","modulefinder")
    print(r)
    