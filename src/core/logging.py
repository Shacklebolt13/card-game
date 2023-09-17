from logging import getLogger,Logger
from typing import Callable,ClassVar

def logger(klass):
    
    @classmethod
    def setLogger(cls, logger):
        cls.__LOGGER = logger 
            
    @property
    def log(self):
        return self.__LOGGER
    
    klass.setLogger = setLogger
    klass.setLogger( getLogger(klass.__module__))
    klass.log = log

    return klass
    