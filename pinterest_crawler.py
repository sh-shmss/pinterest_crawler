# -*- coding: utf-8 -*-
"""
Created on Wed Dec 31 22:07:35 2018
Copyright KSU DIR Lab
@author: Shayan Shamskolahi sshamsko@students.kennesaw.edu
"""

#!/usr/bin/python
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
import datetime
from login import loginner
from pin_info import getPinsinfo
from user_info import user_info_finder

# To extract the information of the first hundred pins on Pinterest popular
def parser ():
    driver= loginner()
    pause_time = 1.5
    counter= 0
    pin_classes= []

    # To scroll down the page 10 time and scrape the content through BeautifulSoup. Content will be saved to souplist.
    while counter < 20:
        html = driver.page_source
        soup = BeautifulSoup(html, features="html.parser")
        divs= soup.find_all('div', {'class': 'Yl- MIw Hb7'})
        for pin_class in divs:
            # To ensure the pin is not already in the list and is not a promoted post either
            if pin_class not in pin_classes and pin_class.div.div.div.div.a.get("href")[:5] == "/pin/":
                pin_classes.append(pin_class)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        counter= counter+1
        time.sleep(pause_time)
        global no_of_pins
        no_of_pins = len(pin_classes)
    print (no_of_pins, "pins were captured.")
    print("Remaining pins to parse:")
# To open the stored pins url one by one and extract data through getPinsinfo()
    for i in range (len(pin_classes)):
        # if i == 1:
        #     break
        try:
            protopin= pin_classes[i]
            childurl = protopin.div.div.div.div.a.get ("href")
            pinurl= "https://www.pinterest.com"+childurl
            # print ("\r" + str(no_of_pins - i), pinurl, end="", flush=True)
            print (str(no_of_pins - i), pinurl)

            # print (no_of_pins - i, pinurl + "\n")
            # driver.execute_script("window.open('');")
            # driver.switch_to.window(driver.window_handles[1])
            # driver.back()
            # To allow for the full content to load
            # WebDriverWait (driver, 60)
            driver.get(pinurl)
            # time.sleep(0.4)
            # WebDriverWait (driver, 60)
            pin = getPinsinfo(driver)
            user = user_info_finder(driver)
            f.write (
                     # # str(user.checker) + "," +
                     str(pin.pinner_user_name).replace(",", "|") + "," +
                     pin.pinner_gender + "," +
                     str(user.followers) + "," +
                     str(user.following) + "," +
                     str(user.total_pins) + "," +
                     str(user.pins_in_board) + "," +
                     str(user.board_followers) + "," +
                     # str(user.total_boards) + "," +
                     # # str(user.average_repins) + "," +
                     str(pin.repins).replace(",","").replace("k", "000") + "," +
                     str(pin.pin_url) + "," +
                     # str(pin.board_url) + "," +
                     str(pin.img_url) + "," +
                     str(pin.board_name).replace(",", "|") + "\n"
                     )

            # for i in pin.categories:
            #     f.write(i + ",")
            # f.write("\n")

        except UnicodeEncodeError:
            continue
        except NoSuchElementException:
            continue
        except StaleElementReferenceException:
            continue
        except TimeoutException:
            continue
        except ValueError:
            continue

# To generate different file name every time new data is parsed
# tt = time.time()
# current_timestamp = datetime.datetime.fromtimestamp(tt).strftime('%Y-%m-%d %H-%M-%S')
# filename = "pinterest " + current_timestamp + ".csv"
filename = "pinterest.csv"

global f
# f = open(filename, "a", encoding="utf-8")
f = open(filename, "a")

print ("Fetching data... Please be patient!")
parser()
f.close()
print ("\nCrawling successful. Check the CSV file in the current folder.")

# cd C:\Users\shayan\AppData\Local\Programs\Python\Python37-32
# python.exe "C:\Users\shayan\Desktop\Pinterest\pinterest_crawler.py"