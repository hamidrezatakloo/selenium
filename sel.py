from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
options = Options()
# options.headless = True
browser = webdriver.Firefox(options=options)
# browser.set_page_load_timeout(100)
browser.get('http://getlike.io/login')
username = browser.find_element_by_id('User_loginLogin')
username.send_keys('')
password = browser.find_element_by_id('User_passwordLogin')
password.send_keys('')
login = browser.find_element_by_name('submitLogin')
login.click()
tasks = browser.find_element_by_link_text('Биржа заданий')
tasks.click()
time.sleep(5)
isOK = True
#naruto
while isOK :
    firstClick = browser.find_element_by_link_text('0.08')
    firstClick.click()
    try:
        time.sleep(5)
        finded = browser.find_element_by_link_text('Проверить')
        print(finded.text)
        isOK=False
    except:
        continue
time.sleep(30)
browser.switch_to.window(browser.window_handles[1])
browser.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/span/a[1]/button').click()
time.sleep(5)
userInput = browser.find_element_by_name('username')
passInput = browser.find_element_by_name('password')
userInput.send_keys('sakurafabo')
passInput.send_keys('fagfagfag12')
login = browser.find_element_by_tag_name('button')
login.submit()
time.sleep(5)
saveInfo = browser.find_element_by_tag_name('button')
saveInfo.click()
time.sleep(5)
fallow_button = browser.find_element_by_tag_name('button')
fallow_button.click()
browser.close()
browser.switch_to.window(browser.window_handles[0])
time.sleep(4)
def do():
    time.sleep(5)
    Fclicks = browser.find_elements_by_link_text('0.08')
    for Fclick in Fclicks:
        Fclick.click()
        time.sleep(5)
        task_page = browser.window_handles[0]
        try:
            confirm = browser.find_element_by_link_text('Проверить')
            insta_page = browser.window_handles[1]
            browser.switch_to.window(insta_page)
            time.sleep(40)
            fallow_button = browser.find_element_by_tag_name('button')
            fallow_button.click()
            browser.close()
            browser.switch_to.window(task_page)
            time.sleep(4)
        except:
            time.sleep(4)
            continue

do()
browser.refresh()
time.sleep(10)
do()
browser.refresh()
time.sleep(10)
do()
# isOk = 
# print(isOk.text)
