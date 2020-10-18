from stockfish import Stockfish
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import pyautogui
import time
import Passwords


# This is function is used to map x coordinate of white to chess coordinate
def get_key(val):
    for key, value in x_coords_white.items():
        if val == value:
            return key


# This is function is used to map y coordinate of white to chess coordinate
def get_key1(val):
    for key, value in y_coords_white.items():
        if val == value:
            return key


# Loading browser with default conditions
#options = Options()
#options.add_argument('start-maximized')
#options.add_argument('--disable-infobars')
#stockfish = Stockfish(
#        r"C:\Users\DANDELIA\Downloads\stockfish-11-win\stockfish-11-win\Windows\stockfish_20011801_x64.exe")
#driver = webdriver.Chrome(chrome_options=options, executable_path='C:\Program Files (x86)\chromedriver.exe')
#driver.get('https://lichess.org/login')

#Login process
#username = driver.find_element_by_xpath('//*[@id="form3-username"]')
#username.click()
#username.send_keys('Holmes1109')
#password = driver.find_element_by_xpath('//*[@id="form3-password"]')
#password.click()
#password.send_keys('hjdbjhd')
#password.send_keys(Passwords.chess())
#login = driver.find_element_by_xpath('//*[@id="main-wrap"]/main/form/div[1]/button')
#login.click()
#time.sleep(2)
#play = driver.find_element_by_xpath('//*[@id="main-wrap"]/main/div[1]/div[1]/a[3]')
#play.click()

#time.sleep(5)
#level = driver.find_element_by_xpath('//*[@id="config_level"]/group/div[4]/label')
#level.click()
#black = driver.find_element_by_xpath('//*[@id="modal-wrap"]/div/form/div[5]/button[1]')
#black.click()
#time.sleep(5)

# Setting initial position of board from start
#stockfish.set_fen_position('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')

# Dictionary for white coordinates
#x_coords_white = {'a': 951, 'b': 885, 'c': 818, 'd': 752, 'e': 686, 'f': 619, 'g': 553, 'h': 486}
#y_coords_white = {'1': 102, '2': 169, '3': 235, '4': 302, '5': 368, '6': 434, '7': 501, '8': 567}
#print(x_coords_white)
#print(y_coords_white)

#print(driver.get_window_size())

# Dictionary for black coordinates
#x_coord_black = {'a': 1155, 'b': 1128, 'c': 1051, 'd': 934, 'e': 863, 'f': 800, 'g': 720, 'h': 635}
#y_coord_black = {'1': 285, '2': 360, '3': 450, '4': 540, '5': 628, '6': 680, '7': 762, '8': 829}

#i = 0
#moves_history = []
#while True:
#    try:
#        print(i)
#        time.sleep(5)

        # If i is even then it is white's turn
#        if i % 2 == 0:
            # This will read the last move of white from lichess webpage and give its coordinates in x and y
#            xcoord2 = (int(driver.find_element_by_xpath(
#                '//*[@id="main-wrap"]/main/div[1]/div[1]/div/cg-helper/cg-container/cg-board/square[1]').location[
#                               'x']) + 40)
#            ycoord2 = (int(driver.find_element_by_xpath(
#                '//*[@id="main-wrap"]/main/div[1]/div[1]/div/cg-helper/cg-container/cg-board/square[1]').location[
#                               'y']) + 40)
#            xcoord1 = (int(driver.find_element_by_xpath(
#                '//*[@id="main-wrap"]/main/div[1]/div[1]/div/cg-helper/cg-container/cg-board/square[2]').location[
#                               'x'] + 40))
#            ycoord1 = (int(driver.find_element_by_xpath(
#                '//*[@id="main-wrap"]/main/div[1]/div[1]/div/cg-helper/cg-container/cg-board/square[2]').location[
#                               'y'] + 40))
#            print(xcoord1, ycoord1, xcoord2, ycoord2)
            # This will map the x,y coordinates of white to chess coordinates
#            xcoord1 = get_key(xcoord1)
#            ycoord1 = get_key1(ycoord1)
#            xcoord2 = get_key(xcoord2)
#            ycoord2 = get_key1(ycoord2)

#            moves_history.append(str(xcoord1) + str(ycoord1) + str(xcoord2) + str(ycoord2))
            # Giving stockfish the history of moves from start
            # stockfish.set_position(moves_history)
            # current = stockfish.get_fen_position()
            # print(current)
            # stockfish.set_fen_position(current)
#            i += 1
#            continue

#        print(moves_history)
        # Giving stockfish the history of moves from start
#        stockfish.set_position(moves_history)
#        current = stockfish.get_fen_position()
#        print(current)
#        stockfish.set_fen_position(current)
        # Predicting the next best move for black
#        next_move = str(stockfish.get_best_move())

#        if stockfish.is_move_correct(next_move):  # Checking if the predicted move is valid
#            moves_history.append(next_move)

#            print(next_move)
            # Converting the best move of black from chess coordinates to x,y coordinates
#            xcoord1 = int(x_coord_black[next_move[0]])
#            ycoord1 = int(y_coord_black[next_move[1]])
#            xcoord2 = int(x_coord_black[next_move[2]])
#            ycoord2 = int(y_coord_black[next_move[3]])
#            print(xcoord1, ycoord1, xcoord2, ycoord2)
#        else:
#            continue

        # Using pyautogui to move our black pieces on board
#        pyautogui.click(xcoord1, ycoord1, duration=1)
#        pyautogui.click(xcoord2, ycoord2, duration=1)
#        i += 1

#    except:
#        time.sleep(2)
#        driver.close()
#        break
