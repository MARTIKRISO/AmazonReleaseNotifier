from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import re, requests, json


with open("token.txt", "r") as apitoken:
    TOKEN = apitoken.read()



#TODO: hide the token, fix the spaghetti, make it pretty, add comments
def pushbullet_message(title, body):
    msg = {"type": "note", "title": title, "body": body}
    resp = requests.post('https://api.pushbullet.com/v2/pushes', 
                         data=json.dumps(msg),
                         headers={'Authorization': 'Bearer ' + TOKEN,
                                  'Content-Type': 'application/json'})
    if resp.status_code != 200:
        raise Exception(resp.status_code)
    else:
        print ('Message sent') 


url = "https://www.amazon.com/dp/B0815Y8J9N/ref=cm_sw_r_cp_apa_fabc_mCdPFbSG2B6PM"


driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

sleep(.00125)

content = driver.page_source.encode('utf-8').strip()

soup = BeautifulSoup(content, 'html.parser')

thing = "nope"
thing = soup.find(id = "availability")

if "Currently unavailable." in str(thing):
    pushbullet_message("Valk's CPU is OUT", "Go buy it")
driver.quit()