import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

pyautogui.FAILSAFE = True

def skipAd():
    while True:
        videoAdCords = pyautogui.locateCenterOnScreen("play.png")
        bannerCords = pyautogui.locateCenterOnScreen("bannerad.png")
        blackBannerCords = pyautogui.locateCenterOnScreen("black banner.png")

        if videoAdCords or bannerCords or blackBannerCords is not None:
            break
        
    if videoAdCords is not None:
        pyautogui.click(videoAdCords)
    elif bannerCords is not None:
        pyautogui.click(bannerCords)
    elif blackBannerCords is not None:
        pyautogui.click(blackBannerCords)

    skipAd()


musicOptions = ["> Choice(0)", "> Lofi Girl(1)", "> Workout(2)", "> Gaming(3)", "> Morning Tunes(4)", "> Inspirational(5)", "> Classical(6)", "> Fantasy(7)"]

print("What Playlist would you like to listen to?")
for i in musicOptions:
    print(i)

musicChoice = input("\n> ").lower()

if musicChoice == "choice" or musicChoice == "0":
    select = input("What song would you like to listen to? (Be Exact)\n")
    print("\nPlaying " + select + "...")

    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    driver.get("https://www.youtube.com/")

    search = driver.find_element("name", "search_query")
    search.send_keys(select)
    search.submit()

    try:
        element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, select))
        )
        element.click()

        skipAd()
    except:
        driver.quit()

    time.sleep(3600)

    driver.quit()





elif musicChoice == "lofi girl" or musicChoice == "1" or musicChoice == "lofi":
    print("Playing Chill Playlist...")

    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    driver.get("https://www.youtube.com/")

    search = driver.find_element("name", "search_query")
    search.send_keys("chill music")
    search.submit()

    try:
        element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "lofi hip hop radio - beats to relax/study to"))
        )
        element.click()

        skipAd()
    except:
        driver.quit()

    time.sleep(3600)

    driver.quit()


elif musicChoice == "workout" or musicChoice == "2":
    print("Playing Workout Playlist...")

    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    driver.get("https://www.youtube.com/")

    search = driver.find_element("name", "search_query")
    search.send_keys("super saiyan gym music")
    search.submit()

    try:
        element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "🔥All Saiyans Rage GYM Motivation Dragon Ball"))
        )
        element.click()

        skipAd()
    except:
        driver.quit()

    time.sleep(970)

    driver.quit()

elif musicChoice == "gaming" or musicChoice == "3":
    print("Playing Gaming Playlist...")

    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    driver.get("https://www.youtube.com/")

    search = driver.find_element("name", "search_query")
    search.send_keys("Gaming Music")
    search.submit()

    try:
        element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Best gaming music for TRYHARD No. 2"))
        )
        element.click()

        skipAd()
    except:
        driver.quit()

    time.sleep(3800)

    driver.quit()

elif musicChoice == "morning tunes" or musicChoice == "4" or musicChoice == "morning":
    print("Playing Morning Tunes Playlist...")

    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    driver.get("https://www.youtube.com/")

    search = driver.find_element("name", "search_query")
    search.send_keys("morning tunes")
    search.submit()

    try:
        element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Happy Morning Cafe Music - Relaxing Jazz & Bossa Nova Music For Work, Study, Wake up"))
        )
        element.click()

        skipAd()
    except:
        driver.quit()

    time.sleep(12600)

    driver.quit()

elif musicChoice == "inspirational" or musicChoice == "5":
    print("Playing Inspirational Playlist...")

    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    driver.get("https://www.youtube.com/")

    search = driver.find_element("name", "search_query")
    search.send_keys("inspirational music")
    search.submit()

    try:
        element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "6 Hours of The Best Epic Inspirational Music for Studying and Working"))
        )
        element.click()

        skipAd()
    except:
        driver.quit()

    time.sleep(21600)

    driver.quit()

elif musicChoice == "classical" or musicChoice == "6" or musicChoice == "classic":
    print("Playing Classical Playlist...")

    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    driver.get("https://www.youtube.com/")

    search = driver.find_element("name", "search_query")
    search.send_keys("classical music")
    search.submit()

    try:
        element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Classical Music Is NOT Boring"))
        )
        element.click()

        skipAd()
    except:
        driver.quit()

    time.sleep(8580)

    driver.quit()

elif musicChoice == "fantasy" or musicChoice == "7" or musicChoice == "tavern" or musicChoice == "dnd":
    print("Playing Fantasy Playlist...")

    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    driver.get("https://www.youtube.com/")

    search = driver.find_element("name", "search_query")
    search.send_keys("fantasy music")
    search.submit()

    try:
        element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Medieval Fantasy Music – Medieval Market | Folk, Traditional, Instrumental | Fantasy Music World #2"))
        )
        element.click()

        skipAd()
    except:
        driver.quit()

    time.sleep(3600)

    driver.quit()

elif musicChoice == "13":
    print("Playing " + "\033[1m" + "null" + "\033[1m" + " Playlist...")

    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    driver.get("https://www.youtube.com/")

    search = driver.find_element("name", "search_query")
    search.send_keys("heart broken")
    search.submit()

    try:
        element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "ＨＥＡＲＴＢＲＯＫＥＮ"))
        )
        element.click()

        skipAd()
    except:
        driver.quit()

    time.sleep(180)

    driver.quit()

else:
    print("Unable to complete request.")