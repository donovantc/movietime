'''
Created on 05 Jul 2014

@author: donovan.isherwood
'''
from utilities.GoogleKinoReader import GoogleKinoReader
from utilities.DBMan import DBMan
from data_model.Cinema import Cinema
import datetime

try:
    step = 1
    googleKinoReader = GoogleKinoReader()
    
    '''
    Insert Cinemas only
    '''
    if step == 0:
        cinema_info = googleKinoReader.executeInitialCinemaRetrieve()
        cineam = Cinema()
        sql = []
        now = datetime.datetime.today()
        for cinema in cinema_info:
            cinema._LastUpdate = now
            sql_single = cinema.getSqlInsert("cinema") 
            sql.append(sql_single)
            #print(sql_single)
            #print(cinema)
        res = DBMan.executeBatchSql(sql)

    elif step == 1:
        source_id = "60e0c61e9c3d5969"
        place = "Berlin"
        date = datetime.datetime.today()
        movies = googleKinoReader.readCinemaMoviePage(place, source_id, date)
        for movie in movies:
            print(movie)
        
        
    
    #print(res)
    print("Insert complete")
except:
    raise