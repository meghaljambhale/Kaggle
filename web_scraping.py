from selenium import webdriver                    #import webDriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')                             
chrome_options.add_argument('--disable-dev-shm-usage')
wd = webdriver.Chrome('chromedriver',chrome_options=chrome_options)


url = "https://www.amazon.in/" 
wd.get(url)

element = wd.find_element_by_id("twotabsearchtextbox")
from selenium.webdriver.common.keys import Keys
element.send_keys("Laptop")   #same as typing Laptop into the amazon search bar
element.send_keys(Keys.ENTER) #same as hitting enter
time.sleep(10)

elements = wd.find_elements_by_class_name('sg-col-inner')
def add_data(a,b,c):
    elements = wd.find_elements_by_class_name('sg-col-inner')
    for element in elements:
        try:
            name = element.find_element_by_xpath(".//span[@class = 'a-size-medium a-color-base a-text-normal']").text
            price = element.find_element_by_xpath(".//span[@class = 'a-price-whole']").text
            link = element.find_element_by_xpath(".//a[@class = 'a-size-base a-link-normal a-text-normal']").get_attribute('href')
            b.append(price)
            a.append(name)
            c.append(link)
        except:
            NoSuchElementException  
    return a,b,c
c = -1
import time
while c!=0:
    try:
        wd.find_element_by_xpath("//li[@class = 'a-last']/a").click()
        time.sleep(10)   
        names, prices ,links = add_data(names, prices ,links)
    except NoSuchElementException:
        print("end of Search Results")
        c = 0
