import datetime 
import time
from time import sleep
from selenium import webdriver
browser=webdriver.Chrome('.\\chromedriver_win32\\chromedriver.exe')
browser.get('http://web.whatsapp.com')

def conform():
    print("Did u scan the QR code")
    askUser=input("Press Y or N")
    if(askUser=='Y'):
        msg()
    elif(askUser=='N'):
        print("Pls Try again")
        conform()
    else:
        print("Pls Enter Valid")
        conform
def msg():
    name=input('Enter Group / User Name: ')
    
    try:
        user=browser.find_element_by_xpath('//span[@title="{}"]'.format(name))
        user.click()
    except:
        print("Exception")
        msg()
    message=f'Happy Birthday {name}'
    text_box=browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
    text_box.send_keys(message)
    print("Button")
    browser.find_element_by_class_name('_4sWnG').click()
conform()
msg()