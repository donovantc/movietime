'''
Created on 05 Jul 2014

@author: donovan.isherwood
'''
from bottle import Bottle, route, run, response # @UnresolvedImport
from utilities.GoogleKinoReader import GoogleKinoReader
import time
import datetime
from utilities.DBMan import DBMan
import utilities.custom_serialiser
import json
from data_model.Cinema import Cinema

#app = Bottle()

@route('/hello')
def hello():
    return "Hello World!"

@route('/cinemas/update/<place>')
def updateCinemas(place):
    googleKinoReader = GoogleKinoReader()
    cinemas = googleKinoReader.executeUpdateCinemas(place)
    
    sqlCommands = []
    for cs in cinemas:
        sqlCommands.append(cs.getSqlUpdate())
    
    res = DBMan.executeBatchSql(sqlCommands)
    sqlInsertCom = []
    for indx, r in enumerate(res):
        if r == 0:
            print(sqlCommands[indx])
            sqlInsertCom.append(cinemas[indx].getSqlInsert())
            
    res = DBMan.executeBatchSql(sqlInsertCom)
            
    _json = json.dumps([c.toDictionary() for c in cinemas], ensure_ascii=False)
    return _json

@route('/cinemas/<place>')
def getCinemas(place):
    response['content_type'] = 'application/json;charset=utf-8'
    cinemas = Cinema.getAllCinemas(place)
    _json = json.dumps([c.toDictionary() for c in cinemas], ensure_ascii=False)
    return _json

@route('/cinema/movietimes/<place>/<source_id>/<date>')
def getMovieTimes(place,source_id,date):
    filterDate = datetime.datetime.strptime(date, '%Y-%m-%d')
    googleKinoReader = GoogleKinoReader()
    movies = googleKinoReader.readCinemaMoviePage(place, source_id, filterDate)
    _json = json.dumps([m.toJSONString() for m in movies],ensure_ascii=False)
    #_json = json.dumps(movies[0], default=utilities.custom_serialiser.default)
    return _json

run(host='localhost', port=3333)
