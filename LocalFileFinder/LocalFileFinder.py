import inspect

class LocalFileFinder:
    @staticmethod
    def GetLocalMembers(
            localModule 
    ):
        return inspect.getmembers(localModule)
    @staticmethod
    def GetLocalFunctions(
            localModule
    ):
        localMembers = LocalFileFinder.GetLocalMembers(localModule = localModule)
        return [ k for (k,v) in localMembers if inspect.isfunction(v)]
    @staticmethod
    def GetClasses(
            localModule
    ):
        localMembers = LocalFileFinder.GetLocalMembers(localModule = localModule)
        return [ k for (k,v) in localMembers if inspect.isclass(v)]
    
    @staticmethod
    def GetLocalClasses(
            localModule
    ):
        localMembers = LocalFileFinder.GetLocalMembers(localModule = localModule)
        lo = [ (k,v) for (k,v) in localMembers if inspect.isclass(v)]
        return [ k for (k,v) in lo if v.__name__ == localModule.__name__ ]
