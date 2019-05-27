from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from login import loginner
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup



class User():
    def __init__(self):
        self.followers = None
        self.following = None
        self.total_pins = None
        self.board_followers = None
        self.pins_in_board = None
        self.total_boards = None
        # self.average_repins = None
        # self.checker = None

user= User()
# def scroller (driver, rep):
#     for i in range (rep):
#         driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_DOWN)
#         time.sleep(0.01)

def user_info_finder(driver):
    board = WebDriverWait(driver, 1).until(EC.presence_of_element_located((
        By.XPATH, "//*[@class='Jea b8T zI7 iyn Hsu']//*//*/a[2]"))
    )
    board_url= board.get_attribute("href").replace (",","|")

    pinner_user1 = WebDriverWait(driver, 1).until(EC.presence_of_element_located((
        By.XPATH, "//*[@class='tBJ dyH iFc SMy yTZ pBj DrD IZT swG']/a"))
    )
    pinner_user_url1 = pinner_user1.get_attribute("href")  # url for the user who has pinned this post
    # driver.get (pinner_user_url1)

    url = pinner_user_url1 + "followers/"
    driver.get (url)
    followers_div= WebDriverWait(driver, 1).until(EC.presence_of_element_located((
        By.XPATH, "//*[@class='lH1 dyH iFc SMy ut5 pBj IZT']"))
    )
    followers_div_text = followers_div.text
    user.followers = followers_div_text.replace(",", "").replace("k", "000")

    url = pinner_user_url1 + "following/"
    driver.get (url)
    following_div = WebDriverWait(driver, 1).until(EC.presence_of_element_located((
        By.XPATH, "//*[@class='lH1 dyH iFc SMy ut5 pBj IZT']"))
    )
    following_div_text = following_div.text
    user.following = following_div_text.replace(",", "").replace("k", "000")

    url = pinner_user_url1 + "pins/"
    driver.get (url)
    total_pins_div= WebDriverWait(driver, 1).until(EC.presence_of_element_located((
        By.XPATH, "//*[@class='tBJ dyH iFc SMy MF7 B9u DrD IZT swG']"))
    )
    total_pins_div_text = total_pins_div.text
    user.total_pins = (total_pins_div_text.split()[0]).replace(",", "").replace("k", "000")

    # driver.get (pinner_user_url1+'boards/')
    # SCROLL_PAUSE_TIME = 1
    # last_height = driver.execute_script("return document.body.scrollHeight")
    # while True:
    #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #     time.sleep(SCROLL_PAUSE_TIME)
    #     new_height = driver.execute_script("return document.body.scrollHeight")
    #     if new_height == last_height:
    #         break
    #     last_height = new_height
    #
    # user.total_boards = len (WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
    #     By.XPATH, "//*[@class='Mhr Zr3 sLG zI7 iyn Hsu']")))
    # )
    # # print (user.total_boards)
    #


    driver.get(board_url)
    board_followers_div = WebDriverWait(driver, 1).until(EC.presence_of_element_located((
        By.XPATH, "//*[@class='Jea gjz k1A zI7 iyn Hsu']"))
    )

    board_followers_div = (board_followers_div.text).split()

    user.pins_in_board = (board_followers_div[0]).replace(",", "").replace("k", "000")
    user.board_followers = (board_followers_div[-2]).replace(",", "").replace("k", "000")



    # except TimeoutException:
    #     user.board_followers = "0"
    # # print (user.pins_in_board, user.board_followers)
    #
    # # pin_links=[]
    # # count= round(int(user.pins_in_board)/6)
    # # for i in range (count):
    # #     try:
    # #         # x = (WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
    # #         #     By.XPATH, "//*[@class='Yl- MIw Hb7']/div/div/div/div/div/div/div/div[1]/a")))
    # #         # )
    # #         html = driver.page_source
    # #         soup = BeautifulSoup(html, features="html.parser")
    # #         divs = soup.find_all('div', {'class': 'pinWrapper'})
    # #         for i in divs:
    # #             if i.div.a.get('href') not in pin_links:
    # #                 pin_links.append(i.div.a.get('href'))
    # #         scroller(driver, 25)
    # #     except StaleElementReferenceException:
    # #         continue
    # #     except AttributeError:
    # #         continue
    # # print (len(pin_links))
    # # print (pin_links)
    #
    # # pin_links=[]
    # # count= round(int(user.pins_in_board)/5)
    # # for i in range (count):
    # #     try:
    # #         # x = driver.execute_script("return document.body.clientHeight") + 1000
    # #         html = driver.page_source
    # #         soup = BeautifulSoup(html, features="html.parser")
    # #         divs = soup.find_all('div', {'class': 'pinWrapper'})
    # #         for i in divs:
    # #             if i.div.a.get('href') not in pin_links:
    # #                 pin_links.append(i.div.a.get('href'))
    # #         # driver.execute_script("var x = arguments[0]; window.scrollTo(document.body.scrollHeight,0)", x)
    # #         driver.execute_script("window.scrollBy(0,800)")
    # #         time.sleep(0.5)
    # #
    # #     except StaleElementReferenceException:
    # #         continue
    # #     except AttributeError:
    # #         continue
    # # print (len(pin_links))
    #
    # # total_repins=0
    # # for i in range (len(pin_links)):
    # #     try:
    # #         url= pin_links[i]
    # #         pinurl= "https://www.pinterest.com"+url
    # #         driver.get(pinurl)
    # #         repin_info = driver.find_element_by_xpath("//*[@class='Eqh zI7 iyn Hsu']")
    # #         raw_repins = repin_info.text[3:]  # number of repins
    # #         repins= int (raw_repins.replace(",", "").replace("k", "000"))
    # #         total_repins= total_repins+repins
    # #         print ("\r", i, "out of", len(pin_links), "pins in the current board are parsed.", end="", flush=True)
    # #         user.average_repins= round (total_repins/len(pin_links))
    # #     except UnicodeEncodeError:
    # #         continue
    # #     except NoSuchElementException:
    # #         continue
    # #     except StaleElementReferenceException:
    # #         continue
    # #     except TimeoutException:
    # #         continue
    # #     except ValueError:
    # #         continue
    # # if int (user.pins_in_board) == len(pin_links):
    # #     user.checker = "true"
    # # else:
    # #     user.checker = "false"
    return user

# user_info_finder(loginner())
