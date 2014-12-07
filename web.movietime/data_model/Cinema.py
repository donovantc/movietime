'''
Created on 27 Jul 2014

@author: donovan.isherwood
'''
import abc
from utilities.DBMan import DBMan

class Cinema(object):
    '''
    classdocs
    '''
    _tableName = ''
    
    def __init__(self, CinemaID="-", Name="", Address="", GeoLat="NULL", GeoLong="NULL", Telephone="", LastUpdate="", SourceID=""):
        self._CinemaID = CinemaID
        self._Name = Name
        self._Address = Address
        self._GeoLat = GeoLat
        self._GeoLong = GeoLong
        self._Telephone = Telephone
        self._LastUpdate = LastUpdate
        self._SourceID = SourceID
        
    @property
    def CinemaID(self):
        return self._CinemaID
    
    @CinemaID.setter
    def CinemaID(self, value):
        self._CinemaID = value
        
    @property
    def Name(self):
        return self._Name
    
    @Name.setter
    def Name(self, value):
        self._Name = value
        
    @property
    def Address(self):
        return self._Address
    
    @Address.setter
    def Address(self,value):
        self._Address = value
        
    @property
    def GeoLat(self):
        return self._GeoLat
    
    @GeoLat.setter
    def GeoLat(self, value):
        self._GeoLat = value
        
    @property
    def GeoLong(self):
        return self._GeoLong
    
    @GeoLong.setter
    def GeoLong(self, value):
        self._GeoLong = value
        
    @property
    def Telephone(self):
        return self._Telephone
    
    @Telephone.setter
    def Telephone(self, value):
        self._Telephone = value
        
    @property
    def LastUpdate(self):
        return self._LastUpdate
    
    @LastUpdate.setter
    def LastUpdate(self, value):
        self._LastUpdate = value
        
    @property
    def SourceID(self):
        return self._SourceID
    
    @SourceID.setter
    def SourceID(self, value):
        self._SourceID = value
        
    def __str__( self ):
        str = "CinemaID: " + self._CinemaID + "\n"
        str += "Name: " + self._Name + "\n"
        str += "Address: " + self._Address + "\n"
        str += "Telephone: " + self._Telephone + "\n"
        str += "GeoLat: " + self._GeoLat + "\n"
        str += "GeoLong: " + self._GeoLong + "\n"
        str += "LastUpdate: " + self._LastUpdate.__str__() + "\n"
        str += "SourceID: " + self._SourceID
        return str
    
    def toDictionary(self):
        data = {}
        data['CinemaID'] = self._CinemaID
        data['Name'] = self._Name
        data['Address'] = self._Address
        data['Telephone'] = self._Telephone
        data['GeoLat'] = self._GeoLat.__str__()
        data['GeoLong'] = self._GeoLong.__str__()
        data['LastUpdate'] = self._LastUpdate.__str__()
        data['SourceID'] = self._SourceID
        return data
        
    def getSqlInsert(self, TableName = "cinema"):
        template = "INSERT INTO {0} SET Name='{1}', Address='{2}', GeoLat='{3}', GeoLong='{4}', Telephone='{5}', LastUpdate='{6}', SourceID='{7}'"
        return template.format(TableName, self._Name, self._Address, self._GeoLat, self._GeoLong, self._Telephone, self._LastUpdate, self._SourceID)
    
    def getSqlUpdate(self, TableName = "cinema"):
        template = "UPDATE {0} SET Name='{1}', Address='{2}', GeoLat='{3}', GeoLong='{4}', Telephone='{5}', LastUpdate='{6}' WHERE SourceID='{7}'"
        return template.format(TableName, self._Name, self._Address, self._GeoLat, self._GeoLong, self._Telephone, self._LastUpdate, self._SourceID)
        
    @staticmethod
    def getAllCinemas(place):
        template = 'SELECT * FROM cinema'
        db_man = DBMan()
        res = db_man.executeSqlFetchAll(template)
        cinemas = []
        for row in res:
            cinema = Cinema()
            cinema._CinemaID = row[0]
            cinema._Name = row[1]
            cinema._Address = row[2]
            cinema._GeoLat = float(row[3])
            cinema._GeoLong = float(row[4])
            cinema._Telephone = row[5]
            cinema._LastUpdate = row[6]
            cinema._SourceID = row[7]
            cinemas.append(cinema)
        return cinemas
        