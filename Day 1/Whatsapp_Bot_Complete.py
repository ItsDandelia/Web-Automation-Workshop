from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException as nse

def Search_chat(User):
    Search_bar = driver.find_element_by_xpath('//*[@id="side"]/div[1]')
    Search_bar.click()
    Search_User = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    Search_User.clear()
    Search_User.send_keys(User)
    sleep(1)
    Search_list = driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div[2]/div[1]/div')
    Search_list.click()

QR_cookies = webdriver.ChromeOptions()
QR_cookies.add_argument('--user-data-dir=C:\\Users\\amogh\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
QR_cookies.add_argument('--profile-data-directory=Default')
QR_cookies.add_argument('start-maximized')
QR_cookies.add_argument('--disable-infobars')

Path = "C:\\Program Files (x86)\\chromedriver.exe"
driver = webdriver.Chrome(Path, options=QR_cookies)
driver.get('Https://web.whatsapp.com')
sleep(10)

User_list = ["Abhijeet Gaonkar","Abhijeet Jio", "Atharva Patil","Raj (TE)","Jatin (TE)","Omkar (SE CO)"]

for User in User_list :
    try :
        Recent_chat = driver.find_element_by_xpath('//*[@title="{}"]'.format(User))
        Recent_chat.click()
    except nse:
        Search_chat(User)

    msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    msg_box.send_keys('Hi there, Whatsapp bot test')
    send_button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]')
    send_button.click()
