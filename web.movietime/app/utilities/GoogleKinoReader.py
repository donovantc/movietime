'''
Created on 15 Jun 2014

@author: donovan.isherwood
'''
import urllib.request
from bs4 import BeautifulSoup
import sys,io
from data_model.Cinema import Cinema
from data_model.Movie import Movie
from data_model.Showtime import Showtime
import datetime
import time

class GoogleKinoReader(object):
    '''
    classdocs
    '''
    _cinema_url = "http://www.google.de/movies?near={0}&start={1}"
    _movies_url = "http://www.google.de/movies?near={0}&tid={1}&date={2}"
    
    def __init__(self):
        return
    
    @classmethod
    def readCinemaMoviePage(self, place, source_id, date):
        dateNum = self.getDateNum(date)
        url = self._movies_url.format(place,source_id,dateNum)
        print(url)
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer,'cp437','backslashreplace')
        movies = self.parseHtmlForCinemaMovies(self.readUrl(url), date)
        print(len(movies).__str__() + " movies found.")
        return movies 
    '''
    Read all cinema info
    '''
    @classmethod
    def readAllPages(self, place = "Berlin"):
        start = 0 #start record
        start_inc = 10 #increment
        start_max = 60 #when to stop
        
        res = []
        while start <= start_max:
            cinemas = self.parseHtmlForCinemaInfo(self.readUrl(self._cinema_url.format(place,start)))
            for c in cinemas:
                res.append(c)
            start += start_inc
            
        return res 
    
    '''
    Open the URL
    '''
    @classmethod
    def readUrl(self, url):
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        soup = BeautifulSoup(response.read())            
        return soup
    
    @classmethod
    def parseFullHtml(self,soup):
        cinemas = soup.find_all("div", class_="theater")
        #print(cinemas)
        cinemaList = []
        for tag in cinemas:
            cinema = Cinema()
            '''Get the name of the cinema'''
            desc = tag.find("div", class_="desc")
            name = desc.h2.a.string
            source_id = desc.h2.a['href']
            #print("- " + name)
            cinema._Name = name
            index = source_id.find("tid=", 0)
            cinema._SourceID = source_id[index+4:]
            
            '''Get the address of the cinema'''
            info = desc.find("div", class_="info")
            full_address = info.contents[0]
            #print(full_address)
            seperator = full_address.find(" - ")
            if (seperator != -1):
                cinema._Address = full_address[:seperator]
                cinema._Telephone = full_address[seperator+3:]
            
            '''Get the movies for a cinema'''
            movies = tag.find_all("div", class_="movie")
            for movie in movies:
                '''Get the name'''
                name = movie.find("div", class_="name").a.string
                #print(name)
                '''Get the show times'''
                showtimes = movie.find("div", class_="times")
                #showtimes.find_all()
                for showtime in showtimes.children:
                    time = (showtime.contents[2])[:5]
                    #print(time)
            
            cinemaList.append(cinema)
        return cinemaList
    
    @classmethod
    def parseHtmlForCinemaInfo(self,soup):
        datetimenow = datetime.datetime.now()
        cinemas = soup.find_all("div", class_="theater")
        #print(cinemas)
        cinemaList = []
        for tag in cinemas:
            cinema = Cinema()
            '''Get the name of the cinema'''
            desc = tag.find("div", class_="desc")
            name = desc.h2.a.string
            source_id = desc.h2.a['href']
            #print("- " + name)
            cinema._Name = name
            index = source_id.find("tid=", 0)
            cinema._SourceID = source_id[index+4:]
            
            '''Get the address of the cinema'''
            info = desc.find("div", class_="info")
            full_address = info.contents[0]
            #print(full_address)
            seperator = full_address.find(" - ")
            if (seperator != -1):
                cinema._Address = full_address[:seperator]
                cinema._Telephone = full_address[seperator+3:]
            
            cinema._LastUpdate = datetimenow
            cinemaList.append(cinema)
        return cinemaList
    
    @classmethod
    def parseHtmlForCinemaMovies(self,soup,date):
        moviesList = []
        movies = soup.find_all("div", class_="movie")
        for tag in movies:
            movie = Movie()
            '''Get the name of the movie'''
            desc = tag.find("div", class_="name")
            name = desc.a.string
            movie._Name = name
            '''Get the show times'''
            showtimes = tag.find("div", class_="times")
            #showtimes.find_all()
            showtimeList = []
            for showtime in showtimes.children:
                showtimeObj = Showtime()
                time = (showtime.contents[2])[:5]
                showtimeObj._Time = time
                showtimeObj._Date = date
                showtimeList.append(showtimeObj)
            
            movie.Showtimes = showtimeList
            moviesList.append(movie)
        return moviesList
        
    @classmethod
    def executeInitialCinemaRetrieve(self, place):
        return self.readAllPages(place)
    
    @classmethod
    def executeUpdateCinemas(self, place):
        #sys.stdout = io.TextIOWrapper(sys.stdout.buffer,'cp437','backslashreplace')
        cinemas = self.readAllPages(place)
        return cinemas
    
    @classmethod
    def executeUpdateMovies(self):
        return
    
    @classmethod
    def executeUpdateShowtimes(self):
        return
    
    @classmethod
    def getDateNum(self, filterDate):
        now = datetime.datetime.now()
        if filterDate == now:
            return 0
        
        delta = filterDate - now
        return delta.days