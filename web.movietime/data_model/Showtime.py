'''
Created on 27 Jul 2014

@author: donovan.isherwood
'''
import abc
import demjson
import json
#from data_model import DBModelBase

class Showtime(object):
    '''
    classdocs
    '''
    def __init__(self, ShowtimeID="-", Date="", Time="", TimeZone=""):
        self._ShowtimeID = ShowtimeID
        self._Date = Date
        self._Time = Time
        self._TimeZone = TimeZone
        
    @property
    def ShowtimeID(self):
        return self._ShowtimeID
    
    @ShowtimeID.setter
    def ShowtimeID(self, value):
        self._ShowtimeID = value
        
    @property
    def Date(self):
        return self._Date
    
    @Date.setter
    def Date(self, value):
        self._Date = value
        
    @property
    def Time(self):
        return self._Time
    
    @Time.setter
    def Time(self, value):
        self._Time = value
        
    @property
    def TimeZone(self):
        return self._TimeZone
    
    @TimeZone.setter
    def TimeZone(self, value):
        self._TimeZone = value
            
    def __str__( self ):
        str = "ShowtimeID: " + self._ShowtimeID + "\n"
        str += "Date: " + self._Date.__str__() + "\n"
        str += "Time: " + self._Time +"\n"
        str += "TimeZone: " + self._TimeZone
        return str
    
    def toJSONString(self):
        data = {}
        data['ShowtimeID'] = self._ShowtimeID
        data['Date'] = self._Date.__str__()
        data['Time'] = self._Time
        data['TimeZone'] = self._TimeZone
        return data
        
    def getSqlInsert(self, TableName):
        template = "INSERT INTO {0} SET Date='{1}', Time='{2}', TimeZone='{3}'"
        return template.format(TableName, self._Date.__str__(), self._Time, self._TimeZone) 