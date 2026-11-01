from modulefinder import ModuleFinder
from inspect import isclass

finder = ModuleFinder()
finder.run_script('LocalFileFinder_v2.py')

print('Loaded modules:')
for name, mod in finder.modules.items():
    print('%s: ' % name, end='')
    print(','.join(list(mod.globalnames.keys())[:3]))

