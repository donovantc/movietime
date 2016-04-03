#!/usr/bin/python
import pymysql

class DBMan(object):
    '''
    classdocs
    ''' 
    @staticmethod
    def executeSql(sql):
        try:
            conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='mymoviesdb',charset='utf8')
            cur = conn.cursor()
            res = cur.execute(sql)
            cur.close()
            conn.close()
            return res
        except:
            raise
        
    @staticmethod
    def executeSqlFetchAll(sql):
        try:
            conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='mymoviesdb',charset='utf8')
            cur = conn.cursor()
            cur.execute(sql)
            res = cur.fetchall()
            cur.close()
            conn.close()
            return res
        except:
            raise
    
    @staticmethod
    def executeBatchSql(sqlCommands):
        try:
            conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='mymoviesdb',charset='utf8')
            res =  []
            cur = conn.cursor()
            for sql in sqlCommands:
                #cur = conn.cursor()
                res.append(cur.execute(sql))
            
            conn.commit()
            cur.close()
            conn.close()
            return res
        except:
            raise
        