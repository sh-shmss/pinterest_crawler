# from selenium import webdriver
# from bs4 import BeautifulSoup
# import time
# import re
#
# def loginner():
#     global driver
#     driver = webdriver.Chrome('C:\\Users\\Shayan\\Downloads\\chromedriver')
#     driver.get("https://www.pinterest.com/categories/popular/")
#     first_login = driver.find_element_by_xpath("//*[@class='_4f _50 _5a _h _z7 _4q _j']")
#     first_login.click()
#     username = driver.find_element_by_id("email")
#     password = driver.find_element_by_id("password")
#     username.send_keys("sshamsko@students.kennesaw.edu")
#     password.send_keys("22862182")
#     second_login = driver.find_element_by_xpath("//*[@class='red SignupButton active']")
#     second_login.click()
#     time.sleep(1.01)
#     return (driver)
#
# def getPinsinfo():
#     driver= loginner()
#     driver.get("https://www.pinterest.com/pin/AZrZSpozfhu7Hjurjt9sJmfCZRbDEUJsP47xZYmcPUgBRCO0v9bfuLU/")
#     parser = driver.find_element_by_xpath("//*[@aria-label='Saved']/a")
#     print("parser's username: ", parser.get_attribute("href").strip("/").split("/")[-1])
#     username = driver.find_element_by_xpath("//*[@class='userActivity']//*//*/a")
#     print("username link: ", username.get_attribute("href"))
#     print("User's Name: ", username.get_attribute("text"))
#     # Can use [0] to extract the first name to for gender-related analytics purposes
#     folder = driver.find_element_by_xpath("//*[@class='userActivity']//*//*/a[2]")
#     print("folder link: ", folder.get_attribute("href"))
#     print("folder name: ", folder.get_attribute("text"))
#     repins = driver.find_element_by_xpath("//*[@class='_5k _h _z7 _4q']")
#     print("Number of repins: ", repins.text[3:])
#     hashtags = driver.find_element_by_xpath("//*[@class='_4f _h _z7 _4q']/img")
#     hashtag_list = (hashtags.get_attribute("alt").split())
#     for hashtag in hashtag_list:
#         regex = re.compile('[,\.!?#]')
#         if hashtag[0] == "#":
#             print("#: ", regex.sub('', hashtag))
#
# getPinsinfo()

# x=list("hello world")
# print (x[0])

# import pandas as pd
# pinterest = pd.read_pickle('dataset_array')
# print (len(pinterest['image_vector'][49]))