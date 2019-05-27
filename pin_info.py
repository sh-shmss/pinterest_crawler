from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import time
# import re
import datetime
from topic_finder import findxMostFreqWord
from topic_finder import gender_finder
from login import loginner

# To extract data about each individual pin from on what is stored by parser ()
class Pin():

    def __init__(self):
        self.repins = None
        self.board_url = None
        self.pinner_user_name = None
        self.pinner_gender = None
        self.img_url = None
        self.board_name = None
        self.pin_url = None
        self.categories= []

def getPinsinfo(driver):
    pin= Pin()
    # driver.page_source
    pin.pin_url= driver.current_url
    # try:
    # parser = driver.find_element_by_xpath("//*[@aria-label='Saved']/a")
    # parser_name= parser.get_attribute("href").strip("/").split("/")[-1]
    # print("parser's username: ", parser_name)
    # pinner_user = driver.find_element_by_xpath("//*[@class='userActivity']//*//*/a")
    pinner_user= WebDriverWait(driver, 1).until(EC.presence_of_element_located((
        By.XPATH, "//*[@class='tBJ dyH iFc SMy yTZ pBj DrD IZT swG']/a"))
    )
    # pinner_user_url= pinner_user.get_attribute("href") # url for the user who has pinned this post
    # print ("Pinner's URL: ", pinner_user_url)
    pin.pinner_user_name= pinner_user.get_attribute("text").replace(",", "|") # the user who has pinned this post
    # print ("Pinner's Name: ", pinner_user_name)
    # Can use [0] to extract the first name to for gender-related analytics purposes
    # folder = driver.find_element_by_xpath("//*[@class='userActivity']//*//*/a[2]") # the folder where the repined post is saved
    # folder = driver.find_element_by_xpath("//*[@class='tBJ dyH iFc SMy yTZ pBj DrD IZT swG']//*/a") # the folder where the repined post is saved


    board =WebDriverWait(driver, 1).until(EC.presence_of_element_located((
        By.XPATH, "//*[@class='Jea b8T zI7 iyn Hsu']//*//*/a[2]"))
    )

    pin.board_url= board.get_attribute("href").replace (",","|")
    # print("board url: ", board_url)

    pin.board_name= board.get_attribute("text")
    # print("board name: ", board_name)

    repin_info = driver.find_element_by_xpath("//*[@class='Eqh zI7 iyn Hsu']")
    # pin.repins= repin_info.text[3:] # number of repins
    pin.repins= repin_info.text

    # print (repins)

    img_info =WebDriverWait(driver, 1).until(EC.presence_of_element_located((
        By.XPATH, "//*[@class='XiG Zr3 hUC zI7 iyn Hsu']//*//*//*//*//*//*//*/img"))
    )
    pin.img_url = (img_info.get_attribute("src"))

    pin.pinner_gender= gender_finder(str(pin.pinner_user_name.split()[0]))

    # except NoSuchElementException:
    #     pinner_user_name=""
    #     board_url=""
    #     board_name=""
    #     repins =""
    #     img_url=""
    #     pinner_gender=""

    # try: # some pins has no title, so we define an exception mechanism
    #     title = driver.find_element_by_xpath("//*[@class='lH1 dyH iFc SMy kON pBj IZT']/div")
    #     pin_title = title.text.replace(",", "|")
    # except NoSuchElementException:
    #     pin_title=""
    # # print (pin_title)

    # try: # some pins have no original user information. Maybe they are original pins. To handle that:
        # username_info = driver.find_element_by_xpath("//*[@class='Jea Shl jzS ujU zI7 iyn Hsu']/a")
        # username_url= username_info.get_attribute("href") #the original user who has posted the pin
        # print (username_url)
        # username_info2 = driver.find_element_by_xpath("//*[@class='tBJ dyH iFc SMy yTZ pBj DrD IZT mWe z-6']")
        # username= username_info2.text.replace(",", "|")
        # print (username)
        # username_info3= driver.find_element_by_xpath("//*[@class='tBJ dyH iFc SMy yTZ pBj DrD IZT swG z-6']")
        # username_followers= username_info3.text.replace(",", "|")[:-9]
        # print (username_followers)
    # except NoSuchElementException:
    #     username_url=""
    #     username=""
    #     username_followers=""

    # We won't use hashtags at this point
    # hashtags = driver.find_element_by_xpath("//*[@class='XiG zI7 iyn Hsu']/img")
    # initial_hashtag_list = (hashtags.get_attribute("alt").split())
    # hashtag_list=[]
    #
    # for hashtag in initial_hashtag_list:
    #     if hashtag[0] == "#":
    #         hashtag_list.append(hashtag)

    # content= board_name + " : " + pin_title
    # possible_topics= findxMostFreqWord(pin.board_name,5)
    # print (content)

    # f.write ((repins.replace(",","")).replace("k", "000") + "," +
    #          # pin_title.replace(",", "|") + "," +
    #          # username.replace(",", "|") + "," +
    #          # username_url.replace(",", "|") +"," +
    #          # username_followers.replace(",", "|") + "," +
    #          board_url.replace(",", "|") + "," +
    #          pinner_user_name.replace(",", "|") + "," +
    #          pinner_gender.replace(",", "|") + "," +
    #          # pinner_user_url.replace(",", "|") + "," +
    #          pin_url.replace(",", "|") + "," +
    #          img_url.replace(",", "|") + "," +
    #          board_name.replace(",", "|") + ","
    #          )

    # if len (hashtag_list)> 0:
    #     for ht in hashtag_list:
    #         f.write ("," + ht)
    #     f.write("\n")
    # else:
    #     f.write ("\n")

    # counter=0
    # while counter < 5:
    #     try:
    #         pin.categories.append(possible_topics[counter])
    #         counter= counter+1
    #     except:
    #         pin.categories.append("")
    #         counter= counter+1

    # if len (possible_topics)> 0:
    #     for wrd in possible_topics:
    #         f.write ("," + wrd)
    #     f.write(",")
    # else:
    #     f.write (",")
    # time.sleep(2)
    return (pin)
