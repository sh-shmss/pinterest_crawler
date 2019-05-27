# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 22:07:35 2018
Copyright KSU DIR Lab
@author: MH
"""

#!/usr/bin/python

""" 
This script will extract the information from http://pinterest.com/popular/
    and store the popular pins into the database(MongoDB).
"""

import sys
import urllib.request  as urllib2 
import pymongo
from bs4 import BeautifulSoup

from selenium import webdriver

#
# driver = webdriver.Chrome('C:\\Users\\Shayan\\Downloads\\chromedriver')
# driver.get("http://pinterest.com/popular/")
# html = driver.page_source
# soup = BeautifulSoup(html)
# pin = soup.find_all('div', {'class': '_uh _4h _ui'})
# pin.find('a', href=True)


# url = "http://pinterest.com/popular/"
# req = urllib2.Request(url, headers={'User-Agent' : "PyBrowser"})
# con = urllib2.urlopen(req)
# content = con.read()
# soup = BeautifulSoup(content)
# soup.find_all('div', 'item')

class User(object):
    """ This is the Pinterest user class
    """
    def __init__(self):
        self.name = None    # User name
        self.img = None # User image
        self.url = None    # User profile link

class Pin(object):
    """ This class represent the pin
    """
    def __init__(self):
        self.url = None # link of the pin
        self.domain = None   # the domain of the pin
        self.img = None # The img address of the pin
        self.description = None  # the description of the pin
        self.repins = None # The list of users who repinned this pin
        self.likes = None  # The list of users who liked this pin
        self.user = None   # The user who post this pin or repin
        self.cate = None    # The category in which this pin belongs to

class PinSpider(object):
    """ The PinSpider is a class that will read the HTML page, extract the information
        in it and then store the information in the db
    """
    def __init__(self, url):
        """ Args:
            url: The URL we will extract the data from
        """
        try:
            self._content = self._getContent(url)
        except Exception as e:
            print(e)
            print("Couldn't connect to the server! ... will now exit program ...")
            sys.exit()
        self.conn = pymongo.MongoClient('localhost', 27017)   # connect the db for writing pins
        self.db = self.conn.pin_database    # get the database
        self.collection = self.db.pins  # get the collection

    def find(self):
        """ This function will go through the HTML, find each pin.
            And then call _getPinInfo() on each pin
        """
        print('Start searching ...')
        soup = BeautifulSoup(self._content, features="html.parser") # wrap the content with BeautifulSoup
        for pin in soup.find_all('div', 'item'):    # find all pins
            self._getPinInfo(pin)  # for each pin, call storePin to extract info
        print('Cong! DONE!')

    def _getContent(self, url = None):
        if url is None: # Make sure we have an URL to work on
            return
        req = urllib2.Request(url, headers={'User-Agent' : "PyBrowser"})    # Okay, we need to be a browser to not being 403
        try:
            con = urllib2.urlopen(req)  # connect to Pinterest
        except:
            raise 
        content = con.read() # read the HTML content
        con.close() # close the connection
        return content

    def _getPinInfo(self, pinsoup):
        """ Args:
            pin: the pin BeautifulSoup object that we will analyze
        """
        pin = Pin() # init a new Pin object to store the information
        pin.url = pinsoup.find('a', 'pinImageWrapper') 
        pin.url = pin.url.get('href') if pin.url else None  # Get the URL of the pin
        # print pin.url
        pin.domain = pinsoup.find('h4', 'pinDomain')
        pin.domain = pin.domain.string if pin.domain else None # Get the pinDomain
        # print pin.domain
        pin.img = pinsoup.find('img', 'pinImg')
        pin.img = pin.img.get('src') if pin.img else None   # Get the pin img
        # print pin.img
        pin.description = pinsoup.find('p', 'pinDescription')
        pin.description = pin.description.string if pin.description else None  # get the description
        # print pin.description
        pin.repins = self._getRepins(pinsoup.find('a', 'socialItem'))   # Get the list of repinned users
        pin.likes = self._getLikes(pinsoup.find('a', 'likes'))  # Get the list of liked users
        pin.cate = pinsoup.find('a', 'lastAttribution')
        pin.cate = pin.cate.get('href') if pin.cate else None   # get the category link of the pin

        user = User()   # generate a new user to store the owner of current pin
        user.url = pinsoup.find('a', 'firstAttribution')
        user.url = user.url.get('href') if user.url else None   # get the user URL
        user.img = pinsoup.find('img', 'attributionImg')
        user.img = user.img.get('src') if user.img else None    # get the user pic
        user.name = pinsoup.find('span', 'attributionName')
        user.name = user.name.string if user.name else None # get the name of the user

        pin.user = user.__dict__    # we unwrap the user object into dict so we could store it in mongo

        pinDict = pin.__dict__  # make pin into a dict
        print(pinDict)
        # We will store the pin info into mongoDB now
        self.collection.insert(pinDict)
        print('Good! **********')

    def _getRepins(self, repinSoup):
        """ Args:
            repinSoup: the BeautifulSoup object that has the repin URL
        """
        if repinSoup is None:   # in case there's no repins
            return None
        baseURL = 'http://pinterest.com'
        repinURL = baseURL + repinSoup.get('href')  # Get the repin URL
        try:
            content = self._getContent(repinURL) # read the HTML content
        except Exception as e:
            print('A bad repins page request: ', e)
            return None
        result = [] # a tmp list that will store the repin user list
        soup = BeautifulSoup(content) # wrap the content with BeautifulSoup
        for pin in soup.find_all('div', 'item'):    # find all pins
            user = User()
            user.url = pin.find('a', 'boardLinkWrapper')
            user.url = user.url.get('href') if user.url else None   # get the board link
            user.img = pin.find('span', 'thumbImageWrapper').find('img')
            user.img = user.img.get('src') if user.img else None    # get the user img
            user.name = pin.find('span', 'fullname')
            user.name = user.name.string if user.name else None # get the user name
            result.append(user.__dict__)
        return result
        

    def _getLikes(self, likeSoup):
        """ Args:
            likeSoup: the BeautifulSoup object that has the like URL
        """
        if likeSoup is None:   # in case there's no likes
            return None
        baseURL = 'http://pinterest.com'
        likeURL = baseURL + likeSoup.get('href')  # Get the repin URL
        try:
            content = self._getContent(likeURL) # read the HTML content
        except Exception as e:
            print('A bad likes page request: ', e)
            return None
        result = [] # a tmp list that will store the repin user list
        soup = BeautifulSoup(content) # wrap the content with BeautifulSoup
        for pin in soup.find_all('div', 'item'):    # find all pins
            user = User()
            user.url = pin.find('a', 'userWrapper')
            user.url = user.url.get('href') if user.url else None   # get the board link
            user.img = pin.find('img', 'userFocusImage')
            user.img = user.img.get('src') if user.img else None    # get the user img
            user.name = pin.find('h3', 'username')
            user.name = user.name.string if user.name else None # get the user name
            result.append(user.__dict__)
        return result


if __name__ == '__main__':
    try:
        p = PinSpider('http://pinterest.com/popular/')
        p.find()
    except Exception as e:
        print('Something very wrong just happened ...')
        print(e)

