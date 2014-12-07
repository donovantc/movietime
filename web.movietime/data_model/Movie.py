'''
Created on 27 Jul 2014

@author: donovan.isherwood
'''
import abc
#from data_model import DBModelBase
from data_model.Showtime import Showtime
import json
from datetime import datetime

class Movie(object):
    '''
    classdocs
    '''
    def __init__(self, MovieID="-", Name="", Showtimes=[]):
        self._MovieID = MovieID
        self._Name = Name
        self._Showtimes = Showtimes
        
    @property
    def MovieID(self):
        return self._MovieID
    
    @MovieID.setter
    def MovieID(self, value):
        self._MovieID = value
        
    @property
    def Name(self):
        return self._Name
    
    @Name.setter
    def Name(self, value):
        self._Name = value
        
    @property
    def Showtimes(self):
        return self._Showtimes
    
    @Showtimes.setter
    def Showtimes(self, value):
        self._Showtimes = value
    
    def __str__( self ):
        str = "MovieID: " + self._MovieID + "\n"
        str += "Name: " + self._Name + "\n"
        str += "Showtimes:\n"
        for time in self._Showtimes:
            str += time.__str__() + "\n"
        return str
    
    def toJSONString(self):
        data = {}
        data['MovieID'] = self._MovieID
        data['Name'] = self._Name
        data['Showtimes'] = [p.toJSONString() for p in self._Showtimes]
        return data
        
    def getSqlInsert(self, TableName):
        template = "INSERT INTO {0} SET Name='{1}'"
        return template.format(TableName, self._Name)