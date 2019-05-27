from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
options = Options()
options.add_argument("--headless") # Runs Chrome in headless mode.
# options.add_argument('--no-sandbox') # Bypass OS security model
# options.add_argument('--disable-gpu')  # applicable to windows os only
options.add_argument('start-maximized') #
# options.add_argument('disable-infobars')
# options.add_argument("--disable-extensions")
options.add_argument("user-data-dir=C:\\Users\\Shayan\\AppData\\Local\\Google\\Chrome\\User Data")


#To open the Pinterest Popular page using chromedriver and enter the credentials to login:
def loginner():
    driver = webdriver.Chrome('C:\\Users\\Shayan\\Downloads\\chromedriver', options=options) #, options=options
    # driver.get("https://www.pinterest.com/categories/popular/")
    driver.get("https://www.pinterest.com/")
    # driver.get("https://www.pinterest.com/pin/14707136269842801/")
    # driver.get("https://www.pinterest.com/pin/21181060733983267/") #joy
    # driver.get("https://www.pinterest.com/pin/595530750705036527/") #candle
    # driver.get("https://www.pinterest.com/pin/492299803014651574/") #off grid
    # driver.get("https://www.pinterest.com/pin/21181060732213176/") #hair
    # driver.get("https://www.pinterest.com/bakerbrit19/makeup/") #hair

    # first_login = WebDriverWait(driver, 20).until(EC.presence_of_element_located((
    #     By.XPATH, "//*[@class='Jea XiG gjz mQ8 zI7 iyn Hsu']"))
    # )
    # first_login.click()

    # username = driver.find_element_by_id("email")
    # password = driver.find_element_by_id("password")
    # # username.send_keys("sh.shmss@gmail.com")
    # username.send_keys("sshamsko@students.kennesaw.edu")
    # password.send_keys("Sh22862182")
    # second_login = driver.find_element_by_xpath("//*[@class='red SignupButton active']")
    # second_login.click()
    # time.sleep(2)

    return (driver)
