'''
In the config module, we’ll define our tiny configuration management framework. 
The idea is:
++ make the app behave according to configuration preset selected by the APP_ENV environment variable, 
++ add an option to override any configuration setting with a specific environment variable if required.
'''


import os
import sys
import config.settings

# create settings object corresponding to specified env
APP_ENV = os.environ.get('APP_ENV', 'Dev')
_current = getattr(sys.modules['config.settings'], '{0}Config'.format(APP_ENV))()

# copy attributes to the module for convenience
for atr in [f for f in dir(_current) if not '__' in f]:
   # environment can override anything
   val = os.environ.get(atr, getattr(_current, atr))
   setattr(sys.modules[__name__], atr, val)


def as_dict():
   res = {}
   for atr in [f for f in dir(config) if not '__' in f]:
       val = getattr(config, atr)
       res[atr] = val
   return res