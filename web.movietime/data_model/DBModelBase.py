'''
Created on 27 Jul 2014

@author: donovan.isherwood
'''
import abc

class MyClass(object):
    '''
    classdocs
    '''
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def getSQLInsert(self, TableName):
        return
        