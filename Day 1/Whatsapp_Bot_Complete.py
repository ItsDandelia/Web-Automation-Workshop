#First download the chrome webdriver from https://chromedriver.chromium.org/downloads
#Copy that .exe file in C:/Program Files(x86)
from time import sleep
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException as se


#Search Function for non-recent chats
def Search_chat(User):
    #Clickng search bar
    Search = driver.find_element_by_xpath('//div[@class="_2EoyP"]')
    Search.click()
    #Finding the User
    Search_user = driver.find_element_by_xpath('//div[@class="_3FRCZ copyable-text selectable-text"]')
    Search_user.clear()
    Search_user.send_keys(User)
    sleep(1)
    Search_Bar = driver.find_element_by_xpath('//span[@class="matched-text _3Whw5"]')
    Search_Bar.click()
    sleep(2)  # Increase if browser is slow


#By using the QR_cache we only need to scan QR code once
QR_cache = webdriver.ChromeOptions()
# path C:\\Users\\<Your username>\\AppData\\Local\\Google\\Chrome\\User Data\\Default
QR_cache.add_argument('--user-data-dir=C:\\Users\\amogh\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
QR_cache.add_argument('--profile-data-directory=Default')
QR_cache.add_argument('start-maximized')
QR_cache.add_argument('--disable-infobars')

#Setup Chrome Web driver
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH,options=QR_cache)
driver.get("https://web.whatsapp.com")
sleep(12)

#Fill the users in list you want to send message
User_list= ['Abhijeet Jio','Onkar','Abhijeet Gaonkar','Raj','Jatin (SE CO)',
            'Shubham (SE CO)','Omkar (SE CO)','Atharva Patil']

for User in User_list :
    try :
        #Find user in recent chat
        Search_Box = driver.find_element_by_xpath('//span[@title="{}"]'.format(User))
        Search_Box.click()


    except se :
        Search_chat(User)


    #Find msg box windows and sends text
    msg = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    sleep(1)
    msg.send_keys("Dream 11 pe team me bana leta hu aap ISA ka workshop attend karo")

    #Find send button and click it
    send_button = driver.find_element_by_xpath("//button[@class='_1U1xa']")
    #send_button.click()
    sleep(4)
