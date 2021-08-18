from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pickle


'''
driver = webdriver.Chrome()
driver.get('https://10fastfingers.com/')
sleep(10)
pickle.dump(driver.get_cookies() , open("Cookie.pkl","wb"))
driver.close()
'''


driver = webdriver.Firefox()
driver.get('https://10fastfingers.com/')
for cookie in pickle.load(open("Cookie.pkl", "rb")): 
    driver.add_cookie(cookie)


typing_test = driver.find_element_by_id('typing-test').click()


type_area = driver.find_element_by_xpath('//*[@id="inputfield"]')
parent_div = driver.find_element_by_xpath('//*[@id="row1"]')
count_of_span = len(parent_div.find_elements_by_xpath("./span"))


sleep(2)
for words in range(1,count_of_span + 1):
    word_path = '//*[@id="row1"]/span[' + str(words) + ']'
    word = driver.find_element_by_xpath(word_path).text
    type_area.send_keys(word)
    sleep(0.005)
    type_area.send_keys(Keys.SPACE)